import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius:
            self.radius = radius
        elif diameter:
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided")
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def __repr__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f})"
    
    def __add__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Can only add two Circle objects")
        new_radius = self.radius + other.radius
        return Circle(radius=new_radius)
    
    def __gt__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Can only compare Circle objects")
        return self.area() > other.area()
    
    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Can only compare Circle objects")
        return self.area() == other.area()
    
    def __lt__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Can only compare Circle objects")
        return self.area() < other.area()

# Example usage:
circle1 = Circle(radius=5)
circle2 = Circle(diameter=12)

print(circle1)  # Circle(radius=5.00, diameter=10.00)
print(circle2)  # Circle(radius=6.00, diameter=12.00)

print("Circle 1 area:", circle1.area())  # Area of circle 1
print("Circle 2 area:", circle2.area())  # Area of circle 2

# Adding circles
circle3 = circle1 + circle2
print("New Circle (added):", circle3)

# Comparing circles
print("Is Circle 1 greater than Circle 2?", circle1 > circle2)
print("Are Circle 1 and Circle 2 equal?", circle1 == circle2)

# Sorting circles
circles = [circle1, circle2, circle3]
sorted_circles = sorted(circles, key=lambda c: c.area())
print("Sorted Circles by area:", sorted_circles)