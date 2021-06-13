import sys
import librosa
import soundfile as sf

path = sys.argv[1]
shorts = []
longs = []

with open(f"{path}/shorts.txt", "r") as f:
	for line in f:
		shorts.append(line.strip())

with open(f"{path}/longs.txt", "r") as f:
	for line in f:
		longs.append(line.strip())


with open(f"{path}/transcript.csv", "r") as f:
    for line in f:
    	name = line.split("|")[0]
    	if name not in shorts and name not in longs:
	    	y, s = librosa.load(f"{path}/wavs/{name}.wav", sr=16000)
	    	y = librosa.to_mono(y)
	    	sf.write(f"{path}/wavs_16/{name}.wav", y, 16000)
