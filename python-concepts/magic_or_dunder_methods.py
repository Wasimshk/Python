import math
from sys import exception


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print(f"X = {self.x} and Y = {self.y}")

    # this sum function takes class object as an argument and returns the class object
    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))

    def isPointInstance(self, obj):
        if not isinstance(obj, Point): #this checks if the passed argument is Point class Obj
            exception("passed argument is not an instance of a class Point")

    def point_distance(self, p):
        self.isPointInstance(p)
        # point distance formulla sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    # operator overloading through "magic method(dunder method)"
    # When the + operator is used between two instances of a class that has defined the __add__() method, Python automatically calls this method on the left-hand operand, passing the right-hand operand as an argument.
    def __add__(self, p):
        # used to overload + operator
        self.isPointInstance(p)
        return Point((self.x + p.x), (self.y + p.y))

    def __sub__(self, p):
        # used to overload - operator
        self.isPointInstance(p)
        return Point((self.x - p.x), (self.y - p.y))

    def __mul__(self, p):
        # used to overload * operator
        self.isPointInstance(p)
        return Point((self.x * p.x), (self.y * p.y))

    def __truediv__(self, p):
        # used to overload / operator
        self.isPointInstance(p)
        return Point((self.x / p.x), (self.y / p.y))

    def __eq__(self, p):
        # used to overload == operator
        self.isPointInstance(p)
        return self.x == p.x and self.y == p.y

    def __ne__(self, p):
        # used to overload != operator
        self.isPointInstance(p)
        return self.x != p.x and self.y != p.y

    def __lt__(self, other):
        # used to overload < operator
        pass

    def __gt__(self, other):
        # used to overload > operator
        pass

    def __len__(self):
        # used to overload len() function
        pass

    # for list/dict like behavior allowing us to use [] with the object
    def __getitem__(self, item):
        # used to overload
        pass

    def __setitem__(self, key, value):
        # used to overload
        pass

    def __delitem__(self, key):
        # used to overload
        pass

p1 = Point(2, 3)
p2 = Point(4, 6)
p3 = Point(2, 3)

p = p1.sum(p2)  # this takes class object as an argument
p.print_point()

# operator overloading
p = p1 + p2 #same as p1.__add__(p2)
p.print_point()

p = p1 - p2
p.print_point()

p = p1 * p2
p.print_point()

p = p1 / p2
p.print_point()

p = p1 == p3
print("is p1 equals to p3?", p)
print("is p1 equals to p2?", p1==p2)

print("is p1 not equals to p3?",p1!=p3)
print("is p1 not equals to p2?",p1!=p2)

# point distance
d = p1.point_distance(p2)
print("Distance between point is:", d)