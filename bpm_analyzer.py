from essentia.standard import *
from pathlib import Path
import os
import pandas as pd


class bpm_analyzer:

    def __init__(self, folder_path):
        self.fp = Path(folder_path)

        self.df = None

    def get_bpm_batch(self):

        files = os.listdir(self.fp)
        bpm_tracks = []

        for track in files:
            path_to_track = self.fp / track

            audio = MonoLoader(filename=str(path_to_track))()

            r_y = RhythmExtractor2013(method="multifeature")

            bpm, beats, beats_confidence, _, beats_intervals = r_y(audio)

            track_data = {
                'name': track,
                'bpm': bpm
            }

            bpm_tracks.append(track_data)

            print('Analyzed correctly: ' + track)

            df = pd.DataFrame(bpm_tracks, columns=['name', 'bpm'])
            df.set_index('name', inplace=True)

        # Check if the database exists or if it is None
        if not isinstance(self.df, pd.DataFrame):
            self.df = df
        else:
            self.df = self.df.append(df, ignore_index=False)

    def get_bpm_single(self, track_name):

        path_to_track = self.fp / track_name

        audio = MonoLoader(filename=str(path_to_track))()

        r_y = RhythmExtractor2013(method="multifeature")

        bpm, beats, beats_confidence, _, beats_intervals = r_y(audio)

        return bpm


    def export(self, file_path):

        # Create the folder if it does not exist
        if not os.path.exists(Path(file_path)):
            os.mkdir(Path(file_path))

        # Creating the paths
        database_path = Path(file_path) / 'database_bpm_310119.json'

        # Checking if everything's not null
        if isinstance(self.df, pd.DataFrame):
            self.df.to_json(database_path, orient='index')

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
        if isinstance(self.df, pd.DataFrame):
            self.df = self.df.append(pd.read_json(db_path, orient='index'), ignore_index=False)
        else:
            self.df = pd.read_json(db_path, orient='index')

        self.df.index.name = 'name'

        print('Database imported correctly')
        return True
