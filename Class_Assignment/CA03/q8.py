#Given two sets, checks if one set is subset or superset of the other set.
#If a subset is found delete all elements from that set.
#Look at the docs for Python Set

family = {'Waleed','Amal','Sajida','Malak','Alaa','Ez','Maimana','Taqwa','Jalal'}
new_family = {'Ahmad','Malak','Adam'}

print(f"is the new_family a subset from family or superset, the answer is : {new_family.issubset(family) or new_family.issuperset(family)}")
