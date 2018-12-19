from audio_meters import AudioMeters
import os
import pandas as pd
from pathlib import Path


class BatchReader:
    def __init__(self, folder_path):

        # Check if folder exists
        if not os.path.exists(folder_path):
            print('BatchReader: That folder does not exist')
            return

        # Where to find the mp3 files
        self.path = folder_path

        # Names of the files in that folder
        self.files = os.listdir(folder_path)

        # DataFrames to store the data
        self.database = None
        self.avg_values = None

    # Analyze a music folder
    def run(self):

        # Aux lib to store analyzed tracks
        analyzed_tracks_database = []

        # Analyzer
        for track in self.files:
            path = Path(self.path) / track

            measures = AudioMeters.get_loudness(str(path))

            tp = measures['True Peak']['Peak']
            lufs = measures['Integrated Loudness']['I']

            analyzed_tracks_database.append([track, lufs, tp])
            print(track + " has been added successfully")

        # Create DataFrame
        df = pd.DataFrame(analyzed_tracks_database, columns=['name', 'lufs', 'tp'])
        df.set_index('name', inplace=True)

        # Check if the database exists or if it is None
        if not isinstance(self.database, pd.DataFrame):
            self.database = df
        else:
            self.database = self.database.append(df, ignore_index=False)

    # Export the results into JSON
    def export(self, file_path):

        # Create the folder if it does not exist
        if not os.path.exists(Path(file_path)):
            os.mkdir(Path(file_path))

        # Creating the paths
        database_path = Path(file_path) / 'database.json'
        avg_values_path = Path(file_path) / 'avg.json'

        # Checking if everything's not null
        if not self.database.empty:
            self.database.to_json(database_path, orient='index')

        if not self.avg_values.empty:
            self.avg_values.to_json(avg_values_path, orient='records')

    # Add an existing database
    def add_existing_database(self, folder_path):

        db_path = Path(folder_path) / 'database.json'

        if not os.path.isfile(db_path):
            print('The file does not exist')
            return False

        '''
        The method .append() does not work in place. Instead, you need to overwrite the previous object
        '''
        if isinstance(self.database, pd.DataFrame):
            self.database = self.database.append(pd.read_json(db_path, orient='index'), ignore_index=False)
        else:
            self.database = pd.read_json(db_path, orient='index')

        self.database.index.name = 'name'

        print('LUFS database imported correctly')
        return True

    def calculate_average_values(self):
        # Calculate average values
        stats = self.database.mean()

        # Store new values
        aux_avg = [{'lufs': stats.lufs, 'tp': stats.tp}]
        self.avg_values = pd.DataFrame(aux_avg)
