import os
import pandas as pd
from pathlib import Path
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


class MFCCFullTrackAnalyzer:

    def __init__(self, track_mfcc_db_path, instrument_sample_db_path):

        if not os.path.isfile(track_mfcc_db_path):
            print('Error in path: ' + track_mfcc_db_path)
            return

        if not os.path.isfile(instrument_sample_db_path):
            print('Error in path: ' + instrument_sample_db_path)
            return

        self.track_mfcc_db_path = pd.read_json(Path(track_mfcc_db_path), orient='index')
        self.instrument_sample_db_path = pd.read_json(Path(instrument_sample_db_path), orient='index')

        # Useful variables
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None

        # kNN Classifier
        self.knn = KNeighborsClassifier(n_neighbors=3)

    def train_models(self):

        # Removing the 'genre' column to train the algorithm
        x = self.instrument_sample_db_path.drop(columns=['type'])
        y = self.instrument_sample_db_path.type.values

        x = x.mfcc.apply(pd.Series)

        # Splitting the DF to get 80/20 elements
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=0.2, random_state=1,
                                                                                stratify=y)
        # Training
        self.knn.fit(self.x_train, self.y_train)

    '''
    Predicting the genre of a single track
    '''

    def predict_instrument(self):
        for i in self.track_mfcc_db_path.index:
            df = pd.DataFrame(self.track_mfcc_db_path.iloc[i])
            df = df.sort_index()
            df = df.transpose()

            print(self.knn.predict(df))


classifier = MFCCFullTrackAnalyzer('mfcc_database/mfcc_db_tracks/mfcc.json', 'mfcc_database/database_kick_snare.json')
classifier.train_models()
classifier.predict_instrument()
