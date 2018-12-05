from audio_meters import AudioMeters
import os


class BatchReader():
    def __init__(self, folder_path):
        self.path = folder_path
        self.files = os.listdir(folder_path)
        self.database = []
        self.average_tp = None
        self.average_lufs = None


    def run(self):

        lufs_database = []
        tp_database = []

        for track in self.files:
            measures = AudioMeters.get_loudness(self.path + '/' + track)
            data = {
                'name': track,
                'params': {
                    'LUFS': measures['Integrated Loudness']['I'],
                    'TP': measures['True Peak']['Peak']
                }
            }

            self.database.append(data)
            lufs_database.append(measures['Integrated Loudness']['I'])
            tp_database.append(measures['True Peak']['Peak'])
            print(track + " has been added successfully")

        self.average_lufs = self.get_average_lufs(lufs_database)
        self.average_tp = self.get_average_tp(tp_database)

    def get_average_lufs(self, lufs_database):

        lufs_database_sum = 0.0

        for i in lufs_database:
            lufs_database_sum += i

        return lufs_database_sum / len(lufs_database)

    def get_average_tp(self, tp_database):

        tp_database_sum = 0.0

        for i in tp_database:
            tp_database_sum += i

        return tp_database_sum / len(tp_database)
