from data_analyzer_knn import DataAnalyzer
from batch_reader import BatchReader

# Filling the DB
# br = BatchReader('../audio_files/edm_t', 'edm_t')
# br.run()
# br.export('../genres_database')

# br = BatchReader('../audio_files/reggaeton', 'reggaeton')
# br.add_existing_database('../genres_database')
# br.run()
# br.export('../genres_database')
#
# br2 = BatchReader('../audio_files/edm', 'edm')
# br2.add_existing_database('../genres_database')
# br2.run()
# br2.export('../genres_database')
#
# print(br.database)


d_analyzer = DataAnalyzer('../genres_database', 'database.json')

d_analyzer.train_models()
# print(d_analyzer.x_test)
# print(d_analyzer.y_test)
print(d_analyzer.predict_genre('../audio_files/test_tracks', 'DonDiablo.mp3'))
# print(d_analyzer.calculate_accuracy())
