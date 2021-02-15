import ast

f = open("dataIn.json", "r", encoding="utf-8")
jsonData = f.read()
null = None
true = True
false = False
d = ast.literal_eval(jsonData)
f.close()
f = open("dataOut.yaml", "w", encoding="utf-8")
for key in d.keys():
    f.write(key + ":\n")
    for insKey in d[key]:
        if list(insKey.values())[0] is True:
            f.write("- " + list(insKey.keys())[0] + ": " + "true" + '\n')
        elif list(insKey.values())[0] is False:
            f.write("- " + list(insKey.keys())[0] + ": " + "false" + '\n')
        elif list(insKey.values())[0] is None:
            f.write("- " + list(insKey.keys())[0] + ": " + "null" + '\n')
        else:
            f.write("- " + list(insKey.keys())[0] + ": " + list(insKey.values())[0] + '\n')
f.close()
