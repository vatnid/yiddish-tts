# FastSpeech 2 output files are named after the exact utterance
# this renames them according to the transcript file

import os
import re
from pprint import pprint

voices = ["baseline", "unpointed", "phone"]

for voice in voices:
    print(f"voice: {voice}")
    path = f"../FastSpeech2/output/result/zilberberg-{voice}"

    print(os.listdir(f"{path}"))

    for filename in os.listdir(f"{path}"):
        if filename.endswith(".wav"):
            print(f"filename: {filename}")
            if filename == ".wav":
                continue
            name = filename[:-4]
            name = name[:max(15, len(name))]
            sents = {}
            with open(f"test/gold-labs/zilberberg/{voice}.tsv", "r") as f:
                for line in f:
                    l = line.strip()
                    sents[l.split("\t")[1][:max(15, len(name))]] = l.split("\t")[0]

            filename = re.sub(r" ", r"\ ", filename)
            os.system(f"mv {path}/{filename} {path}/{sents[name]}.wav")


"""
for filename in os.listdir("test/zilberberg-baseline"):
    if filename.endswith(".wav"):
        name = filename[:-4]
        name = name[:max(15, len(name))]
        zil_baseline = {}
        with open(f"test/zilberberg-master.tsv", "r") as f:
            for line in f:
                l = line.strip()
                zil_baseline[l.split("\t")[1][:max(15, len(name))]] = l.split("\t")[0]

        filename = re.sub(r" ", r"\ ", filename)
        os.system(f"mv test/zilberberg-baseline/{filename} test/zilberberg-baseline/{zil_baseline[name]}-baseline.wav")


for filename in os.listdir("test/sara-baseline"):
    if filename.endswith(".wav"):
        name = filename[:-4]
        name = name[:max(15, len(name))]
        sara_baseline = {}
        with open(f"test/sara-master.tsv", "r") as f:
            for line in f:
                l = line.strip()
                sara_baseline[l.split("\t")[1][:max(15, len(name))]] = l.split("\t")[0]

        filename = re.sub(r" ", r"\ ", filename)
        os.system(f"mv test/sara-baseline/{filename} test/sara-baseline/{sara_baseline[name]}-baseline.wav")
"""