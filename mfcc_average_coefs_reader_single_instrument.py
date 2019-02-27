import essentia
import essentia.standard as es
from pathlib import Path
import os
import pandas as pd


class MFCCSingleInstrumentAnalyzer:

    def __init__(self, folder_path, type_of_instrument):
        if not os.path.exists(folder_path):
            print('AudioFeaturesExtractor: That folder does not exist')
            return

        self.type = type_of_instrument

        self.path = Path(folder_path)

        self.file_names = os.listdir(self.path)

        self.database = None

    def run(self):
        # Aux lib to store analyzed tracks
        analyzed_tracks_database = []

        for element in self.file_names:
            path = self.path / element

            # Compute all features, aggregate only 'mean' and 'stdev' statistics for all low-level, rhythm and tonal frame features
            features, features_frames = es.MusicExtractor(lowlevelStats=['mean'],
                                                          rhythmStats=['mean'],
                                                          tonalStats=['mean'])(str(path))

            analyzed_tracks_database.append([element, self.type, features['lowlevel.mfcc.mean']])

        # Create DataFrame
        df = pd.DataFrame(analyzed_tracks_database, columns=['element', 'type', 'mfcc'])
        df.set_index('element', inplace=True)

        # Check if the database exists or if it is None
        if not isinstance(self.database, pd.DataFrame):
            self.database = df
        else:
            self.database = self.database.append(df, ignore_index=True)

    def export(self, file_path, db_name):
        # Create the folder if it does not exist
        if not os.path.exists(Path(file_path)):
            os.mkdir(Path(file_path))

        # Creating the paths
        database_path = Path(file_path) / db_name

        # Checking if everything's not null
        if isinstance(self.database, pd.DataFrame):
            self.database.to_json(database_path, orient='index')

    # Add an existing database
    def add_existing_database(self, folder_path, db_name):

        # Path to database
        db_path = Path(folder_path) / db_name

        # Check if the file exists
        if not os.path.isfile(db_path):
            print('The file does not exist')
            return False

        '''
        The method .append() does not work in place. Instead, you need to overwrite the previous object
        '''
        if isinstance(self.database, pd.DataFrame):
            self.database = self.database.append(pd.read_json(db_path, orient='index'), ignore_index=True)
        else:
            self.database = pd.read_json(db_path, orient='index')

        self.database.index.name = 'element'

        print('Database imported correctly')
        return True


# af = AudioFeaturesExtractor('instruments_files/crash', 'crash')
# af.run()
# af.export('mfcc_database/','database.json')

af = MFCCSingleInstrumentAnalyzer('instruments_files/piano', 'piano')
af.add_existing_database('mfcc_database/', 'database.json')
af.run()
af.export('mfcc_database/', 'database.json')
