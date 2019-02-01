from audio_meters import AudioMeters
import os
import pandas as pd
from pathlib import Path
from bpm_analyzer import bpm_analyzer


class BatchReader:
    def __init__(self, folder_path, genre):

        # Check if folder exists
        if not os.path.exists(folder_path):
            print('BatchReader: That folder does not exist')
            return

        # Where to find the mp3 files
        self.path = folder_path

        # Genre name
        self.genre = genre

        # Names of the files in that folder
        self.files = os.listdir(folder_path)

        # DataFrames to store the data
        self.database = None

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

            # Extracting BPM
            bpm_a = bpm_analyzer(self.path)
            bpm = bpm_a.get_bpm_single(track)

            analyzed_tracks_database.append([track, bpm, lufs, tp, self.genre])
            print(track + " has been added successfully")

        # Create DataFrame
        df = pd.DataFrame(analyzed_tracks_database, columns=['name', 'bpm', 'lufs', 'tp', 'genre'])
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
            self.database = self.database.append(pd.read_json(db_path, orient='index'), ignore_index=False)
        else:
            self.database = pd.read_json(db_path, orient='index')

        self.database.index.name = 'name'

        print('Database imported correctly')
        return True

