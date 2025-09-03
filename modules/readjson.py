import json 

def read_json(fn, val):
    with open(fn, 'r') as f:
        a = json.load(f)
        b = a.get(val)
        return b