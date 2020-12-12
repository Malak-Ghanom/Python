#Create a function compare_length(s1, s2) which returns the difference in length between the strings.


def compare_length(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    return abs(len1-len2)

string1 = 'hello'
string2 = 'malak Ghanom'

print(f"the difference in length between the strings is: {compare_length(string1,string2)}")