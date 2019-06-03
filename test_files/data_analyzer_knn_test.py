from knn_genre_classifier import KNNGenreClassifier

d_analyzer = KNNGenreClassifier(None, 'LiveDemo')
g = d_analyzer.predict_genre('../Music/','Avicii - SOS (Laidback Luke Tribute Remix Radio Edit).mp3')
print(g)