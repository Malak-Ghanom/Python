# Fibonacci Sequence

# TODO: Implement a recusrive fibonacci function
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 9
# Check if the number of terms is valid
if n <= 0:
   print("Please enter a positive integer.")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(fibonacci(i))