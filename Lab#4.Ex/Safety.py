import re

number = r"\d+"
notNumber = r"\D+"
f = open("Unsafe.txt", "r", encoding='utf-8')
s = f.read()
f.close()
f = open("Safe.txt", "w", encoding='utf-8')
found = re.findall(number, s)
notFound = re.findall(notNumber, s)
for i in range (len(found)):
    found[i] = int(found[i])**2*3+5
if len(found) < len(notFound):
    found.append("")
elif len(notFound) < len(found):
    notFound.append("")
for i in range(len(found)):
    try:
        if int(s[0]):
            f.write(str(found[i]) + notFound[i])
    except ValueError:
        f.write(notFound[i] + str(found[i]))
f.close()
