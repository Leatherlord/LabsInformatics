import re

number = r"\d+"
notNumber = r"\D+"
f = open("Unsafe.txt", "r")
s = f.read()
f.close()
f = open("Safe.txt", "w")
found = re.findall(number, s)
notFound = re.findall(notNumber, s)
for i in range (len(found)):
    found[i] = int(found[i])**2*3+5
print (len(found), len(notFound))
if len(found) < len(notFound):
    found.append("")
elif len(notFound) < len(found):
    notFound.append("")
print (notFound)
print (found)
print(s[0])
for i in range(len(found)):
    try:
        if int(s[0]):
            f.write(str(found[i]) + notFound[i])
    except ValueError:
        f.write(notFound[i] + str(found[i]))
f.close()
