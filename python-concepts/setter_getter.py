# _name is protected (convention) but it can be accessed. it is just for information to developers that this variable is private
# self.name = public
# self._name = protected (convention)
# self.__name = "private-ish" (can be accessed through name mangling)
class Employee:
    def __init__(self, name):
        self._name = name #_name is a private variable by convention

    # setter getter in other languages
    def get_name(self):
        return self._name
    def set_name(self, new_name):
        self._name = new_name

    # setter getter in python
    # getter
    @property
    def name(self):
        return self._name
    # setter
    @name.setter
    def name(self, new_name):
        self._name = new_name

emp1 = Employee("Wasim")
print("access Name through getter method:_____", emp1.get_name())
emp1.set_name("Shaikh")
print("access Name after updating name through setter:_____", emp1.get_name())

print("Direct access to private variable which is not safe and recommended:_____", emp1._name)
emp1._name = "Wasim" #direct access to the private variables which is not save and not recommended, hence we will use setter getter in pythonic way
print("direct access to the private variable updated by direct assignment:_____", emp1._name)

# pythonic way to setter and getter methods
emp2 = Employee("Wasim")
print("access through getter:_____", emp2.name) # looks like direct access but actually getter
emp2.name = "Shaikh" # looks like assignment but calls setter
print("updated name access through getter:_____", emp2.name)



# class Student:
#     def __init__(self, name):
#         self._name = name
#
#     #setter getter in python
#     #getter
#     @property
#     def name(self):
#         return self._name
#
#     #setter
#     @name.setter
#     def name(self, new_name):
#         self._name = new_name


