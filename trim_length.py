import sys

trimmed = []

with open("dershlisl_full.txt", "r") as f:
    for line in f:
    	wordnum = len(line.split())
    	if wordnum >= 5 and wordnum <= 15:
    		trimmed.append(line.strip())

with open("dershlisl_trimmed.txt", "w") as f:
	for i, line in enumerate(trimmed):
		f.write(line)
		if i != len(trimmed)-1:
			f.write("\n")