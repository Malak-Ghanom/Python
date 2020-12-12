from shape import Shape

# Circle class


class Circle(Shape):

    pi = 3.14
    # TODO: Implement __init__() for this class
    def __init__(self, radius=1.0):
        self.radius = radius

    # TODO: Implement find_area() for this class
    def find_area(self):
        return self.pi*(self.radius**2)

    # TODO: Implement find_circumference() for this class
    def find_circumference(self):
        return self.pi*(self.radius*2)