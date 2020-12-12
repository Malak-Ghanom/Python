'''
Write a program which prints the multiplication table of a given number (stop at 10).
Sample input: n=2
Sample output: 2x1 = 1, 2x2 = 4, 2x3 = 6, 2x4 = 8, 2x5 = 10 ... 2x10 = 20'''

number = input("Please insert an int number: \n")
number = float (number)
number = int (number)
number = abs (number)

for i in range(1,11):
    print(f"{number}x{i} = {number*i}",end=' , ')
    