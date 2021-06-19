import os
import re


books = {"ashtetl": {}, "khayim": {}}
book = ""
number = 0

for filename in os.listdir("../Herbikher/zilberberg"):
    if filename.endswith(".lab"):
        if "ashtetl" in filename:
            book = "ashtetl"
        if "khayim" in filename:
            book = "khayim"
        number = filename[(len(book)+1):-4] # strip book name and file extension
        with open(f"../Herbikher/zilberberg/{filename}", "r") as f:
            text = ""
            for line in f:
                text += line
        books[book][number] = text

first = False
with open(f"combined_labs.txt", "w") as f:
    for book in books:
        for k in books[book]:
            sent = books[book][k]
            if not first:
                first = True
            else:
                f.write(f"\n")
            f.write(f"{book}-{k}|{sent}|{sent}")