import sys

# from data_analyzer_knn import DataAnalyzer
# from data_analyzer_svc import DataAnalyzerSVC
# from emotions_analyzer import EmotionsDetector
from batch_reader import BatchReader

if len(sys.argv) < 2:
    sys.stderr.write("The command has not been introduced properly \n")
    sys.exit(-1)

mode = sys.argv[1]
p2 = None

if len(sys.argv) >= 3:
    p2 = sys.argv[2]

if mode == "-c" or mode == "--classifier":

    if p2 is None:
        sys.stderr.write("Please, introduce a valid mode \n")
        sys.exit(-1)

    if p2 == '-br' or p2 == '--batch_reader':
        path = None
        genre = None
        option = None

        if len(sys.argv) < 6:
            print("Missing parameters")
            sys.exit(-1)

        path = sys.argv[3]
        genre = sys.argv[4]
        option = sys.argv[5]

        br = BatchReader(path, genre)

        if option == "--add":
            if len(sys.argv) < 7:
                print("Missing export path")
                sys.exit(-1)

            if len(sys.argv) < 8:
                print("Missing database name")
                sys.exit(-1)

            br.add_existing_database(sys.argv[6], sys.argv[7])
            sys.exit(0)

        if option == "--run":
            br.run()
            sys.exit(0)

        if option == "--export":
            if len(sys.argv) < 7:
                print("Missing export path")
                sys.exit(-1)

            if len(sys.argv) < 8:
                print("Missing database name")
                sys.exit(-1)

            br.export(sys.argv[6], sys.argv[7])
            sys.exit(0)

        print("Wrong parameter")
        sys.exit(0)

    if p2 == "-d" or p2 == "--data_analyzer":
        print("Data analyzer")

        sys.exit(0)

    if p2 == "--svc":
        print("--svc")

        sys.exit(0)

    sys.stderr.write("Please, introduce a valid sintax (Tip: --help)  \n")
    sys.exit(-1)

if mode == "-h" or mode == "--help":
    sys.stderr.write("The second parameter in the command is the mode in which you want to use the system: \n")
    sys.stderr.write("-b or --basic for basic mode: in this case, the third parameter you have to introduce is ... \n")
    sys.stderr.write("-e or --expert for expert mode: in this case, the third parameter you have to introduce is the "
                     "classifier you want use: -knn or -svc \n")
    sys.stderr.write("-h or -help for help mode \n")
    sys.stderr.write("The fourth parameter is the path of the song you want to introduce in the system, "
                     "if necessary \n")
#
# else:
#
#     sys.stderr.write("The command has not been introduced properly \n")
#     sys.exit(-1)
