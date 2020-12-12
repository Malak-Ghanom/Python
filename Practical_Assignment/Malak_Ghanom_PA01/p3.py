# Places

# Think of at least five places in the world you’d like to visit.

# TODO: Store the locations in the list locations.
locations = ['Turkey','London','Paris','America','Ireland']

# TODO: Print your list in its original order.
print(f"The locations are: {locations}")

# TODO:
# Sort and print your list in alphabetical order wihout modifying the actual list. Read about the sorted() function.
print(f"The sorted locations are: {sorted(locations)}")
# Show that your list is still in its original order by printing it.
print(f"The original list of locations are: {locations}")

# TODO:
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(f"The reversed sort of the locations are: {sorted(locations,reverse=True)}")
# Show that your list is still in its original order by printing it again.
print(f"The original list of locations are: {locations}")

# TODO: Use reverse() to change the order of your list. Print the list to show that its order has changed.
locations.reverse()
print(f"The reversed of the original list is: {locations}")

# TODO: Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
locations.reverse()
print(f"The original list of locations are: {locations}")

# TODO: Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
locations.sort()
print(f"The original list of locations are: {locations}")

# TODO: Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
locations.sort(reverse=True)
print(f"The original list of locations are: {locations}")
