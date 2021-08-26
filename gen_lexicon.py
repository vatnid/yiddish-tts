from enum import unique
import sys
import re
from normalise_unicode import normalise_unicode

alphabet = "־׳״אאַאָבבּבֿגדהווּײװױזחטייִײַכּכךלמםנןסעפּפֿפףצץקרששׂתּת"

unique_words = set()

for filename in os.listdir("segmented"):
    if filename.endswith(".lab"):
        l = normalise_unicode(line)
        l = re.sub(r"[^ ־׳״אאַאָבבּבֿגדהווּײװױזחטייִײַכּכךלמםנןסעפּפֿפףצץקרששׂתּת]", r"", l)
        for word in l.split():
            unique_words.add(word)

with open(f"lexicon.txt", "w") as f:
    for i, word in enumerate(sorted(unique_words)):
        if i != 0:
            f.write("\n")
        f.write(f"{word}\t{' '.join(word)}")