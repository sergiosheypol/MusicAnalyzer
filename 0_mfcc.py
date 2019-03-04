import click
from mfcc_full_track_analyzer import TrackMFCCExtractor
from mfcc_average_coefs_reader_single_instrument import MFCCSingleInstrumentAnalyzer
from knn_mfcc_instrument_classifier import MFCCClassifier


@click.group()
def g():
    pass


@click.command()
@click.argument('filepath', required=True)
@click.argument('exportpath', required=True)
def analyzer_single(filepath, exportpath):
    analyzer = TrackMFCCExtractor(filepath)
    analyzer.run()
    analyzer.export(exportpath)
    click.echo("Track analyzed successfully")


@click.command()
@click.option('-p', '--parameters', nargs=2, required=True,
              help='Set folder to read (1st parameter) and instrument name (2nd parameter)')
@click.option('-a', '--add_database', required=False, nargs=2,
              help='Add existing database Parameters: path_to_db db_file_name')
@click.option('-r', '--run', nargs=2, required=True,
              help='Run and export a JSON file. Parameters: path_to_export db_name')
def analyzer_multi_average(parameters, add_database, run):
    click.echo(parameters)
    click.echo(add_database)
    click.echo(run)

    analyzer = MFCCSingleInstrumentAnalyzer(parameters[0], parameters[1])

    if len(add_database) == 2:
        existing_db_path = add_database[0]
        existing_db_name = add_database[1]
        analyzer.add_existing_database(existing_db_path, existing_db_name)

    analyzer.run()
    analyzer.export(run[0], run[1])
    click.echo("Track analyzed successfully")


@click.command()
@click.option('-m', '--model', required=False, nargs=2,
              help='Train a new model. Parameters: json_file_path model_path_to_export')
@click.option('-p', '--predict', required=False, nargs=3,
              help='Predict the genre of a given track. Parameters: path_to_model music_folder_path track_name')
def classificator(model, predict):
    if len(model) == 2:
        d_analyzer = MFCCClassifier(model[0], None)
        d_analyzer.train_models(model[1])
        accuracy = d_analyzer.calculate_accuracy()
        click.echo(accuracy)
        return accuracy

    elif len(predict) == 3:
        d_analyzer = MFCCClassifier(None, predict[0])
        genre = d_analyzer.predict_genre(predict[1], predict[2])
        click.echo('Predicted instrument: ' + genre[0])
        return genre


g.add_command(analyzer_single)
g.add_command(analyzer_multi_average)

if __name__ == '__main__':
    g()
