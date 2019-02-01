from audio_meters import AudioMeters
from bpm_analyzer import BPMAnalyzer
import os
import pandas as pd
from pathlib import Path
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split


class DataAnalyzerSVC:

    def __init__(self, database_path, database_file_name):

        if not os.path.exists(database_path):
            return

        self.database_file_path = Path(database_path) / database_file_name

        # Load database if exists
        if os.path.isfile(self.database_file_path):
            self.genres_database = pd.read_json(self.database_file_path, orient='index')
            self.genres_database.index.name = 'name'

        # Useful variables
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None

        # kNN Classifier
        self.svc = SVC(gamma='auto')

    def train_models(self):

        # Removing the 'genre' column to train the algorithm
        x = self.genres_database.drop(columns=['genre'])
        y = self.genres_database.genre.values

        # Splitting the DF to get 80/20 elements
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=0.2, random_state=1,
                                                                                stratify=y)
        # Training
        self.svc.fit(self.x_train, self.y_train)

    '''
    Testing the algorithm with the 20% of the dataset
    '''

    def predict_genre_test(self):
        return self.svc.predict(self.x_test)

    '''
    Predicting the genre of a single track
    '''

    def predict_genre(self, folder_path, track_name):

        track_path = Path(folder_path) / track_name

        if not os.path.isfile(track_path):
            return 'The file does not exist'

        # Given track parameters
        measures = AudioMeters.get_loudness(str(track_path))

        # Extracting parameters
        lufs = measures['Integrated Loudness']['I']
        tp = measures['True Peak']['Peak']

        # Extracting BPM
        bpm_a = BPMAnalyzer(folder_path)
        bpm = bpm_a.get_bpm_single(track_name)
        print(bpm)

        # Creating the row for the dataframe
        track_values = [{'name': track_name, 'lufs': lufs, 'tp': tp, 'bpm': bpm}]

        # Creating new DataFrame
        track_df = pd.DataFrame(track_values)
        track_df.set_index('name', inplace=True)

        # Executing the kNN algorithm
        return self.svc.predict(track_df)

    '''
    Getting the accuracy of the system
    '''

    def calculate_accuracy(self):
        return self.svc.score(self.x_test, self.y_test)
