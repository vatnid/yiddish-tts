import os
from depoint import depoint

for filename in os.listdir("../Sara-unpointed/blacher-retter"):
    if filename.endswith(".lab"):
        l = ""    
        with open(f"../Sara-unpointed/blacher-retter/{filename}", "r") as f:
            for line in f:
                l = line

        l = depoint(l)

        with open(f"../Sara-unpointed/blacher-retter/{filename}", "w") as f:
            f.write(l.strip())