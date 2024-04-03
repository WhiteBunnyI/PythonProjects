import json
import sys

args = sys.argv
if len(args) <= 1:
    print("No argument")
    exit()
with open(args[1], mode='r') as file:
    json_data = json.load(file)

for i in json_data:
    with open(i+'.csv', mode='w') as file:
        columns = list(json_data[i][0].keys())
        header = ''
        for o in columns:
            header += o+','
        header = header[:-1]+'\n'

        file.write(header)
        for o in json_data[i]:
            data = ''
            for p in o:
                data += str(o[p])+','
            data = data[:-1]
            file.write(data+'\n')



