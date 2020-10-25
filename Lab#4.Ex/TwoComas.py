import re

twoComasSentence = r"[A-Z0-9][^,?!.]*,[^,?!.]*,[^?!.]*[.?!]"
f = open("Macbeth.txt", "r")
s = f.read()
f.close
f = open("MacOut.txt", "w")
found = re.findall(twoComasSentence, s)
for i in range(1, len(found)):
    f.write(str(i) + ": " + str(found[i]) + "\n\n")
f.close()
