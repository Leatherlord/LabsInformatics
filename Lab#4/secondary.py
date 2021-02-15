import json
import yaml

f = open("dataIn.json", "r", encoding="utf-8")
jsonData = f.read()
f.close()
pyDict = json.loads(jsonData)
yamlData = yaml.dump(pyDict, allow_unicode=True)
f = open("dataOut.yaml", "w", encoding="utf-8")
f.write(yamlData)
f.close()
