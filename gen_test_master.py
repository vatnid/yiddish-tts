import os
import re
from depoint import depoint
from isaac_respelling import respell

zilberberg = {}
sara = {}

for filename in os.listdir("test/zilberberg"):
    if filename.endswith(".lab"):
        name = filename[:-4]
        with open(f"test/zilberberg/{filename}", "r") as f:
            for line in f:
                l = re.sub(r"-", r"־", line)
                l = re.sub(r"\. \. \.", r".", l)
                zilberberg[name] = l.strip()

for filename in os.listdir("test/sara"):
    if filename.endswith(".lab"):
        name = filename[:-4]
        with open(f"test/sara/{filename}", "r") as f:
            for line in f:
                l = re.sub(r"-", r"־", line)
                l = re.sub(r"\. \. \.", r".", l)
                sara[name] = l.strip()


with open(f"test/zilberberg-master.tsv", "w") as f:
    for k in zilberberg:
        f.write(f"{k}\t{zilberberg[k]}\n")

with open(f"test/sara-master.tsv", "w") as f:
    for k in sara:
        f.write(f"{k}\t{sara[k]}\n")

with open(f"test/zilberberg-master-unpointed.tsv", "w") as f:
    for k in zilberberg:
        f.write(f"{k}\t{depoint(zilberberg[k])}\n")

with open(f"test/sara-master-unpointed.tsv", "w") as f:
    for k in sara:
        f.write(f"{k}\t{depoint(sara[k])}\n")

with open(f"test/zilberberg-master-phone.tsv", "w") as f:
    for k in zilberberg:
        f.write(f"{k}\t{respell(zilberberg[k])}\n")

with open(f"test/sara-master-phone.tsv", "w") as f:
    for k in sara:
        f.write(f"{k}\t{respell(sara[k])}\n")