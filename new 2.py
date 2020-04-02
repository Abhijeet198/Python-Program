# Python Json
# Convert JSON data to python object

import json
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\n Name: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"]) 
