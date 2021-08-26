import sys
import re
from tools import *


multiword = re.compile(r"^([\w־]+ )+[\w־]+\t([\w־]+ )+[\w־]+$")
bracketed = re.compile(r"\(.+\)")

dictionary = []

with open(f"fonetisher.txt", "r") as f:
	for line in f:
		line = normalise_unicode(line)
		if len(line.split("\t")) != 2:
			continue
		hebrew = line.split("\t")[1]
		phonetic = line.split("\t")[0]
		if len(hebrew.split()) == len(phonetic.split()):
			for i, w in enumerate(hebrew.split()):
				if (w, phonetic.split()[i]) not in dictionary:
					dictionary.append((w, phonetic.split()[i]))
					#print(f"{w}\t{phonetic.split()[i]}")

cleaned = []

# remove brackets clean
for i, item in enumerate(dictionary):
	# if brackets enclose whole word

	if item[0][0] == "(" and item[0][-1] == ")" and item[1][0] == "(" and item[1][-1] == ")":
		print("bracketed:")
		print(item)
		cleaned.append((item[0][1:-1], item[1][1:-1]))
	# if both sides have brackets
	elif "(" in item[0] and ")" in item[0] and "(" in item[1] and ")" in item[1]:
		print("both bracketed:")
		print(item)
		h = re.sub(r"\(.+\)", r"", item[0])
		t = re.sub(r"\(.+\)", r"", item[1])
		h_brac = re.sub(r"[()]", r"", item[0])
		t_brac = re.sub(r"[()]", r"", item[1])
		cleaned.append((h, t))
		cleaned.append((h_brac, t_brac))
	# if only hebrew has brackets
	elif "(" in item[0] and ")" in item[0]:
		print("hebrew bracketed:")
		print(item)
		h = re.sub(r"\(.+\)", r"", item[0])
		t = item[1]
		h_brac = re.sub(r"[()]", r"", item[0])
		t_brac = item[1]
		cleaned.append((h, t))
		cleaned.append((h_brac, t_brac))
	# if only transcription has brackets
	elif "(" in item[1] and ")" in item[1]:
		print("transcription bracketed:")
		print(item)
		h = item[0]
		t = re.sub(r"\(.+\)", r"", item[1])
		h_brac = item[0]
		t_brac = re.sub(r"[()]", r"", item[1])
		cleaned.append((item[0], re.sub(r"[()]", r"", item[1])))
		cleaned.append((item[0], re.sub(r"\(.+\)", r"", item[1])))
	else:
		cleaned.append((item[0], item[1]))

cleaned.sort(key=lambda a: a[0])

with open(f"fonetisher_split.txt", "w") as f:
	for item in cleaned:
		h = re.sub(r"…", r"", item[0])
		t = re.sub(r"[…־]", r"", item[1])
		t = " ".join(t)
		f.write(f"{h}\t{t}\n")

with open(f"fonetisher_split_unpointed.txt", "w") as f:
	for item in cleaned:
		h = re.sub(r"…", r"", item[0])
		t = re.sub(r"[…־]", r"", item[1])
		h = depoint(h)
		t = depoint(t)
		t = " ".join(t)
		f.write(f"{h}\t{t}\n")