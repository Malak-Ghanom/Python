#Given a tuple my_tuple = ('a', 'b', 'c', 'd)
#Create a list for each element in the tuple, inside each list you should have the value repeated n+1 times where n is the index in the tuple.
#Sample: b_list = ['b', 'b'] and c_list = ['c', 'c', 'c']
#Join all of the lists together and print the final output.
#final_list = ['a','b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd']

my_tuple = ('a', 'b', 'c', 'd')
a_list = list(my_tuple[0]*1)
b_list = list(my_tuple[1]*2)
c_list = list(my_tuple[2]*3)
d_list =  list(my_tuple[3]*4)

final_list = a_list + b_list + c_list + d_list

print(f"the final list is {final_list}")