#55. Find the second most repeated word in a given string

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] +=1
        else:
           counts[word] = 1

    counts_x = sorted(counts.items(),key = lamba kv: kv[1])
    #print(counts_x)
    return counts_x[-2]

print(word_count("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expression in annotations at their definition time, the comiler stores the annotation in a string form equivalent to the AST of the expression in questio. If needed, annotations can be resloved at runtime using typing.get_type_hints().In the common case where this is notrequired, the annotations are cheaper to store(since short strings are interned by the interpreter) and make startup time faster."))
