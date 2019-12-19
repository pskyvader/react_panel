import json
import os
folder=os.path.dirname(__file__)+'\\'
file_str=folder+'bdd.json'

with open(file_str,'r') as file1:
    tables=json.loads(file1.read())
    for t in tables:
        with open(folder+t['tablename']+'.json','w') as table:
            table.write(json.dumps(t))