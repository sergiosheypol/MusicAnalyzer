# from audio_meters import AudioMeters
#
# meter = AudioMeters.get_loudness('audio_files/ADW.mp3')
#
# print(meter)


from batch_reader import BatchReader

# EDM
# reader = BatchReader('../audio_files/trap', 'trap')

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


# Adding TRAP
reader = BatchReader('../audio_files/Rock', 'Rock')
reader.add_existing_database('../genres_database', 'filtered_trap_no_130.json')
reader.run()
reader.export('../genres_database')
