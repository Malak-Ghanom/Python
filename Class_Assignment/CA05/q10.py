#Create a function which take a string as an argument, 
# then prints a string where for every character in the original there are three characters.

def repeat(astring):
    rstring=''
    for i in astring:
        rstring = rstring+i*3
    return rstring

my_string = 'malak'    
print(f"the new string is: {repeat(my_string)}")