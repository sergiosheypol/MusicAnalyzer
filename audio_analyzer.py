import click
from batch_reader import BatchReader


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
def classifier():
    click.echo("Hola")


g.add_command(analyzer)
g.add_command(classifier)

if __name__ == '__main__':
    g()
