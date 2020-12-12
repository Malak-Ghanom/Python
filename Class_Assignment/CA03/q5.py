#Modify the value 22 inside the following tuple to 2222.
#tuple = (11, [22, 33], 44, 55)


tuple0 = (11, [22, 33], 44, 55)
list0 = list(tuple0)
list0[1][0]=2222
tuple0= tuple(list0)
print(f"the tuple after modified is: {tuple0}") 
