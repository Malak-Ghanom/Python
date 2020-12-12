# Define a class called User.
class User:


# Define two attributes called first_name and last_name.
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
# Define and then create several other attributes that are typically stored in a user profile.
        self.age = None
        self.id = 0
        self.university = None
# Define an attribute called login_attempts to your User class.
    login_attempts = None
    
# Define a method called describe_user() that prints a summary of the user’s information.
    def describe_user(self ):
        print(f"""The user information is:  *First name: {self.first_name}
                          *Last name: {self.last_name}
                          *Age: {self.age}
                          *ID: {self.id}
                          *University: {self.university}\n """)

# Define a another method called greet_user() that prints a personalized greeting to the user.
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, hope you have enjoying :)")

# Define a method called increment_login_attempts() that increments the value of login_attempts by 1.
    def increment_login_attempts(self):
        self.login_attempts += 1

# Define another method called reset_login_attempts() that resets the value of login_attempts to 0.
    def reset_login_attempts(self):
        self.login_attempts = 0


# Create several instances representing different users, and call both methods for each user.
person1 = User('Malak', 'Ghanom')
person1.age = 24
person1.id = 111
person1.university = 'HU'
person1.greet_user()
person1.describe_user()

person2 = User('Ahmad', 'Abu Alnadi')
person2.age = 24
person2.id = 112
person2.university = 'HU'
person2.greet_user()
person2.describe_user()

person3 = User('Adam', 'Abu Alnadi')
person3.age = 1
person3.id = 113
person3.university = None
person3.greet_user()
person3.describe_user()

# Create an instance of the User class and call increment_login_attempts() several times.
person1.reset_login_attempts()
person1.increment_login_attempts()
person1.increment_login_attempts()
person1.increment_login_attempts()
person1.increment_login_attempts()
person1.increment_login_attempts()

# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
print(f"The number of attempts is: {person1.login_attempts}")
person1.reset_login_attempts()

# Print login_attempts again to make sure it was reset to 0.
print(f"The number of attempts is: {person1.login_attempts}")