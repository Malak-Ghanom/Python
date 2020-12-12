# You are given a binary string (001101001011) as input,
#  return a list of all substrings which start and end with a 1.

# Input: 001011001011
# Return: ['101', '1011', '1011001', '101100101', '1011001011', '']

binary_word = "001011001011"
def binary_substring(binary_string) :  
    sub_list = []
    for i in range(0, len(binary_string)) : #detect first '1' 
        
        if (binary_string[i] == '1') : 
            string = binary_string[i]

            for j in range(i+1, len(binary_string)) : #detect end '1'

                if (binary_string[j] == '1') : 
                    string += binary_string[j]
                    sub_list.append(string)
                elif (binary_string[j] == '0'):
                    string += binary_string[j]       
    return sub_list 
       
print(f"the substring that starts and end with '1' is: {binary_substring(list(binary_word))}")