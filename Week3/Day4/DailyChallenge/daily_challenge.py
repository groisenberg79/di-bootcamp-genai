# Instructions
# The goal is to create a class that represents a simple circle.

# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.

# Abilities of a Circle Instance
# Your Circle class should be able to:
# ✅ Compute the circle’s area.
# ✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).
# ✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).
# ✅ Compare two circles to see which is bigger — use a dunder method (__gt__).
# ✅ Compare two circles to check if they are equal — use a dunder method (__eq__).
# ✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.

from math import pi

class Circle:
    def __init__(self, radius: int | float) -> float:
        self.radius = round(float(radius), 2)
    
    @property
    def diameter(self) -> float:
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value: int | float) -> float:
        self.radius = round(value / 2, 2)

    def __repr__(self):
        return f"(radius: {self.radius}, diameter: {self.diameter})"

    def area(self):
        return round(pi * self.radius**2, 2)
    
    def __add__(self, other: Circle) -> Circle:
        return Circle(self.radius + other.radius)
    
    def __gt__(self, other: Circle) -> bool:
        return self.radius > other.radius

        
    def __eq__(self, other: Circle) -> bool:
        return self.radius == other.radius

    
    def __lt__(self, other: Circle) -> bool:
        return self.radius < other.radius
    

c1 = Circle(5)
print(f"c1: {c1}")
c2 = Circle(10)
print(f"c2: {c2}")
c3 = Circle(15)
c4 = Circle(10)
print()

c1.diameter = 7.5
print(f"new c1: {c1}")
print()

print(f"area of c1: {c1.area()}")
print()

new_circle = c2 + c3
print(f"new_circle = c2 + c3: {new_circle}")
print()

print(f"is c2 > c3: {c2 > c3}")
print()

print(f"is c2 == c4: {c2 == c4}")
print(f"is c2 == c3: {c2 == c3}")
print()


circle_list = [c1,new_circle,c2,c4,c3]
print(f"unsorted list of circles: {circle_list}")
print()
print(f"sorted list of circles: {sorted(circle_list)}")