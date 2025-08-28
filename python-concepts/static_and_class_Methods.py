class Students:

    def __init__(self, name, age):
        #self.name -- instance variable, name -- local variable
        self.name = name
        self.age = age

    # instance method
    def student_info(self):
        return f"The student {self.name} is {self.age} years old"

    @staticmethod
    def sum1(num1, num2):
        return num1 + num2

    #class variable
    university = "Pune"

    @classmethod
    def change_university(cls, new_university):
        cls.university = new_university

s1 = Students("Wasim", "28")
print(s1.student_info())

# both static and class variales and methods can be access through class name or class instance name(object) obj.methodname(), Classname.methodname
# ways to access static method
print(s1.sum1(4, 8))
print(Students.sum1(3, 2))

# ways to access class method
print(Students.university)
s1.change_university("Mumbai")
print(Students.university)
Students.change_university("Oxford")
print(s1.university)
