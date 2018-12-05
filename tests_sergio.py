from audio_meters import AudioMeters

meter = AudioMeters.get_loudness('audio_files/ADW.mp3')

print(meter)
