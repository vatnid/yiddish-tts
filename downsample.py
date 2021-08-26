import os
import librosa
import soundfile as sf


# hard-coded variables
RATE = 22050 # HiFi-GAN takes 22050
in_dir = "../Herbikher/zilberberg" # please change
out_dir = "../Herbikher22050/zilberberg" # please change


# converts .wav files in a folder and downsamples to RATE
for filename in os.listdir(in_dir):
	if filename.endswith(".wav"):
		y, s = librosa.load(f"Herbikher2/wavs_41/{filename}", sr = RATE)
		sf.write(f"{out_dir}/{filename}", y, s)