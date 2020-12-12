# You are given a list of words. Write a function called find_frequencies(words) 
# which returns a dictionary of the words along with their frequency.
# Input: find_frequencies(['cat', 'bat', 'cat'])
# Return: {'cat': 2, 'bat': 1}

def find_frequencies(words): 
    freq_list= []    
    for i in words:              
        # checking for the duplicacy 
        if i not in freq_list: 
            freq_list.append(i)      
    
    # 
    dict_freq = {i:my_words.count(i) for i in freq_list}
    return dict_freq

my_words =['apple', 'mango', 'apple', 'orange', 'orange', 'apple', 'guava', 'mango', 'mango']

print(f"the freq of each word is: \n{find_frequencies(my_words)}")
