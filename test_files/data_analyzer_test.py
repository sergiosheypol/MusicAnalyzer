from data_analyzer import DataAnalyzer

# Filling the DB
d_analyzer = DataAnalyzer('../genres_database', 'database.json')
# d_analyzer.add_genre('../genres_database/reggaeton', 'reggaeton', 'avg_tp.json', 'avg_lufs.json')
# d_analyzer.add_genre('../genres_database/edm', 'edm', 'avg_tp.json', 'avg_lufs.json')
# d_analyzer.add_genre('../genres_database/rock', 'rock', 'avg_tp.json', 'avg_lufs.json')
# d_analyzer.save_database()

g1 = d_analyzer.calculate_genre('../audio_files/test_tracks/bici.mp3')
print(g1)
# g2 = d_analyzer.calculate_genre('../audio_files/test_tracks/d.mp3')
# print(g2)
# g3 = d_analyzer.calculate_genre('../audio_files/test_tracks/sp.mp3')
# print(g3)
