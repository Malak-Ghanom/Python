#Ask the user for two integers (x, y) as input. 
#Create a range using the range(x,y) then only print the positive numbers.

number1 = int(input("enter the first intejer number: "))
number2 = int(input("enter the second intejer number: "))

for i in range(number1, number2+1):
    if i >= 0:
        print(i, end=" ")