import json
import sys
from scipy.io import wavfile

# (start_time, end_time, line)
sents = []

# loads .json output from aeneas
injson = sys.argv[1]
with open(injson) as f:
  data = json.load(f)
for i in data["fragments"]:
    sents.append((float(i["begin"]), float(i["end"]), i["lines"]))

# loads .wav file
inwav = sys.argv[2]
rate, data = wavfile.read(inwav)

exportdir = sys.argv[3]

# split audio
for i in range(len(sents)):
    print(sents[i])
    begin_frame = int(rate * sents[i][0])
    end_frame = int(rate * sents[i][1])
    target_data = data[begin_frame:end_frame]
    wavfile.write(f"{exportdir}/{i+1}.wav", rate, target_data)