import os
import random

raw = []
test = []

for filename in os.listdir("../Sara/blacher-retter"):
    if filename.endswith(".lab"):
        with open(f"../Sara/blacher-retter/{filename}", "r") as f:
            for line in f:
                raw.append(filename)

for _ in range(40):
    file = random.choice(raw)
    test.append(file[:-4])


with open(f"books/blacher-retter/TEST/sents.txt", "w") as f:
    for i in test:
        os.system(f"mv ../Sara/blacher-retter/{i}.wav books/blacher-retter/TEST/{i}.wav")
        os.system(f"mv ../Sara/blacher-retter/{i}.lab books/blacher-retter/TEST/{i}.lab")
        f.write(i)

print(test)
print(len(test))

