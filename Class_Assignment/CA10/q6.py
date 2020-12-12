# Write a function generate_flat_list(nested_list) which flattens a nested list. The function returns the flattened list.
# Input: nested_list = [[1, 2, [3, 4]], [5, 6], 7] and call generate_flat_list(nested_list)
# Output: [1, 2, 3, 4, 5, 6, 7]

flat_list = []
def flatten_list(my_list):
    for element in my_list:
        if isinstance(element,list):
            flatten_list(element)
        else:
            flat_list.append(element)
    return flat_list

nested_list =  [[1, 2, [3, [4]]], [5, 6], 7]

print('Transformed Flat List', flatten_list(nested_list))