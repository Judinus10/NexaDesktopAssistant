import pocketsphinx 
from pocketsphinx import LiveSpeech

# Create a LiveSpeech instance with the desired language model
speech = LiveSpeech(lm=False, keyphrase='Nexa', kws_threshold=1e-20)

for phrase in speech:
    print("Hotword detected: ", phrase)
