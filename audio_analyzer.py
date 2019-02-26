import click
from batch_reader import BatchReader
from data_analyzer_knn import DataAnalyzer


@click.group()
def g():
    pass


@click.command()
@click.option('-br', '--batch_reader', nargs=2, required=True,
              help='Set folder to read (1st parameter) and genre (2nd parameter)')
@click.option('-a', '--add_database', required=False, nargs=2,
              help='Add existing database Parameters: path_to_db db_file_name')
@click.option('-r', '--run', nargs=2, required=True,
              help='Run and export a JSON file. Parameters: path_to_export db_name')
def analyzer(batch_reader, add_database, run):
    path = batch_reader[0]
    genre = batch_reader[1]

    existing_db_path = None
    existing_db_name = None
    br = BatchReader(path, genre)

    if len(add_database) == 2:
        existing_db_path = add_database[0]
        existing_db_name = add_database[1]
        br.add_existing_database(existing_db_path, existing_db_name)

    br.run()
    output_path = run[0]
    output_db = run[1]

    br.export(output_path, output_db)


@click.command()
@click.option('-m', '--model', required=False, nargs=2,
              help='Train a new model. Parameters: json_file_path model_path_to_export')
@click.option('-p', '--predict', required=False, nargs=3,
              help='Predict the genre of a given track. Parameters: path_to_model music_folder_path track_name')
def classifier(model, predict):
    if len(model) == 2:
        d_analyzer = DataAnalyzer(model[0], None)
        d_analyzer.train_models(model[1])
        accuracy = d_analyzer.calculate_accuracy()
        click.echo(accuracy)  # TEST ME!
        return accuracy

    elif len(predict) == 3:
        d_analyzer = DataAnalyzer(None, predict[0])
        genre = d_analyzer.predict_genre(predict[1], predict[2])
        click.echo('Predicted genre: ' + genre[0])
        return genre

g.add_command(analyzer)
g.add_command(classifier)

if __name__ == '__main__':
    g()
