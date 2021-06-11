import sys

infile = sys.argv[1]

target = sys.argv[2]

with open(infile, "r") as f:
    for i, line in enumerate(f, 1):
        with open(f"{target}/{i}.lab", "w") as f:
            f.write(line.strip())