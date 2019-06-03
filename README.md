# Music Analyzer 
## Supported features

* LUFS, dBTP and BPM reading
* Genre classification based on  LUFS, dBTP and BPM with kNN and SVC algorithms
* MFCC extraction for single instrument files (either MP3 or WAV)
* Average MFCC extraction for full tracks (either MP3 or WAV)

## How to install

This project has been build upon an Conda3/Anaconda3 environment. Simply import the environment with 
`conda env create -f MusicAnalyzerEnvironment.yml`

### Some of the libraries in the environment
* Essentia
* NumPy
* Pandas
* Scikit-Learn

## System requirements
* Conda3/Anaconda3 
* FFMPEG


## Final consideration
This system has been tested on Linux Ubuntu 18.10