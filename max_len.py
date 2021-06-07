import sys

infile = sys.argv[1]

max_len = 0

with open(infile, "r") as f:
    for line in f:
        if len(line) > max_len:
            max_len = len(line)

print(max_len)