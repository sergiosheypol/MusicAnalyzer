from bpm_analyzer import BPMAnalyzer

# b = bpm_analyzer('../audio_files/BassHouse')
#
# b.get_bpm_batch()
# b.export('../genres_database')


b = BPMAnalyzer('test_tracks')

# b.add_existing_database('../genres_database/', 'database_bpm_310119.json')
print(b.get_bpm_single('asfos.mp3'))
# b.export('../genres_database')
