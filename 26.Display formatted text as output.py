# Display formatted text as output

import textwrap
sample_text = '''
  Python is a widely used high-level,general-purpose,
  interpreted, dynamic programming language. Its desgin
  philosophy emphasizes code readability, and its synatx
  allows programmers to express concepts in fewer lines
  of code thsn possible in language such as C++ of Java.
  '''
print()
print(textwrap.fill(sample_text, width=50))
print()
  
