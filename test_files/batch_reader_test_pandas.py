# from audio_meters import AudioMeters
#
# meter = AudioMeters.get_loudness('audio_files/ADW.mp3')
#
# print(meter)


from batch_reader import BatchReader

# EDM
reader = BatchReader('../audio_files/rock')

# reader.export('output/edm')
# print(reader.average_tp)
# print(reader.average_lufs)
# print(reader.tp_database)


# reader.run()
# reader.add_existing_lufs_database('../genres_database/edm_t')
# reader.add_existing_lufs_database('../genres_database/rock')
# print(reader.database)
# print(reader.avg_values)
# reader.calculate_average_values()
# print(reader.avg_values)
# reader.export('../genres_database/edm_t')