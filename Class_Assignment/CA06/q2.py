# Guacamole Search

""" The linear search is used to find an item in a list. 
The items do not have to be in order. 
To search for an item, start at the beginning of the list and continue searching 
until either the end of the list is reached or the item is found.
"""


ingredients = ["1 tbsp cilantro", "2 avocados", "1 lime" , "1 tsp salt", "1/2 onion"]


# TODO: Implement the function which adds an ingredient to the list
def add_ingredient(ingredient):
    global ingredients
    ingredients.append(ingredient)

# TODO: Implement the function which removes and returns the last ingredient in the list
def pop_ingredient():
    return ingredients.pop()

# TODO: Implement the function which removes and returns an ingredient at the given index
def pop_ingredient_at(index):
    #removed_ingredient = ingredients[index]
    return ingredients.pop(index)

# TODO: Implement the function which counts and returns the number of needed ingredients
def count_ingredients():
    return len(ingredients)

# TODO: Implement the function which print the number of ingredients needed and a tabbed list of ingredients
def pretty_recipe():
    print(f"The number of ingredients needed is {len(ingredients)}")
    for ingredient in ingredients:
        print(f"\t *{ingredient}")


# TODO: 
# * Implement the linear search algorithm on the list of ingredients.
# * Test that it works with ingredients in and not in the list.
# * Add a counter to keep track of how many searches have been done for each item searched for.
# * Add the functionality to add an item to the list if it is not found.

def search_for_ingredient(ingredient):
    count = 0
    found = False
    for i in ingredients:
        count+=1
        if i == ingredient:
            found = True
            print(f"the item {ingredient} is exist in the list, i found it after {count} iterate")
            break
        
    if found == False:
        add_ingredient(ingredient) 
        print(f"the item {ingredient} is not exist in the list, i add it after {len(ingredients)} iterate")
        
    
        


# TODO: Call your functions here to test your code.

pretty_recipe()
add_ingredient('garlic')
search_for_ingredient('garlic')
pretty_recipe()
pop_ingredient()
pretty_recipe()
add_ingredient('salt')
pretty_recipe()
print(f"the removed element is {pop_ingredient_at(1)}") 