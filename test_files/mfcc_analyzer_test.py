from mfcc_analyzer_knn import MFCCAnalyzer
import os

d_analyzer = MFCCAnalyzer('../mfcc_database', 'database.json')
d_analyzer.train_models()
# print(d_analyzer.x_test)
# print(d_analyzer.y_test)

file_names = os.listdir('../instruments_files/test/random')
for e in file_names:
    type = d_analyzer.predict_instrument('../instruments_files/test/random', e)
    print(e + ': ' + type)

# print(d_analyzer.calculate_accuracy())
