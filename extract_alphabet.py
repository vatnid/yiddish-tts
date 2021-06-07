import sys

infile = sys.argv[1]

charset = set(open(infile).read())
chars = "".join(charset)
print(chars)