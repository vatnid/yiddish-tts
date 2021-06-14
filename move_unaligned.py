import os

with open(f"unaligned.txt", "r") as f:
    for name in f:
        name = name.strip()
        print(name)
        os.system(f"mv ../Herbikher/zilberberg/{name}.wav Herbikher2/unaligned/{name}.wav")
        os.system(f"mv ../Herbikher/zilberberg/{name}.lab Herbikher2/unaligned/{name}.lab")
