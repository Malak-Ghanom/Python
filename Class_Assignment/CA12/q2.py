#Adapt the code above to count how often the word Flatland 
# (with any capitalization) occurs in the first 5 lines.
#  Print only the number of occurrences of that word.
#  Once it works, remove the count so that you count the number
#  of occurrences of the word in the text as a whole.

my_file = open ('D:\\python\\CA12\\flatland.txt','r')
count = 0

for line in my_file:
    line_list = list(line.lower().split())
    if 'flatland' in line.lower() :
        count += 1

my_file.close()        
print(count)
