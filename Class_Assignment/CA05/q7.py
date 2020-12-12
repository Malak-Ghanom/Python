#Create a function sum_or_max(my_list), given a list, 
# if the length of the list is even return the sum of the list. 
# If the length is odd, return the maximum value in that list.

def sum_or_max(my_list):
    if len(my_list)%2 == 0:
        return sum(my_list)
    return max(my_list) 

num_list = [1,2,3,4,5,6,7]       

if len(num_list)%2 == 0:
    print(f"the sum of the list is: {sum_or_max(num_list)}")
else:
    print(f"the max of the list is: {sum_or_max(num_list)}")