# Ask the user for two lowercase words (w1, w2) as input. Create a function called create_anagram(w1, w2).
# The only allowed operation is to remove a character from any string. 
# Find minimum number of characters to be deleted to make both the strings anagram?

# Input:
# Output:
# function to check if two strings are 
# anagram or not  
def check(s1, s2): 
      
    # the sorted strings are checked  
    if(sorted(s1)== sorted(s2)): 
        print("The strings are anagrams.")  
    else: 
        res = [] 
        for i in s1:
            for j in s2:
                if i == j:
                    res.append(i)
                    list(s1).remove(i)
                    list(s2).remove(j)
                    print(s1,s2)
                    break
            # break        

        print(f"The strings aren't anagrams: {str(res)}")                 
          
# driver code   
word1 ="good"
word2 ="doing"
check(word1, word2)
