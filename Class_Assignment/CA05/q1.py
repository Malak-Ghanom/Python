#Create a function check_ten(n1, n2) which returns a Boolean True if the sum of the numbers is 10.

def check_ten(n1, n2):
    if n1+n2 == 10:
        return True


number1 = int (input("Please insert the first number: \n"))
number2 = int (input("Please insert the second number: \n"))

boolean = check_ten(number1,number2)
print(f"Is the sum of the two numbers 10: {boolean}")