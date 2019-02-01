from bpm_analyzer import bpm_analyzer

# b = bpm_analyzer('../audio_files/BassHouse')
#
# b.get_bpm_batch()
# b.export('../genres_database')


b = bpm_analyzer('../audio_files/Uptempo')

b.add_existing_database('../genres_database/', 'database_bpm_310119.json')
b.get_bpm_batch()
b.export('../genres_database')
