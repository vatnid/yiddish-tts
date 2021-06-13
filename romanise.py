import sys
import re

infile = sys.argv[1]

input = []
output = []

rom_old = {"א": "a",
       "אַ": "a", "אָ": "o",
       "ב": "b", "בּ": "b",
       "בֿ": "v",
       "ג": "g",
       "ד": "d",
       "ה": "h",
       "ו": "u", "וּ": "u",
       "װ": "v",
       "ױ": "oy",
       "ז": "z",
       "ח": "kh",
       "ט": "t",
       "י": "i", "יִ": "i",
       "ײ": "ey",
       "ײַ": "ay",
       "כּ": "k",
       "כ": "kh", "ך": "kh",
       "ל": "l",
       "מ": "m", "ם": "m",
       "נ": "n", "ן": "n",
       "ס": "s",
       "ע": "e",
       "פּ": "p",
       "פֿ": "f", "פ": "f", "ף": "f",
       "צ": "c", "ץ": "c",
       "ק": "k",
       "ר": "r",
       "ש": "sh",
       "שׂ": "s",
       "תּ": "t",
       "ת": "s"
       }

rom = {"א": "",
       "אַ": "a", "אָ": "o",
       "ב": "b", "בּ": "b",
       "בֿ": "w",
       "ג": "g",
       "ד": "d",
       "ה": "h",
       "ו": "u", "וּ": "u",
       "װ": "w",
       "ױ": "eu",
       "ז": "s",
       "ח": "ch",
       "ט": "t",
       "י": "i", "יִ": "i",
       "ײ": "ei",
       "ײַ": "ei",
       "כּ": "k",
       "כ": "ch", "ך": "ch",
       "ל": "l",
       "מ": "m", "ם": "m",
       "נ": "n", "ן": "n",
       "ס": "ss",
       "ע": "e",
       "פּ": "p",
       "פֿ": "f", "פ": "f", "ף": "f",
       "צ": "z", "ץ": "z",
       "ק": "k",
       "ר": "r",
       "ש": "sch",
       "שׂ": "ss",
       "תּ": "t",
       "ת": "ss"
       }

# preprocessing
with open(infile, "r") as f:
    for line in f:
        line = line.strip()
        line = re.sub(r"אַ", r"אַ", line)
        line = re.sub(r"אָ", r"אָ", line)
        line = re.sub(r"בּ", r"בּ", line)
        line = re.sub(r"בֿ", r"בֿ", line)
        line = re.sub(r"וּ", r"וּ", line)
        line = re.sub(r"יִ", r"יִ", line)
        line = re.sub(r"ײַ", r"ײַ", line)
        line = re.sub(r"כּ", r"כּ", line)
        line = re.sub(r"פּ", r"פּ", line)
        line = re.sub(r"פֿ", r"פֿ", line)
        line = re.sub(r"שׂ", r"שׂ", line)
        line = re.sub(r"תּ", r"תּ", line)
        line = re.sub(r"יי", r"ײ", line)
        line = re.sub(r"וו", r"װ", line)
        line = re.sub(r"וי", r"ױ", line)
        input.append(line)

for line in input:
    temp = ""
    for c in line:
        if c in rom.keys():
            temp += rom[c]
        else:
            temp += c
    #temp = re.sub(r"\'", r"", temp)
    #temp = re.sub(r"[^a-zA-Z0-9]", r" ", temp)
    temp = re.sub(r"\s+", r" ", temp)
    temp = re.sub(r"schp", r"sp", temp)
    temp = re.sub(r"scht([aeiour])", r"st\1", temp)
    temp = re.sub(r"\bpun\b", r"fun", temp)
    temp = re.sub(r"eup", r"euf", temp)
    output.append(temp.strip())

with open(f"{infile[:-4]}_rom.txt", "w") as f:
    for i, line in enumerate(output):
        if i == 0:
            f.write(f"{line}")
        else:
            f.write(f"\n{line}\n")