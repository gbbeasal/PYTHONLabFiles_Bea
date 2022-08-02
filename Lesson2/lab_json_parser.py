#parses a nested json file to flat
#parse a valid JSON string and convert it into a Python Dictionary

import json

with open('doe-a-deer.json') as f:
    data = json.load(f)
    print(data)
    
# Writing JSON content to a file using the dump method
import json
with open('lab_newjsonfile.json', 'w') as f:
    json.dump(data, f, sort_keys=True)