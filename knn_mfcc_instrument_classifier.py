import essentia
import essentia.standard as es
import os
import pandas as pd
from pathlib import Path
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from joblib import dump, load


class MFCCClassifier:

    def __init__(self, database_path, trained_model_path):

        if trained_model_path is not None:
            path = Path(trained_model_path + '.joblib')
            self.import_classifier(path)
            return

        self.database_file_path = Path(database_path)

        # Load database if exists
        if os.path.isfile(self.database_file_path):
            self.database = pd.read_json(self.database_file_path, orient='index')

        # Useful variables
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None

        # kNN Classifier
        self.knn = KNeighborsClassifier(n_neighbors=3)

    def train_models(self, model_name):

        # Removing the 'genre' column to train the algorithm
        x = self.database.drop(columns=['type'])
        y = self.database.type.values

        x = x.mfcc.apply(pd.Series)

        # Splitting the DF to get 80/20 elements
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=0.2, random_state=1,
                                                                                stratify=y)
        # Training
        self.knn.fit(self.x_train, self.y_train)

        # Export model
        self.export_classifier(self.knn, model_name)

    '''
    Testing the algorithm with the 20% of the dataset
    '''

    def predict_instrument_test(self):
        return self.knn.predict(self.x_test)

    '''
    Predicting the genre of a single track
    '''

    def predict_instrument(self, folder_path, name):

        track_path = Path(folder_path) / name

        if not os.path.isfile(track_path):
            return 'The file does not exist'

        # Given track parameters
        # Compute all features, aggregate only 'mean' and 'stdev' statistics for all low-level, rhythm and tonal frame features
        features, features_frames = es.MusicExtractor(lowlevelStats=['mean'],
                                                      rhythmStats=['mean'],
                                                      tonalStats=['mean'])(str(track_path))

        # Creating the row for the dataframe
        file_values = [{'element': name, 'mfcc': features['lowlevel.mfcc.mean']}]

        # Creating new DataFrame
        file_df = pd.DataFrame(file_values)
        file_df.set_index('element', inplace=True)
        file_df = file_df.mfcc.apply(pd.Series)

        # Executing the kNN algorithm
        return self.knn.predict(file_df)

    '''
    Getting the accuracy of the system
    '''

    def calculate_accuracy(self):
        if not hasattr(self, 'x_test'):
            print('No test dataset')
            return

        if not hasattr(self, 'y_test'):
            print('No test dataset')
            return

        return self.knn.score(self.x_test, self.y_test)

    '''
    Export classifier
    '''

    def export_classifier(self, classifier, file_name):
        dump(classifier, file_name + '.joblib')
        return

    '''
    Import classifier
    '''

    def import_classifier(self, file_name):
        self.knn = load(file_name)
