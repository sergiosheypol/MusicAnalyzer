import sys
from data_analyzer_knn import DataAnalyzer
from data_analyzer_svc import DataAnalyzerSVC
from emotions_analyzer import EmotionsDetector

if len(sys.argv) < 2 or len(sys.argv) > 3:

    sys.stderr.write("The command has not been introduced properly \n")
    sys.exit(-1)

else:
    mode = sys.argv[1]
    clas = sys.argv[2]
    path = sys.argv[3]

    if mode == "-b" or mode == "-basic":

        ed = EmotionsDetector()
        r = ed.get_emotions(path, '../emotions_models', 'speech_emotions_test')
        print(r)

    elif mode == "-e" or mode == "-expert":

        if clas == "-knn":

            d_analyzer = DataAnalyzer('../genres_database', 'database.json')
            d_analyzer.train_models()
            print(d_analyzer.x_test)
            print(d_analyzer.y_test)
            print(d_analyzer.predict_genre(path)) #esto seguramente esta mal pero no se como es
            print(d_analyzer.calculate_accuracy())

        elif clas == "-svc":

            d_analyzer = DataAnalyzerSVC('../genres_database', 'database.json')
            d_analyzer.train_models()
            print(d_analyzer.x_test)
            print(d_analyzer.y_test)
            print(d_analyzer.predict_genre(path)) #esto seguramente esta mal pero no se como es
            print(d_analyzer.calculate_accuracy())

        else:
            sys.stderr.write("Please, introduce a valid classifier \n")
            sys.exit(-1)

    elif mode == "-h" or mode == "-help":

        sys.stderr.write("The second parameter in the command is the mode in which you want to use the system: \n")
        sys.stderr.write("-b or - basic for basic mode: in this case, the third parameter you have to introduce is ... \n")
        sys.stderr.write("-e or - basic for expert mode: in this case, the third parameter you have to introduce is the classifier you want use: -knn or -svc \n")
        sys.stderr.write("-h or -help for help mode \n")
        sys.stderr.write("The fourth parameter is the path of the song you want to introduce in the system, if necessary \n")

    else:

        sys.stderr.write("The command has not been introduced properly \n")
        sys.exit(-1)