# plot the lengths of the audios

import sys
import librosa
import matplotlib.pyplot as plt

infile = sys.argv[1]

lengths = []

with open(infile, "r") as f:
    for line in f:
        name = line.split("|")[0]
        lengths.append(librosa.get_duration(filename = f"Herbikher/wavs/{name}.wav"))

lengths.sort()
print(lengths)

plt.hist(lengths, density=False)
plt.ylabel("Length")
plt.xlabel("Data")
plt.show()