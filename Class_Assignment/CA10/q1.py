# Ask the user for an integer and then use a list comprehension to build a list with all even number smaller than n
# . Print the list to the user.
# Input: n = 10
# Print: your_even_numbers = [0, 2, 4, 6, 8]

number = int(input("insert a number: "))
your_even_numbers =[x for x in range(0,number+1) if x%2 == 0]
print(f"the even number between 0 and {number} = {your_even_numbers}")