# RGB Lookup

colours = [
    ['red', 'F00'],
    ['yellow', 'FF0'],
    ['green', '0F0'],
    ['cyan', '0FF'],
    ['blue', '00F'],
    ['magenta', 'F0F'],
]
print(f'I have learned the RGB code for {len(colours)} colours so far.')

colour = input("Please enter a colour name: ")

# DO NOT CHANGE CODE ABOVE THIS LINE


# TODO:
# Given a colour name as input from the user print the RGB code for that colour.

# The input case should be ignored, 'RED' and 'red' should both print the same code.
# The ouput should look something like this:
# >> The RGB code for 'red' is 'F00'.
#
#colour.lower()
#print(f"The RGB code for {colour} is {colours[]}")

dictionary_colours = dict (colours)                                       #convert the list into dictionary
colour = colour.lower()                                                   #convert the input into lower case
print(f"The RGB code for {colour} is {dictionary_colours.get(colour)}")   #find th code of the entered colour and print them
