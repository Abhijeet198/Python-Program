# Get a string made of the first 2 and last 2 chars from a given a string


def string_both_ends(str):
    if len(str) < 2 :
      return ''

    return str[0:2] + str[-2:]
print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

