from mfcc_analyzer_knn import MFCCAnalyzer

d_analyzer = MFCCAnalyzer('../mfcc_database', 'database.json')
d_analyzer.train_models()
print(d_analyzer.x_test)
print(d_analyzer.y_test)
# print(d_analyzer.predict_genre('test_tracks', 'MiGente.mp3'))
print(d_analyzer.calculate_accuracy())
