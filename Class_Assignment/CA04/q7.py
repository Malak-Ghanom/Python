#Write a program which reads the age of 3 different people. Then print the oldest, and youngest between them.

age1 = int (input("1- Please enter your age: "))
age2 = int (input("2- Please enter your age: "))
age3 = int (input("3- Please enter your age: "))

ages_list = []
ages_list.append(age1)
ages_list.append(age2)
ages_list.append(age3)

print(f"The oldest one is: {max(ages_list)} and the youngest one is {min(ages_list)}")