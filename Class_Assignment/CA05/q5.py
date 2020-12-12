#Create a function seq_check(numbers) which when given a list of integers, 
# returns True if the sequence [1,2,3] appears somewhere in that list.

def seq_check(numbers):
    for i in range(0,len(numbers)-1):
        if numbers[i] == 1:
            if numbers[i+1] == 2:
                if numbers[i+2] == 3:
                    return True
                
my_list = [3,2,1,5,4,9,1,2,3]     

print(f"Does the sequence [1,2,3] appears somewhere in that list: {seq_check(my_list)}")