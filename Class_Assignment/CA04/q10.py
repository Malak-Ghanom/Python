"""
Given two lists of equal size create a set which contains elements from both lists as a pair.
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
results_set = {(2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64)}"""

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
index = len(first_list)

results_set = set((first_list[x],second_list[x]) for x in range(0, index))

print(f"results_set = {sorted(results_set)}")

