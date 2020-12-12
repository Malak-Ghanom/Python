# Write a function find_max_sublist(numbers) which returns the sum of maximum sub-list in a list of integers.
# Input: numbers = [-8, -2, 4, 6, 8, 4, 5, -3]
# Return: 27

my_numbers = [-8, -2, -4, -6, 8, -4, -1, -3]  # -9 #-1

def find_max_sublist(numbers):
    sum1 = sum(numbers)
    
    min_number = min(numbers)
    numbers.remove(min_number)
    sum2 = sum(numbers)
    print(f"sum1 {sum1} min num {min_number} sum2 {sum2}")
    if sum2>sum1:
        return find_max_sublist(numbers)
    else:
        return sum2

    return sum1


print(f"max sum = {find_max_sublist(my_numbers)}")