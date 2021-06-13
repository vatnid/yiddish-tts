from enum import unique
import sys
import re

infile = sys.argv[1]

alphabet = "אאַאָבבּבֿגדהווּװױזחטייִײַכּכךלמםנןסעפּפֿףצץקרששׂתּתאַאָבּבֿוּיִױכּפפֿשׂתּ"

unique_words = set()

def normalise_unicode(text):
    text = text.strip()
    text = re.sub(r"אַ", r"אַ", text)
    text = re.sub(r"אָ", r"אָ", text)
    text = re.sub(r"בּ", r"בּ", text)
    text = re.sub(r"בֿ", r"בֿ", text)
    text = re.sub(r"וּ", r"וּ", text)
    text = re.sub(r"יִ", r"יִ", text)
    text = re.sub(r"ײַ", r"ײַ", text)
    text = re.sub(r"כּ", r"כּ", text)
    text = re.sub(r"פּ", r"פּ", text)
    text = re.sub(r"פֿ", r"פֿ", text)
    text = re.sub(r"שׂ", r"שׂ", text)
    text = re.sub(r"תּ", r"תּ", text)
    text = re.sub(r"יי", r"ײ", text)
    text = re.sub(r"וו", r"װ", text)
    text = re.sub(r"וי", r"ױ", text)
    return text.strip()

with open(infile, "r") as f:
    for line in f:
        line = line.split("|")[1]
        line = normalise_unicode(line)
        line = re.sub(r"[^ אאַאָבבּבֿגדהווּװױזחטייִײַכּכךלמםנןסעפּפֿףצץקרששׂתּתאַאָבּבֿוּיִױכּפפֿשׂתּ]", r"", line)
        for word in line.split():
            unique_words.add(word)

with open(f"lexicon.txt", "w") as f:
    for i, word in enumerate(sorted(unique_words)):
        if i != 0:
            f.write("\n")
        f.write(f"{word}\t{' '.join(word)}")