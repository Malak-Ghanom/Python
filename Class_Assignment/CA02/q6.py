#add no. to the compound list

lists = [ 10, 20, [300, 400, [5000, 6000], 500], 30, 40]

lists[2][2].insert(2,7000)

print("New list is: ", lists)