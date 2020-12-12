#Given a dictionary the following dictionary, 
#personal_info={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
#1 Print when and where Plato was born.
#2Change Plato's birth year from B.C. 427 to B.C. 428.
#3Add the following item to the dictionary --> "work": ["Apology", "Phaedo", "Republic", "Symposium"]
#4Find and print how many keys there are in the dictionary.
#5Find and print the key with the highest value in the dictionary.
#6Find and print the key with the lowest value in the dictionary. """

personal_info={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}

#1
print(f"{personal_info['name']} born in_ {personal_info['born']} and_ lives in_ {personal_info['country']}")

#2
personal_info['born']= 428

#3
personal_info['work']=["Apology", "Phaedo", "Republic", "Symposium"]

#4
my_keys = personal_info.keys()
my_values = personal_info.values()
print(f"the keys are: {my_keys} and the number of keys is: {len(my_keys)} ")

#5
print(f"the highest value of the keys is: {max(my_keys)}")

#6
print(f"the highest value of the values is: {min(my_keys)}")
