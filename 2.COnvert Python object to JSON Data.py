# Python JSON
# COnvert Python object to JSON Data

import json
# a Python object(dict):
python_obj = {
    "name":"David",
    "class":"I",
    "age": 6
}
print(type(python_obj))
#convert into JSON
j_data = json.dumps(python_obj)

#result is a JSON String
print(j_data)

