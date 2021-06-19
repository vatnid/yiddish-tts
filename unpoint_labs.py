import os
import re

for filename in os.listdir("../Herbikher-unpointed/zilberberg"):
    if filename.endswith(".lab"):
        l = ""    
        with open(f"../Herbikher-unpointed/zilberberg/{filename}", "r") as f:
            for line in f:
                l = line

        l = re.sub(r"אַ", r"א", l)
        l = re.sub(r"אָ", r"א", l)
        l = re.sub(r"בּ", r"ב", l)
        l = re.sub(r"בֿ", r"ב", l)
        l = re.sub(r"וּ", r"ו", l)
        l = re.sub(r"יִ", r"י", l)
        l = re.sub(r"ײַ", r"ײ", l)
        l = re.sub(r"כּ", r"כ", l)
        l = re.sub(r"פּ", r"פ", l)
        l = re.sub(r"פֿ", r"פ", l)
        l = re.sub(r"שׂ", r"ש", l)
        l = re.sub(r"תּ", r"ת", l)

        with open(f"../Herbikher-unpointed/zilberberg/{filename}", "w") as f:
            f.write(l.strip())