""" Write a program which prints the following pattern for any given number, n = 5, for example.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5"""


number = input("Please insert an int number: \n")
number = float (number)
number = int (number)
number = abs (number)

number = 5
for i in range(1,number+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print("\t")    
        
for h in range(number+1,1,-1):
    for k in range(1,h):
        print(k, end=' ')
    print("\t")
        
