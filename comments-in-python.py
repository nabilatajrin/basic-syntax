#A hash sign (#) that is not inside a string literal is the beginning of a comment. All characters after the #,
# up to the end of the physical line, are part of the comment and the Python interpreter ignores them.

#!/usr/bin/python3

# First comment
print ("Hello, Python!") # second comment

#This produces the following result − Hello, Python!


#You can type a comment on the same line after a statement or expression −

name = "Madisetti" # This is again comment

#You can comment multiple lines as follows −

# This is a comment.
# This is a comment, too.
# This is a comment, too.
# I said that already.

#Following triple-quoted string is also ignored by Python interpreter and can be used as a multiline comments:

'''
This is a multiline
comment.
'''