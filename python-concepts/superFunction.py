class Wasim:

    def __init__(self, a, b):
        a = a + a 
        b = b + b
        print(f"parent class operation: a = {a}, b = {b}")

    def parentFunc(self):
        print("This is parent function!")

    def addition(self, a, b):
        return a + b

class Maryam(Wasim):
    def __init__(self, a, b, c, d):
        c = c + c
        d = d + d
        super().__init__(a, b)
        print(f"parent class operation: c = {c}, d = {d}")

    def childFunc(self):
        print("This is child function!")
    
    def addition(self, a, b, c, d):
        parent_addition = super().addition(a, b)
        return parent_addition + c + d


obj = Wasim(1,2)
obj = Maryam(1,2,3,4)
obj.childFunc()
obj.parentFunc()

print(obj.addition(1,2,3,4))
