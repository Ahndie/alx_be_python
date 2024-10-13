import math

# Base Class - Shape
class Shape:
    def area(self):
        raise NotImplementedError("Derived classes must override this method.")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Main function to demonstrate polymorphism
def main():
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(5, 10)
    circle = Circle(7)

    # Create a list of shapes
    shapes = [rectangle, circle]

    # Loop through each shape and print its area using polymorphism
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area():.2f}")

if __name__ == "__main__":
    main()
