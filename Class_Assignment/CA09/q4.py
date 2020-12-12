# Iterate over the range(1, 100) and print the numbers. However, if the number is a multiple of 3, print Fizz instead.
#  If the number is a multiple of 5, print Buzz. If the number is a multiple of both 3 and 5, print FizzBuzz.

# Input: None
# Print: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz 10 ...

for i in range(1,101):
    if i%5 == 0 and i%3 == 0:
        print ("FizzBuzz" , end= " ")
    elif i%3 == 0:
        print("Fizz", end=" ")
    elif i%5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")

list_my = [number for i in range(1,101) if i%5 == 0 and i%3 == 0]