#Create a function which returns a list of all numbers between 1 and 50 that are divisible by 3.

def divisible_by_three():
    three_list=[]
    for i in range(1,50):
        if i%3 == 0:
            three_list.append(i)
            if i == 50:
                break
    return three_list            

three_list = divisible_by_three()
print(f"the list of all numbers between 1 and 50 that are divisible by 3 are: {three_list}")