# Python JSON
# Check whether a JSON string contains complex object or not


import json
def is_complex_num(objct):
    if '_complx_' in objct:
        return complex(objct['real'], objct['img'])
    return objct

complex_object = json.loads('{"_complex_": true, "real": 4, "img": 5}', object_hook = is_complex_num)
simple_object = json.loads('{"real": 4, "img": 3}',object_hook = is_complex_num)
print("Complex_object:",complex_object)
print("Without complex object: ", simple_object)
  