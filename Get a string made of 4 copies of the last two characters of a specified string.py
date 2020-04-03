# Get a string made of 4 copies of the last two characters
# of a specified string



def insert_end(str):
    sub_str = str[-2:]
    return sub_str *4

print(insert_end('Python'))
print(insert_ed('Exercise'))
