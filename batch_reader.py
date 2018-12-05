from audio_meters import AudioMeters
import os


class BatchReader():
    def __init__(self, folder_path):
        self.path = folder_path
        self.files = os.listdir(folder_path)
        self.database = []

    def run(self):
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

        return True
