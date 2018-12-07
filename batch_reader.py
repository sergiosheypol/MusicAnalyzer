from audio_meters import AudioMeters
import os
import numpy as np


class BatchReader():
    def __init__(self, folder_path):
        # Where to find the mp3 files
        self.path = folder_path

        # Names of the files in that folder
        self.files = os.listdir(folder_path)

        # Storage for analyzed values
        self.lufs_database = []
        self.tp_database = []

        # Average True Peak value of the analyzed files
        self.average_tp = None

        # Average LUFS value of the analyzed files
        self.average_lufs = None

    def run(self):
        # Auxiliar lists. It helps simplify calculating average value
        lufs_aux = []
        tp_aux = []

        # Analyzer
        for track in self.files:
            measures = AudioMeters.get_loudness(self.path + '/' + track)

            tp = {
                track: measures['True Peak']['Peak']
            }

            lufs = {
                track: measures['Integrated Loudness']['I']
            }

            # Store values
            self.lufs_database.append(lufs)
            self.tp_database.append(tp)

            # Preparing values to be computed
            lufs_aux.append(measures['Integrated Loudness']['I'])
            tp_aux.append(measures['True Peak']['Peak'])

            print(track + " has been added successfully")

        # Calculate the mean value of each parameter
        self.average_lufs = np.mean(lufs_aux)
        self.average_tp = np.mean(tp_aux)
