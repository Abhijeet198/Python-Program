# Count the occurrences of each word in a given sentence

def word_count(str):
    couts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[words] +=1
        else:
            counts[words] = 1

     return count

print(word_count('the quick brown fox jumps over the lazy dog.'))
