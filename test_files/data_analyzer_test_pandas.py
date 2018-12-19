from data_analyzer import DataAnalyzer

# Filling the DB
d_analyzer = DataAnalyzer('../genres_database', 'database.json')
# d_analyzer.add_genre('../genres_database/edm_t', 'edm_t')
# print(d_analyzer.genres_database)
# d_analyzer.add_genre('../genres_database/rock', 'rock')
# print(d_analyzer.genres_database)
# d_analyzer.save_database()
# d_analyzer.add_genre('../genres_database/edm', 'edm', 'avg_tp.json', 'avg_lufs.json')
# d_analyzer.add_genre('../genres_database/rock', 'rock', 'avg_tp.json', 'avg_lufs.json')
# d_analyzer.save_database()
g = d_analyzer.calculate_genre_euclidean_distance('../audio_files/test_tracks/asfos.mp3')
print(g)
