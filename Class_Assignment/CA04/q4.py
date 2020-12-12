"""Given a list of numbers iterate over it and print numbers which are divisible by 5.
 If you find number greater than 150 stop the exit iteration."""
 
my_list = [20,13,15,80,99,111,116,120,170]

print(f"The numbers that are divisible by (5) are: ", end=" ")

for i in range(0,len(my_list)-1):
    if my_list[i]> 150:
        break
    elif my_list[i] % 5 == 0: 
        print(my_list[i], end="  ")