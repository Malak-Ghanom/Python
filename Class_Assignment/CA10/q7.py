# Write a function generate_flat_dict(nested_dict) which flattens a nested dictionary by joining the keys with the.
# character. The function returns the flattened dictionary.
# Input: nested_dict = {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4} and call generate_flat_dict(nested_dict)
# Output: {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}

flat_dict = {}
def flatten_dict(initial_dict, separator ='', prefix =''): #generate flat dict
    for k,v in initial_dict.items():                       #extract key with value
        if isinstance(v , dict):
            flatten_dict(v , separator = '.' , prefix=k)            
        else:
            flat_dict[prefix+separator+k]= v
    return flat_dict        

# initialising_dictionary 
initial_dict =  {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
    
# printing final dictionary 
print (f"final_dictionary{flatten_dict(initial_dict)}") 