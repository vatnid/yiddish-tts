from enum import unique
import sys
import re

infile = sys.argv[1]

unique_words = set()

def normalise_unicode(text):
    text = re.sub(r"אַ", r"אַ", text)
    text = re.sub(r"אָ", r"אָ", text)
    text = re.sub(r"בּ", r"בּ", text)
    text = re.sub(r"בֿ", r"בֿ", text)
    text = re.sub(r"פּ", r"פּ", text)
    text = re.sub(r"פֿ", r"פֿ", text)
    text = re.sub(r"וּ", r"וּ", text)
    text = re.sub(r"יִ", r"יִ", text)
    text = re.sub(r"ײַ", r"ײַ", text)
    text = re.sub(r"כּ", r"כּ", text)
    text = re.sub(r"שׂ", r"שׂ", text)
    text = re.sub(r"תּ", r"תּ", text)
    text = re.sub(r"-", r"־", text)
    return text

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
    return text

with open(infile, "r") as f:
    for line in f:
        l = normalise_unicode(line)
        l = depoint(l)
        unique_words.add(l.strip())

with open(f"lexicon-phone-oovs2.txt", "w") as f:
    for i, word in enumerate(sorted(unique_words)):
        if i != 0:
            f.write("\n")
        f.write(f"{word}\t{' '.join(word)}")