# Write a function recursive_sum(numbers) which returns the sum of the list.
# Input: numbers = [1, 2, 3, 4, 5]
# Return: 15

my_numbers = [1, 2, 3, 4, 5]
count = 0
numbers_sum = 0
def recursive_sum(numbers):

    global numbers_sum,count
    numbers_sum += numbers[count]
    count+=1
    if count == len(numbers):
        return numbers_sum
    else:
        return recursive_sum(numbers)

print(f"the sum of the list is: {recursive_sum(my_numbers)}")
