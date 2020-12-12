#Write a program which reads a number (n) from the user and the print the sum of all numbers between 1 and n.

number = input("Please insert an int number: \n")
number = float (number)
number = int (number)
number = abs (number)

print(number)

sums = 0
for i in range(number+1):
    sums+=i

print(f'the sum of numbers is: {sums}')