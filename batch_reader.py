from audio_meters import AudioMeters
from file_converter import FileConverter
import os
import numpy as np


class BatchReader():
    def __init__(self, folder_path):
        # Where to find the mp3 files
        self.path = folder_path

        # Names of the files in that folder
        self.files = os.listdir(folder_path)

        # Storage for analyzed values
        self.lufs_database = []
        self.tp_database = []

        # Average True Peak value of the analyzed files
        self.average_tp = None

        # Average LUFS value of the analyzed files
        self.average_lufs = None

    # Analyze a music folder
    def run(self):
        # Analyzer
        for track in self.files:
            measures = AudioMeters.get_loudness(self.path + '/' + track)

            tp = {
                track: measures['True Peak']['Peak']
            }

            lufs = {
                track: measures['Integrated Loudness']['I']
            }

            # Store values
            self.lufs_database.append(lufs)
            self.tp_database.append(tp)

            print(track + " has been added successfully")

        # Calculate the mean value of each parameter
        self.calculate_avg_lufs()
        self.calculate_avg_tp()

    # Export the results into JSON
    def export(self, folder_path):
        fc = FileConverter(folder_path)

        # Checking if everything's not null
        if self.lufs_database:
            fc.py_to_json(self.lufs_database, 'lufs.json')

        if self.tp_database:
            fc.py_to_json(self.tp_database, 'tp.json')

        if self.average_lufs:
            fc.py_to_json(self.average_lufs, 'avg_lufs.json')

        if self.average_tp:
            fc.py_to_json(self.average_tp, 'avg_tp.json')

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

    # Calculate the average lufs value from a given database
    def calculate_avg_lufs(self):

        if not self.lufs_database:
            return False

        values = []

        # Read all tracks in database
        for track in self.lufs_database:
            value = list(track.values())
            values.append(value)

        # Calculate the avg LUFS value
        self.average_lufs = {
            'avg_lufs': np.mean(values)
        }

        return True

    # Calculate the average tp value from a given database
    def calculate_avg_tp(self):

        if not self.tp_database:
            return False

        values = []

        # Read all tracks in database
        for track in self.tp_database:
            value = list(track.values())
            values.append(value)

        # Calculate the avg TP value
        self.average_tp = {
            'avg_tp': np.mean(values)
        }

        return True
