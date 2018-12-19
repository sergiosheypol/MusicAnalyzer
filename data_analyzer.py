from audio_meters import AudioMeters
import os
import pandas as pd
from pathlib import Path


class DataAnalyzer:

    def __init__(self, database_path, database_file_name):

        if not os.path.exists(database_path):
            return

        self.database_file_path = Path(database_path) / database_file_name

        self.genres_database = None

        # Load database if exists
        if os.path.isfile(self.database_file_path):
            self.genres_database = pd.read_json(self.database_file_path, orient='index')
            self.genres_database.index.name = 'genre'

    def add_genre(self, folder_path, genre_name):

        avg_genre_values = pd.read_json(Path(folder_path) / 'avg.json', orient='records')

        genre_df = pd.DataFrame(avg_genre_values)

        genre_df.rename(index={0: genre_name}, inplace=True)

        # Add it to DB
        if isinstance(self.genres_database, pd.DataFrame):
            self.genres_database = self.genres_database.append(genre_df, ignore_index=False)
        else:
            self.genres_database = genre_df
            self.genres_database.index.name = 'genre'

        self.genres_database = self.genres_database.drop_duplicates(keep='first')


    # Exports DB to JSON file
    def save_database(self):
        if isinstance(self.genres_database, pd.DataFrame):
            self.genres_database.to_json(self.database_file_path, orient='index')

    # Calculates the genre with the minimum distance between vectors
    # def calculate_genre(self, track_path):
    #     if not os.path.isfile(track_path):
    #         return 'The file does not exist'
    #
    #     # Given track parameters
    #     measures = AudioMeters.get_loudness(track_path)
    #     lufs = measures['Integrated Loudness']['I']
    #     tp = measures['True Peak']['Peak']
    #     track_values = [lufs, tp]
    #
    #     # Aux vars for the loop
    #     most_alike_genre = None
    #     min_distance = None
    #
    #     # Search for the most likely genre
    #     for genre in self.genres_database:
    #
    #         # Genre parameters
    #         genre_values = [genre['lufs'], genre['tp']]
    #
    #         # Distance between genres
    #         subs = np.subtract(track_values, genre_values)
    #         distance = np.linalg.norm(subs)
    #         print(distance)
    #
    #         # If it is the first iteration, set that genre as most alike
    #         if not min_distance:
    #             min_distance = distance
    #             most_alike_genre = genre['name']
    #             continue
    #
    #         # If the current distance is smaller than the previous, switch them
    #         if min_distance > distance:
    #             min_distance = distance
    #             most_alike_genre = genre['name']
    #             continue
    #
    #     return most_alike_genre
