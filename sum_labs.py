import os

sents = {}

for filename in os.listdir("../Herbikher/zilberberg"):
    if filename.endswith(".lab"):
        with open(f"../Herbikher/zilberberg/{filename}", "r") as f:
            for line in f:
                sents[filename[:-4]] = line.strip()
                print(f"{filename[:-4]}|{sents[filename[:-4]]}")

        
with open(f"all_labs.txt", "w") as f:
    for i, k in enumerate(sents):
        f.write(f"{sents[k]}")
        if i != 0:
            f.write("\n")