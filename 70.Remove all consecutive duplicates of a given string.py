#70.Remove all consecutive duplicates of a given string

from itertools import groupby
def remove_all_consecutive(str1):
    result_str = []
    for (key,group) in groupby(str1):
        result_str.append(key)

    return ''.join(result_str)

str1 = 'xxxxxyyyyy'
print("original string:" + str1)
print("after removing consecutive duplicates: " + str1)
print(remove_all_consecutive(str1))
