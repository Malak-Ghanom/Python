#Create a function which returns a list of all even number between x and y. Use the range() function.

def even_number(n1,n2):
    even_number=[]
    for i in range(n1,n2+1):
        if i%2 == 0:
            even_number.append(i)
    return even_number

number1 = 6
number2 = 20
print(f"even number between {number1} and {number2} is: {even_number(number1,number2)}")            
