# from audio_meters import AudioMeters
#
# meter = AudioMeters.get_loudness('audio_files/ADW.mp3')
#
# print(meter)


from batch_reader import BatchReader

# EDM
reader = BatchReader('../audio_files/edm_t')
reader.run()
reader.export('../genres_database/database.json')
# reader.export('output/edm')
# print(reader.average_tp)
# print(reader.average_lufs)
# print(reader.tp_database)
