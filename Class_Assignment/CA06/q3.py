# Shopping List

# Your shopping list should keep asking for new items until nothing is entered (no input followed by enter/return key).
# The program should then print a menu for the user to choose one of the following options:
# (A)dd - To add a new item to the list.
# (F)ind - To search for an item in the list.
# (P)rint - To pretty print the list.
# (S)ort - To sort the list.
# (C)lear - To clear all items in the list.
# (Q)uit - To exit your program.

# TODO: Define a data structure to keep track of your shopping list.
shopping_list = []

# TODO: Implement a function to show the menu to the user, then wait for a valid user choice.
def show_menu():
    print("""please choose one of the following options:\n
# (A)dd - To add a new item to the list.\n
# (F)ind - To search for an item in the list.\n
# (P)rint - To pretty print the list.\n
# (S)ort - To sort the list.\n
# (C)lear - To clear all items in the list.\n
# (Q)uit - To exit your program.\n""")

# TODO: Implement a function to add an item to your shopping list.
def add_item(item):
    shopping_list.append(item)
    print(f"The item has successfully added to the list, the new list is:\t{shopping_list}\n")

# TODO: Implement a function to find an item in your shopping list.
def find_item(item):
    if item in shopping_list:
        print("The item is in the list")
    else:
        print("The item is not in the list, would you like to add it?")
        answer = input("Please insert y to add / n not to add? ")
        if answer == 'y':
            add_item(item)
            print(f"The item has successfully added to the list, the new list is:\t{shopping_list}")

# TODO: Implement a function to pretty print your tabbed lits.
def print_list():
    print(f"The shopping list is:\t {shopping_list}")

# TODO: Implement a function to pretty print your tabbed lits.
def sort_list():
    print(f"The shopping list is:\t {shopping_list.sort()}")


# TODO: Implement a function to pretty print your tabbed lits.
def clear_list():
    shopping_list.clear()

# TODO: Implement a function which calls the exit() function.
def quit():
    print("Goodbye! Hope to see you again soon :).")
    exit()


while True:
    show_menu()
    option = str (input("enter a value: ").upper())
    #print(option)
    if option == 'A':
        element = input("Please insert the element:\n")
        add_item(element)

    elif option == 'F':
        element1 = input("Please insert the element:\n")
        find_item(element1)
        
    elif option == 'P':
        print_list()

    elif option == 'S':
        sort_list()
        
    elif option == 'C':
        clear_list
        
    elif option == 'Q':
        quit()


