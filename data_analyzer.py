from file_converter import FileConverter
from audio_meters import AudioMeters
import os
import numpy as np
import pandas as pd
from pathlib import Path


class DataAnalyzer():

    def __init__(self, database_path, database_file_name):

        if not os.path.exists(database_path):
            return

        database_path = Path(database_path)
        self.database_file_path = database_path / database_file_name

        self.database_reader = FileConverter(database_path)

        # Load database if exists
        if os.path.isfile(self.database_file_path):
            self.genres_database = pd.DataFrame(self.database_reader.json_to_py(database_file_name))
            self.genres_database.set_index('name', inplace=True)




    def add_genre(self, folder_path, genre_name, tp_file_name, lufs_file_name):
        f_reader = FileConverter(folder_path)

        # Extracts the genre average values
        tp = f_reader.json_to_py(tp_file_name)['avg_tp']
        lufs = f_reader.json_to_py(lufs_file_name)['avg_lufs']

        genre = {
            'name': genre_name,
            'tp': tp,
            'lufs': lufs
        }

        # Add it to DB
        if self.genres_database.append(genre):
            return True

        return False

    # Exports DB to JSON file
    def save_database(self):
        if self.database_reader.py_to_json(self.genres_database, self.database_file_name):
            return True
        return False

    # Calculates the genre with the minimum distance between vectors
    def calculate_genre(self, track_path):
        if not os.path.isfile(track_path):
            return 'The file does not exist'

        # Given track parameters
        measures = AudioMeters.get_loudness(track_path)
        lufs = measures['Integrated Loudness']['I']
        tp = measures['True Peak']['Peak']
        track_values = [lufs, tp]

        # Aux vars for the loop
        most_alike_genre = None
        min_distance = None

        # Search for the most likely genre
        for genre in self.genres_database:

            # Genre parameters
            genre_values = [genre['lufs'], genre['tp']]

            # Distance between genres
            subs = np.subtract(track_values, genre_values)
            distance = np.linalg.norm(subs)
            print(distance)

            # If it is the first iteration, set that genre as most alike
            if not min_distance:
                min_distance = distance
                most_alike_genre = genre['name']
                continue

            # If the current distance is smaller than the previous, switch them
            if min_distance > distance:
                min_distance = distance
                most_alike_genre = genre['name']
                continue

        return most_alike_genre
