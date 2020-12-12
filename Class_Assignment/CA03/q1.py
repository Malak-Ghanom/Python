#Given the following list, lst=[11, 100, 99, 1000, 999]
#Print the first and last elements.
#Append the value 10000 to the list. Then append 9999 to the list.
#Insert the value 2 at every even index in the list that is lower than 10.
#Print the list, then print the list sorted.
#Count and print the number of times the element 2 appears in your list.
#Print the sum of the values in your list.

# malak ghanom
lst=[11, 100, 99, 1000, 999]

# branch 1
print (f"the first value of the list is: {lst[0]} and the last value of the list is: {lst[4]}")

#branch 2
lst.append(1000)
lst.append(9999)
print(f"the new list is: {lst}")

#branch 3
lst.insert(0,2)
lst.insert(2,2)
lst.insert(4,2)
lst.insert(6,2)
lst.insert(8,2)

#branch 4
print(f"the new list is: {lst}")
lst.sort()
print(f"the sorted list is: {lst}")

#branch 5
print(f"the number 2 appeare in the list {lst.count(2)} time")

#branch 6
print(f"the sum of the value is {sum(lst)}")

# the end