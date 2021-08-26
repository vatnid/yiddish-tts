import sys
import time
from random import sample

lines = []

with open("dershlisl_trimmed.txt", "r") as f:
    for line in f:
    	lines.append(line.strip())

sample = sample(lines, 40)

with open(f"dershlisl_test_{int(time.time())}.txt", "w") as f:
	for i, line in enumerate(sample):
		f.write(line)
		if i != len(sample)-1:
			f.write("\n")