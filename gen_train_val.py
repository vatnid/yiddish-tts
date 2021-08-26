import os
import random

train = {}
validate = {}

for filename in os.listdir("../Sara/blacher-retter"):
    if filename.endswith(".lab"):
        with open(f"../Sara/blacher-retter/{filename}", "r") as f:
            for line in f:
                train[filename[:-4]] = line.strip()

for _ in range(len(train)//10):
    k = random.choice(list(train.keys()))
    validate[k] = train.pop(k)

print(train)
print(len(train))
print(validate)
print(len(validate))


with open(f"../Sara/training.txt", "w") as f:
    for k in train:
        f.write(f"{k}|{train[k]}|{train[k]}\n")

with open(f"../Sara/validation.txt", "w") as f:
    for k in validation:
        f.write(f"{k}|{validation[k]}|{validation[k]}\n")