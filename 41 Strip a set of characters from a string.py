# 42.Strip a set of characters from a string

def strip_char(str, chars):
    return"".join(c for c in str if c not in chars)
print("\nOriginal String:")
print("The quick brown fox jumps over the lazy dog.")
print("After stripping a,e,i,o,u")
print(strip_chars("The quick brown for jumps over the lazy dog.","aeiou"))
print()
