import os
import librosa
import soundfile as sf

for filename in os.listdir("../Herbikher/zilberberg"):
	if filename.endswith(".wav"):
		y, s = librosa.load(f"Herbikher2/wavs_41/{filename}", sr=22050)
		sf.write(f"../Herbikher2205/zilberberg/{filename}", y, s)