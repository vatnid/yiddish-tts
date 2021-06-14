import os
import re

for filename in os.listdir("../Herbikher/zilberberg"):
    if filename.endswith(".lab"):
        l = ""    
        with open(f"../Herbikher/zilberberg/{filename}", "r") as f:
            for line in f:
                l = line

        l = re.sub(r"אַ", r"אַ", l)
        l = re.sub(r"אָ", r"אָ", l)
        l = re.sub(r"בּ", r"בּ", l)
        l = re.sub(r"בֿ", r"בֿ", l)
        l = re.sub(r"וּ", r"וּ", l)
        l = re.sub(r"יִ", r"יִ", l)
        l = re.sub(r"ײַ", r"ײַ", l)
        l = re.sub(r"כּ", r"כּ", l)
        l = re.sub(r"פּ", r"פּ", l)
        l = re.sub(r"פֿ", r"פֿ", l)
        l = re.sub(r"שׂ", r"שׂ", l)
        l = re.sub(r"תּ", r"תּ", l)
        l = re.sub(r"יי", r"ײ", l)
        l = re.sub(r"וו", r"װ", l)
        l = re.sub(r"וי", r"ױ", l)
        l = re.sub(r"[\"„—\']", r"", l)
        l = re.sub(r"([()!,.:;?])", r"\1 ", l)
        l = re.sub(r"\s+", r" ", l)

        with open(f"../Herbikher/zilberberg/{filename}", "w") as f:
            f.write(l.strip())