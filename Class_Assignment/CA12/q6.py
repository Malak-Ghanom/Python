#Which exceptions can the code below raise? Extend the code to 
# handle all of them in a reasonable manner.


number_list = [ 100, 101, 0, "103", 104 ]

try:
    i = int(input( "Give an index: " ))
    print(f"100 / {number_list[i]} = {100 / number_list[i]}")

except ValueError:
    print("invalid litral expect intejer index")

except ZeroDivisionError:
    print("Divided by Zero")

except IndexError:
    print("entered index out of range")

except TypeError:
    print('expect intejer number')

