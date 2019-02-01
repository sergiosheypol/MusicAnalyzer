from data_analyzer_knn import DataAnalyzer
from batch_reader import BatchReader

# Filling the DB
# br = BatchReader('../audio_files/AmericanTrap', 'AmericanTrap')
# br.run()
# br.export('../genres_database')

# br = BatchReader('../audio_files/Uptempo', 'Uptempo')
# br.add_existing_database('../genres_database', 'database.json')
# br.run()
# br.export('../genres_database')

d_analyzer = DataAnalyzer('../genres_database', 'database.json')

d_analyzer.train_models()
print(d_analyzer.x_test)
print(d_analyzer.y_test)
# print(d_analyzer.predict_genre('test_tracks', 'MiGente.mp3'))
print(d_analyzer.calculate_accuracy())
