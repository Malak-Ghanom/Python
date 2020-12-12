# Class Circle

class Circle:

    # TODO: Define an instance attribute for PI
    PI = 3.14

    def __init__(self, radius=1.0):
        # TODO: Define an instance attribute for the radius
        self.radius = radius

    # TODO: Define the string representation method and print
    # r = {self.radius} c = {self.get_circumference()} a = {self.get_area()}
    def __str__(self):
        return f"r = {self.radius} c = {self.get_circumference()} a = {self.get_area()}"

    # TODO: Define a get_area() method and return the area
    def get_area(self):
        return Circle.PI * (self.radius ** 2)

    # TODO: Define a get_circumference() method and return the circumference
    def get_circumference(self):
        return 2 * self.radius * Circle.PI
    
    # TODO: Define a set_color(color) method which sets the object attribute
    def set_color(self, color):
        self.color = color
    
    # TODO: Define a get_color() method which returns the object attribute
    def get_color(self):
        return self.color

# Playground

# TODO: Create two circles one with radius 3, and one with the default radius
circle1 = Circle(3)
circle2 = Circle()

# TODO: Set the colors of your circles using the setter method
circle1.set_color('yellow')
circle2.set_color('green')

# TODO: Print the colors of your circles using the getter method
print(f"The first circle has a {circle1.get_color()} color")
print(f"The second circle has a {circle2.get_color()} color")

# TODO: Print your circles. How does this work?
print(circle1)
print(circle2)

# TODO: Print the radius and areas of your cricles
print(f"The first circle has a {circle1.get_area()} raduis and {circle1.radius} of area")
print(f"The second circle has a {circle2.get_area()} raduis and {circle2.radius} of area")

# TODO: Print the circumference of your circles using the getter methods
print(f"The first circle has a circumference of {circle1.get_circumference()}")
print(f"The second circle has a circumference of {circle2.get_circumference()}")