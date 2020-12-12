# given an input list remove the element at index 2 and add it at index 4 and also at the end of the list

my_list = [33,10,15,14,99,85,65,75]
removed_index = my_list.pop(2)
my_list.insert(4,removed_index)
my_list.append(removed_index)

print(f"\nThe new list is: {my_list}\n")
