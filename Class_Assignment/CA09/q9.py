# Given a string with repeated characters as input,
#  create a function shuffle_well() and return a rearranged string so that no two adjacent characters are the same.

# Input: aaabb or aa
# Return: ababa or "String cannot be rearranged."
import random

# def shuffle_well(string):
#     for i in string:
#         for 


string1 = 'aaabb'


# shuffle_well(string1)
# shuffle_well(string2)
print(random.shuffle(list(string1)))