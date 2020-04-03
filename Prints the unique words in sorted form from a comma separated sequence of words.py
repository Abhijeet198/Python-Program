# Prints the unique words
#in sorted form from a comma separated sequence of words



item = input("Iput Comma Separated sequece of words")
words = [word for word in item.split(",")]
print(",".join(sorted(list(set(words)))))

