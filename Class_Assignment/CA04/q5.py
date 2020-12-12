"""Given a list of numbers, reverse the list without using the reverse() method."""

numbers_list = [10,20,30,40,50,60,70,80,90]

reversed_list = numbers_list.copy()

x = len(numbers_list)-1

for i in range(0,len(numbers_list)):
    reversed_list[x]= numbers_list[i]
    x-=1

print(f"\nThe list after reversed it without reversed() function is: {reversed_list}\n")