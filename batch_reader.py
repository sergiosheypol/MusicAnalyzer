from audio_meters import AudioMeters
from file_converter import FileConverter
import os
import numpy as np
import pandas as pd
from pathlib import Path


class BatchReader():
    def __init__(self, folder_path):

        if not os.path.exists(folder_path):
            print('BatchReader: That folder does not exist')
            return

        # Where to find the mp3 files
        self.path = folder_path

        # Names of the files in that folder
        self.files = os.listdir(folder_path)

        # Storage for analyzed values
        self.analyzed_tracks_database = []

        # Average True Peak value of the analyzed files
        self.average_tp = None

        # Average LUFS value of the analyzed files
        self.average_lufs = None

    # Analyze a music folder
    def run(self):
        # Analyzer
        for track in self.files:
            path = Path(self.path) / track

            measures = AudioMeters.get_loudness(str(path))

            tp = measures['True Peak']['Peak']
            lufs = measures['Integrated Loudness']['I']

            self.analyzed_tracks_database.append([track, lufs, tp])
            print(track + " has been added successfully")

        # Create DataFrame
        self.database = pd.DataFrame(self.analyzed_tracks_database, columns=['name', 'lufs', 'tp'])
        self.database.set_index('name', inplace=True)

        # Calculate average values
        stats = self.database.mean()
        self.average_lufs = stats.lufs
        self.average_tp = stats.tp




    # Export the results into JSON
    def export(self, file_path):

        # Checking if everything's not null
        # TWEAK!!
        # if self.database:
        #
        self.database.to_json(Path(file_path), orient='records')

        # if self.average_lufs:
        #     fc.py_to_json(self.average_lufs, 'avg_lufs.json')
        #
        # if self.average_tp:
        #     fc.py_to_json(self.average_tp, 'avg_tp.json')

    # Add an existing LUFS database
    def add_existing_lufs_database(self, folder_path, file):

        if not os.path.exists(folder_path):
            print('The folder does not exist')
            return False

        if not os.path.isfile(file):
            print('The file does not exist')
            return False

        # Create JSON converter
        fc = FileConverter(folder_path)

        # Create aux database
        lufs_database = fc.json_to_py(file)

        # Move it to self object
        self.lufs_database = lufs_database

        print('LUFS database imported correctly')

        return True

    # Add an existing TP database
    def add_existing_tp_database(self, folder_path, file):

        if not os.path.exists(folder_path):
            print('The folder does not exist')
            return False

        if not os.path.isfile(file):
            print('The file does not exist')
            return False

        # Create JSON converter
        fc = FileConverter(folder_path)

        # Create aux database
        tp_database = fc.json_to_py(file)

        # Move it to self object
        self.tp_database = tp_database

        print('TP database imported correctly')

        return True

