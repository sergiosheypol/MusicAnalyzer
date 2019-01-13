from emotions_analyzer import EmotionsDetector

ed = EmotionsDetector()

# print(ed.train('../emotions_audio_files/edm_t', '../emotions_models/edm_t', 'edm_t'))
# r = ed.get_emotions('../audio_files/edm/ov.mp3', '../emotions_models', 'edm_t')
# print(r)

# ed.train('../emotions_audio_files/speechEmotion', '../emotions_models', 'speech_emotions_test')
r = ed.get_emotions('../audio_files/edm/ADW.mp3', '../emotions_models', 'speech_emotions_test')
print(r)
