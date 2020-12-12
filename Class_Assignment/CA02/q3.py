#slice the list into 3 different part

my_list = [33,10,15,14,99,85,65,75,50,88,23,00]
slice1 = my_list[0:4]
slice2 = my_list[4:8]
slice3 = my_list[8:12]
slice1.reverse()

print(slice1)
print(slice1[::-1])
print(slice2[::-1])
print(slice3[::-1])
