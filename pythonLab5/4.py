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
        header = str(columns)[1:-1].replace("'", "")+'\n'
        file.write(header)

        for o in json_data[i]:
            data = str(list(o.values()))[1:-1].replace("'", "")+'\n'
            file.write(data)



