#Create a function last_two(astring) which returns the last two characters as a tuple. 
# If there are less than two characters, return the value "Error".

def last_two(astring):
    str_len = len(astring)
    if str_len < 2:
        return 'Error'
    else:
        return astring[str_len-2], astring[str_len-1]


my_string = 'malak'

print(f"the last two characters as a tuple is: {last_two(my_string)}")