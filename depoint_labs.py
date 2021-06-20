import os
import re

def depoint(text):
    text = re.sub(r"[אַאָ]", r"א", text)
    text = re.sub(r"[בּבֿ]", r"ב", text)
    text = re.sub(r"[פּפֿ]", r"פ", text)
    text = re.sub(r"כּ", r"כ", text)
    text = re.sub(r"שׂ", r"ש", text)
    text = re.sub(r"תּ", r"ת", text)
    text = re.sub(r"וּ", r"ו", text)
    text = re.sub(r"יִ", r"י", text)
    text = re.sub(r"ײַ", r"יי", text)
    text = re.sub(r"ײ", r"יי", text)
    text = re.sub(r"װ", r"וו", text)
    text = re.sub(r"ױ", r"וי", text)
    text = re.sub(r"ִ", r"", text)
    text = re.sub(r"ַ", r"", text)
    text = re.sub(r"ָ", r"", text)
    text = re.sub(r"ּ", r"", text)
    text = re.sub(r"ֿ", r"", text)
    text = re.sub(r"ׂ", r"", text)
    text = re.sub(r"-", r"־", text)
    return text

for filename in os.listdir("../Herbikher-unpointed/zilberberg"):
    if filename.endswith(".lab"):
        l = ""    
        with open(f"../Herbikher-unpointed/zilberberg/{filename}", "r") as f:
            for line in f:
                l = line

        l = depoint(l)

        with open(f"../Herbikher-unpointed/zilberberg/{filename}", "w") as f:
            f.write(l.strip())