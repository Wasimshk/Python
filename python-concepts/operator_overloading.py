
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print(f"X = {self.x} and Y = {self.y}")

    # this sum function takes class object as an argument and returns the class object
    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))

    # operator overloading through "magic method(dunder method)"
    # When the + operator is used between two instances of a class that has defined the __add__() method, Python automatically calls this method on the left-hand operand, passing the right-hand operand as an argument.
    def __add__(self, p):
        # used to overload + operator
        return Point((self.x + p.x), (self.y + p.y))

p1 = Point(2, 3)
p2 = Point(4, 9)

p1.print_point()
p2.print_point()

p = p1.sum(p2) #this takes class object as an argument
p.print_point()

# operator overloading, means + operator can now add two point coordinates as well, we have used __add__() to overload
p = p1 + p2
# this is same as below
# p = p1.__add__(p2)
p.print_point()


