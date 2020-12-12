"""Given two lists, create a third list by picking an even-index element from the first list and odd-index element from second.
first_list = [3, 6, 9, 12, 15, 18, 21]
second_list = [4, 8, 12, 16, 20, 24, 28]
results_list = [6, 12, 18, 4, 12, 20, 28]"""

first_list = [3, 6, 9, 12, 15, 18, 21]
second_list = [4, 8, 12, 16, 20, 24, 28]
max_list = []
max_list.append(len(first_list))
max_list.append(len(second_list))
print(max(max_list))
results_list = []

for i in range( 0 , max(max_list)):
    if i % 2 == 0:
        results_list[i]=second_list[i]
    else:
        results_list[i]=first_list[i]  

print(f"The Results list is: {results_list}")          
