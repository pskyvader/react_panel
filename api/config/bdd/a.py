import json
import os
file_str='bdd.json'

with open(file_str,'r') as file1:
    tables=json.loads(file1)
    for t in tables:
        with open(t['tablename']+'.json','w') as table:
            table.write(json.dumps(t))