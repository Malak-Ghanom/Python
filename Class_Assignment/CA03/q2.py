#Given a list, remove all duplicate element and create a tuple with the remaining values. Then find the minimum and maximum numbers in that tuple.
#list = [87, 45, 41, 65, 94, 41, 99, 94]
#tuple = (87,45, 41, 65, 99)
#min = 41 max = 99

my_list = [87, 45, 41, 65, 94, 41, 99, 94]
del_duplicate = set(my_list)
new_tuple = tuple(del_duplicate)

print(f"\nThe min value of the tuple is: {min(new_tuple)} and The max value of the tuple is: {max(new_tuple)}\n")
