import re

twoComasSentence = r"[A-Z0-9А-Я][^,?!.]*,[^,?!.]*,[^.]*?[\"]?[!?.]{1,3}"
f = open("Macbeth.txt", "r")
s = f.read()
f = open("MacOut.txt", "w")
found = re.findall(twoComasSentence, s)
for i in enumerate(found):
    f.write(str(i+1) + ": " + str(found[i]) + "\n\n")
