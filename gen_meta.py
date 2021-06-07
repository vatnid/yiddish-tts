import sys

infile = sys.argv[1]

output = []

i = 1
with open(infile, "r") as f:
    for line in f:
        output.append(f"{i}|{line.strip()}")
        i += 1

with open(f"{infile[:-4]}_metaaa.txt", "w") as f:
    for line in output:
        f.write(f"{line}\n")