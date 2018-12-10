from file_converter import FileConverter
from audio_meters import AudioMeters
import os
import numpy as np


class DataAnalyzer():

    def __init__(self, database_path, database_file_name):
        self.genres_database = []
        self.database_file_name = database_file_name

        if not os.path.exists(database_path):
            return

        self.database_reader = FileConverter(database_path)

        if os.path.isfile(database_path + '/' + database_file_name):
            self.genres_database = self.database_reader.json_to_py(database_file_name)

    def add_genre(self, folder_path, genre_name, tp_file_name, lufs_file_name):
        f_reader = FileConverter(folder_path)

        tp = f_reader.json_to_py(tp_file_name)['avg_tp']
        lufs = f_reader.json_to_py(lufs_file_name)['avg_lufs']

        genre = {
            'name': genre_name,
            'tp': tp,
            'lufs': lufs
        }

        if self.genres_database.append(genre):
            return True

        return False

    def save_database(self):
        if self.database_reader.py_to_json(self.genres_database, self.database_file_name):
            return True
        return False

    def calculate_genre(self, track_path):
        if not os.path.isfile(track_path):
            return 'The file does not exist'

        measures = AudioMeters.get_loudness(track_path)

        lufs = measures['Integrated Loudness']['I']
        tp = measures['True Peak']['Peak']
        track_values = [lufs, tp]

        most_alike_genre = None
        comparison_value = None

        for genre in self.genres_database:
            genre_values = [genre['lufs'], genre['tp']]
            prod = np.dot(track_values, genre_values)
            # print(prod)

            if not comparison_value:
                comparison_value = prod
                most_alike_genre = genre['name']
                continue

            if comparison_value > prod:
                comparison_value = prod
                most_alike_genre = genre['name']
                continue

        return most_alike_genre


#################################################
##################### TEST ######################
#################################################

d_analyzer = DataAnalyzer('genres_database', 'database.json')
# d_analyzer.add_genre('output/edm', 'EDM', 'avg_tp.json', 'avg_lufs.json')
# # d_analyzer.save_database()
# # print(d_analyzer.genres_database)

# d_analyzer.add_genre('output/rock', 'rock', 'avg_tp.json', 'avg_lufs.json')
# d_analyzer.save_database()
print(d_analyzer.genres_database)

g = d_analyzer.calculate_genre('audio_files/test_tracks/asfos.mp3')
print(g)
