import re

time = r"(([0-1][0-9])|(2[0-3]))\:(([0-5][0-9]\:[0-5][0-9][^:]??)|([0-5][0-9][^:]??))"
f = open("dataIn.txt", "r")
s = f.readlines()
for i in range(len(s)):
    s[i] = re.sub(time, "(TBD)", s[i])
f.close()
f = open("dataOut.txt", "w")
for i in s:
    f.write(i)
f.close()
