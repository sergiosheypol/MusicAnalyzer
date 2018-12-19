from data_analyzer import DataAnalyzer

# Filling the DB
d_analyzer = DataAnalyzer('../genres_database', 'database.json')
# d_analyzer.add_genre('../genres_database/reggaeton', 'reggaeton', 'avg_tp.json', 'avg_lufs.json')
# d_analyzer.add_genre('../genres_database/edm', 'edm', 'avg_tp.json', 'avg_lufs.json')
# d_analyzer.add_genre('../genres_database/rock', 'rock', 'avg_tp.json', 'avg_lufs.json')
# d_analyzer.save_database()
print(d_analyzer.database_file_path)
print(d_analyzer.genres_database)
