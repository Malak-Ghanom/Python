# Famous Dinner

# You are inviting three famous people for dinner.
guests = ['nicola tesla', 'albert einstine', 'leonardo da vinci']

# Invite your guests to dinner.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# TODO: Einstine can't make it on this day! Remove him and invite Socrates instead.
del(guests[1])
guests.insert(1,'Socrates')
print(f"{name}, please come to dinner.")

# TODO: Print the invitations again.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")
# We got a bigger table
print("\nWe got a bigger table!")

# TODO: Think of three more people and add them to the list.
# Use append() and insert() at least once
guests.insert(0,'Ahmad')
guests.insert(3,'Malak')
guests.append('Adam')

# TODO: Print the invitations again.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")
# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

# TODO: Use the following lines to remove a guest from the list, make sure you only invite two.
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")


# TODO: There should be two people left. Let's invite them.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

# We all have good food, and good conversation. Time to go.
print("\nGood food. Good conversation. Bye for now.")

# TODO: Empty out your guest list.
guests.clear()

# TODO: Print your empty guest list
print(f"The  invited guests are: {guests}")
