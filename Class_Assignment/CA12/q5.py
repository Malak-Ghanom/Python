#The code below can generate several exceptions. 
# These are now handled by a single try ... except clause.
#  Extend this code by handling all exceptions that may occur explicitly 
# (there are at least three different kinds of exceptions that can be raised). 
# Note: Let me stress again that I rather have you avoid exceptions occurring than handling them,
#  but in this case I want you to practice with exception handling.


fruit_list = ["apple", "banana", "cherry"]

try:
	num = input( "Please enter a number: " ) 
if "." in num:
	num = float(num)
else:
	num = int(num) print( fruit_list[num] )
except:
	print( "Something went wrong." )
