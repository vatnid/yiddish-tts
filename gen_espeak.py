# generate espeak voices

import os

# hard-coded variables
in_dir = "test/gold-labs/zilberberg/master-espeak"
out_dir = "test/gold-labs/zilberberg/espeak-output"

for filename in os.listdir(in_dir):
    if filename.endswith(".lab"):
        print(f"Processing {filename}")
        name = filename[:-4] # remove ".lab" for output
        with open(f"{in_dir}/{filename}", "r") as f:
            utt = ""
            for line in f:
                utt = line.strip()
                print(f"Utterance: {utt}")
            # use "-v de" for male voice and "-v de+13" for female 
            os.system(f"espeak -v de -w {out_dir}/{name}.wav '{utt}'")