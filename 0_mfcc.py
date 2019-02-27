import click
from mfcc_full_track_analyzer import TrackMFCCExtractor
from mfcc_average_coefs_reader_single_instrument import MFCCSingleInstrumentAnalyzer
from knn_mfcc_instrument_classifier import MFCCAnalyzer


@click.group()
def g():
    pass


#
# @click.command()
# @click.option('-br', '--batch_reader', nargs=2, required=True,
#               help='Set folder to read (1st parameter) and genre (2nd parameter)')
# @click.option('-a', '--add_database', required=False, nargs=2,
#               help='Add existing database Parameters: path_to_db db_file_name')
# @click.option('-r', '--run', nargs=2, required=True,
#               help='Run and export a JSON file. Parameters: path_to_export db_name')
# def analyzer(batch_reader, add_database, run):
#
#
#
# @click.command()
# @click.option('-m', '--model', required=False, nargs=2,
#               help='Train a new model. Parameters: json_file_path model_path_to_export')
# @click.option('-p', '--predict', required=False, nargs=3,
#               help='Predict the genre of a given track. Parameters: path_to_model music_folder_path track_name')
# def classifier(model, predict):


@click.command()
@click.argument('filepath', required=True, help='File to analyze')
@click.argument('exportpath', required=True, help='Path to export the results')
def read_single_track(filepath, exportpath):
    analyzer = TrackMFCCExtractor(filepath)
    analyzer.run()
    analyzer.export(exportpath)


# g.add_command(analyzer)
# g.add_command(classifier)
g.add_command(read_single_track)

if __name__ == '__main__':
    g()
