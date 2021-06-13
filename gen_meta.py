import sys

infile = sys.argv[1]
bookname = sys.argv[2]

output = []

with open(infile, "r") as f:
    for i, line in enumerate(f, 1):
        output.append(f"{bookname}-{i}|{line.strip()}|{line.strip()}")

with open(f"{bookname}_transcript.csv", "w") as f:
    for i, line in enumerate(output):
        if i == 0:
            f.write(f"{line}")
        else:
            f.write(f"\n{line}")