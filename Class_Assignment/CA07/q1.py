#Define a class called Restaurant.
class Restaurant:

#The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
# Add an attribute called number_served with a default value of 0.
        self.number_served = 0

#Define a method called describe_restaurant() that prints these two pieces of information.
    def describe_restaurant(self):
        print(f"The resturant name is {self.restaurant_name} and the cuisine type is {self.cuisine_type}")

#Define a method called open_restaurant() that prints a message indicating that the restaurant is open.
    def open_restaurant(self):
        print(f"The resturant opens from 9:00 AM to 11:00 PM")

# Define a method called set_number_served() that lets you set the number of customers that have been served.
    def set_number_served(self, number_people):
        self.number_served = number_people

# Define a method called increment_number_served() that lets you increment the number of customers who’ve been served.
    def increment_number_served(self , number):
        self.number_served += number

#Create an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
restaurant = Restaurant('pizza hut', 'Italian')
print(f"The resturant name is {restaurant.restaurant_name} and the cuisine type is {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Create three different instances from the class, and call describe_restaurant() for each instance.
restaurant1 = Restaurant ('Fried Potato' , 'Irish')
restaurant2 = Restaurant ('Fire Fly', 'American')
restaurant3 = Restaurant ('Alia' , 'Jordanian')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class.
# Print the number of customers the restaurant has served, and then change this value and print it again.
print(f"The number of people have been served is: {restaurant.number_served}.") 
restaurant.number_served = 34
print(f"The number of people have been served is: {restaurant.number_served}.") 

# Define a method called set_number_served() that lets you set the number of customers that have been served.
# Call this method with a new number and print the value again.
restaurant.set_number_served(60)
print(f"The number of people have been served is: {restaurant.number_served}.") 


# Define a method called increment_number_served() that lets you increment the number of customers who’ve been served.
# Call this method with any number you like that could represent how many customers were served in,
#  say, a day of business

restaurant.increment_number_served(14)
print(f"The number of people have been served is: {restaurant.number_served}, a day of business.") 
