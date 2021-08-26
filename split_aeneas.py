# split recordings according to timestamps from aeneas

import json
import sys
from scipy.io import wavfile

# hard-coded variables
injson = "xxx.json" # path for input .json file
inwav = "yyy.wav" # path for .wav you want to split
out_dir = "zzz"


sents = [] # format: (start_time, end_time, line)

# loads .json output from aeneas
with open(injson) as f:
    data = json.load(f)
for i in data["fragments"]:
    sents.append((float(i["begin"]), float(i["end"]), i["lines"]))

# loads .wav file
rate, data = wavfile.read(inwav)

# split audio
for i in range(len(sents)):
    print(sents[i])
    begin_frame = int(rate * sents[i][0])
    end_frame = int(rate * sents[i][1])
    target_data = data[begin_frame:end_frame]
    wavfile.write(f"{out_dir}/{i+1}.wav", rate, target_data)