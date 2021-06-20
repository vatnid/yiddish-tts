import sys
import re

multiword = re.compile(r"^([\w־]+ )+[\w־]+\t([\w־]+ )+[\w־]+$")

bracketed = re.compile(r"\(.+\)")

def normalise_unicode(text):
    text = re.sub(r"אַ", r"אַ", text)
    text = re.sub(r"אָ", r"אָ", text)
    text = re.sub(r"בּ", r"בּ", text)
    text = re.sub(r"בֿ", r"בֿ", text)
    text = re.sub(r"פּ", r"פּ", text)
    text = re.sub(r"פֿ", r"פֿ", text)
    text = re.sub(r"וּ", r"וּ", text)
    text = re.sub(r"יִ", r"יִ", text)
    text = re.sub(r"ײַ", r"ײַ", text)
    text = re.sub(r"כּ", r"כּ", text)
    text = re.sub(r"שׂ", r"שׂ", text)
    text = re.sub(r"תּ", r"תּ", text)
    text = re.sub(r"-", r"־", text)
    return text

def depoint(text):
    text = re.sub(r"[אַאָ]", r"א", text)
    text = re.sub(r"[בּבֿ]", r"ב", text)
    text = re.sub(r"[פּפֿ]", r"פ", text)
    text = re.sub(r"כּ", r"כ", text)
    text = re.sub(r"שׂ", r"ש", text)
    text = re.sub(r"תּ", r"ת", text)
    text = re.sub(r"וּ", r"ו", text)
    text = re.sub(r"יִ", r"י", text)
    text = re.sub(r"ײַ", r"יי", text)
    text = re.sub(r"ײ", r"יי", text)
    text = re.sub(r"װ", r"וו", text)
    text = re.sub(r"ױ", r"וי", text)
    text = re.sub(r"ִ", r"", text)
    text = re.sub(r"ַ", r"", text)
    text = re.sub(r"ָ", r"", text)
    text = re.sub(r"ּ", r"", text)
    text = re.sub(r"ֿ", r"", text)
    text = re.sub(r"ׂ", r"", text)
    return text

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