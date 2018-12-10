# from audio_meters import AudioMeters
#
# meter = AudioMeters.get_loudness('audio_files/ADW.mp3')
#
# print(meter)


from batch_reader import BatchReader

# EDM
# reader = BatchReader('audio_files/edm')
# reader.run()
# reader.export('output/edm')
# print(reader.average_tp)
# print(reader.average_lufs)
# print(reader.tp_database)

# # ROCK
# reader = BatchReader('audio_files/rock')
# reader.run()
# reader.export('output/rock')
# print(reader.average_tp)
# print(reader.average_lufs)


# Test adding database functions

# reader2 = BatchReader('audio_files/edm')
# reader2.add_existing_lufs_database('output/edm', 'lufs.json')
# reader2.add_existing_tp_database('output/edm', 'tp.json')
# a1 = reader2.calculate_avg_lufs()
# a2 = reader2.calculate_avg_tp()


# print(reader2.lufs_database)
# print(reader2.tp_database)
# print(reader2.average_tp)
# print(reader2.average_lufs)


# reader3 = BatchReader('audio_files/rock')
# reader3.run()
# reader3.export('output/rock')
# print(reader3.average_lufs)
# print(reader3.average_tp)

# reader4 = BatchReader('audio_files/rock')
# reader4.add_existing_lufs_database('output/edm', 'lufs.json')
# reader4.add_existing_tp_database('output/edm', 'tp.json')
#
# reader4.run()
# reader4.export('output/mix')
#
# print(reader4.tp_database)
