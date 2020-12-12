# Symmetric Difference

odd_list = [1, 3, 5, 7, 9]
natural_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# DO NOT CHANGE CODE ABOVE THIS LINE

difference_in_natural =  set(natural_list) - set (odd_list)                 #extract the difference in natural_list
difference_in_odd = set(odd_list) - set(natural_list)                       #extract the difference in odd_list
total_differences= difference_in_natural.union(difference_in_odd)           #join the two differences togather   
print(f"the difference between two list is: {list(total_differences)}")     #print the difference

# TODO:
# Print a list of the difference between the two lists.
# You cannot use the symmetric_difference() method for sets to solve this problem.
#
# For the input above, the printed list looks like this:
# >> [2, 4, 6, 8]