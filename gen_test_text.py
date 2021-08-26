# generate different versions of texts for listening test generation

import os
from tools import *

parts = ["a", "b"]

for part in parts:
    for filename in os.listdir(f"test/gold-labs/zilberberg/{part}/unnormalised"):
        if filename.endswith(".lab"):
            with open(f"test/gold-labs/zilberberg/{part}/unnormalised/{filename}", "r") as f:
                l = ""
                for line in f:
                    l = line.strip()

                # normalised baseline
                with open(f"test/gold-labs/zilberberg/{part}/normalised/{filename}", "w") as f:
                    l = normalise_unicode(l)
                    f.write(l)

                # unpointed
                with open(f"test/gold-labs/zilberberg/{part}/unpointed/{filename}", "w") as f:
                    f.write(depoint(l))

                # respelt
                with open(f"test/gold-labs/zilberberg/{part}/respelt/{filename}", "w") as f:
                    f.write(respell(l))

                # romanised into German-like orthography, for eSpeak generation
                with open(f"test/gold-labs/zilberberg/{part}/romanised/{filename}", "w") as f:
                    f.write(romanise(l))