#29.Add a prefix text to all of the lines in a string


import textwrap
sample_text = '''
 Python is a widely sued high-level,general-purpose,
 interpreted,dynamic programming language. Its
 desgin philosophy emphasizes concepts in fewer
 lines of code than possible in language such as
 C++ or Java.
 '''
text_without_Indentation  = textwrap.dedent(sample_text)
wrapped = textwrap.fill(text_without_Indentation,width=50)
#wrapped += '\n\nSecond pragraph after a blank line.'
final_result = textwrap.indent(wrapped,'>')
print()
print(final_result)
print()
