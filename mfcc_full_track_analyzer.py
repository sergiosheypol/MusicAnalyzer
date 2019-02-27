import essentia
from essentia.standard import *
import pandas as pd
from pathlib import Path
from pylab import plot, show, figure, imshow
import matplotlib.pyplot as plt


class TrackMFCCExtractor:
    def __init__(self, file_path):
        self.path = Path(file_path)
        self.mfccs = None
        self.melbands = None
        self.melbands_log = None

    def run(self):
        # we start by instantiating the audio loader:
        loader = essentia.standard.MonoLoader(filename=str(self.path))

        # and then we actually perform the loading:
        audio = loader()

        w = Windowing(type='hann')
        spectrum = Spectrum()  # FFT() would return the complex FFT, here we just want the magnitude spectrum
        mfcc = MFCC()
        logNorm = UnaryOperator(type='log')

        mfccs = []
        melbands = []
        melbands_log = []

        bpm = 128
        fr = 44100
        hopSize_seg = 4 * 60 / bpm  # 4Beats * 60 seg
        hopSize = hopSize_seg * fr

        for frame in FrameGenerator(audio, frameSize=1024 * 4, hopSize=int(hopSize), startFromZero=True):
            mfcc_bands, mfcc_coeffs = mfcc(spectrum(w(frame)))
            mfccs.append(mfcc_coeffs)
            melbands.append(mfcc_bands)
            melbands_log.append(logNorm(mfcc_bands))

        self.mfccs = pd.DataFrame(mfccs)
        self.melbands = pd.DataFrame(melbands)
        self.melbands_log = pd.DataFrame(melbands_log)

    def plot(self):
        # transpose to have it in a better shape
        mfccs = essentia.array(self.mfccs.values.tolist()).T
        melbands = essentia.array(self.melbands.values.tolist()).T
        melbands_log = essentia.array(self.melbands_log.values.tolist()).T

        # and plot
        imshow(melbands[:, :], aspect='auto', origin='lower', interpolation='none')
        plt.title("Mel band spectral energies in frames")
        show()

        imshow(melbands_log[:, :], aspect='auto', origin='lower', interpolation='none')
        plt.title("Log-normalized mel band spectral energies in frames")
        show()

        imshow(mfccs[1:, :], aspect='auto', origin='lower', interpolation='none')
        plt.title("MFCCs in frames")
        show()

    def export(self, folder_path):
        self.mfccs.to_json(Path(folder_path) / 'mfcc.json', orient='index')
        self.melbands.to_json(Path(folder_path) / 'melbands.json', orient='index')
        self.melbands_log.to_json(Path(folder_path) / 'melbands_log.json', orient='index')


#####################################################
####################### TEST ########################
#####################################################
# tfe = TrackMFCCExtractor('audio_files/EDM/Martin Garrix, Bonn - High On Life (Original Mix) [SWM].mp3')
# tfe.run()
# tfe.export('mfcc_database/mfcc_db_tracks')
# tfe.plot()
