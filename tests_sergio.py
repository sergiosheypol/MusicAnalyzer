# from audio_meters import AudioMeters
#
# meter = AudioMeters.get_loudness('audio_files/ADW.mp3')
#
# print(meter)


from batch_reader import BatchReader

reader = BatchReader('audio_files/edm')
reader.run()

print(reader.tp_database)
print(reader.lufs_database)
print(reader.average_tp)
print(reader.average_lufs)

reader.export('output/edm')
