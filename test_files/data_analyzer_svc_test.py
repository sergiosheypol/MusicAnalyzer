from svc_genre_classifier import SVCGenreClassifier
from batch_analyzer import BatchAnalyzer

# Filling the DB
# br = BatchReader('../audio_files/AmericanTrap', 'AmericanTrap')
# br.run()
# br.export('../genres_database')

# br = BatchReader('../audio_files/Uptempo', 'Uptempo')
# br.add_existing_database('../genres_database', 'database_working_010219.json')
# br.run()
# br.export('../genres_database')

# d_analyzer = DataAnalyzerSVC('../genres_database/database.json', None)
d_analyzer = SVCGenreClassifier(None, 'sv1')
# d_analyzer.train_models('sv1')
# print(d_analyzer.x_test)
# print(d_analyzer.y_test)
print(d_analyzer.predict_genre('test_tracks', 'MiGente.mp3'))
# print(d_analyzer.calculate_accuracy())
