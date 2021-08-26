# limit length of recordings to between 1 and 10 seconds (or otherwise specified)

import sys
import os
import librosa


# hard-coded variables
min_dur = 1
max_dur = 10
path = sys.argv[1]


shorts = []
longs = []



with open(f"{path}/transcript.csv", "r") as f:
    for line in f:
        name = line.split("|")[0]
        length = librosa.get_duration(filename = f"{path}/wavs/{name}.wav")
        if length < min_dur:
            os.system(f"mv {path}/wavs/{name}.wav {path}/short/{name}.wav")
            os.system(f"mv {path}/wavs/{name}.lab {path}/short/{name}.lab")
            shorts.append(name)
        if length > max_dur:
            os.system(f"mv {path}/wavs/{name}.wav {path}/long/{name}.wav")
            os.system(f"mv {path}/wavs/{name}.lab {path}/long/{name}.lab")
            longs.append(name)

with open(f"{path}/shorts.txt", "w") as f:
    for i, name in enumerate(shorts):
        if i == 0:
            f.write(f"{name}")
        else:
            f.write(f"\n{name}")


with open(f"{path}/longs.txt", "w") as f:
    for i, name in enumerate(longs):
        if i == 0:
            f.write(f"{name}")
        else:
            f.write(f"\n{name}")