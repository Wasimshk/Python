class Students:

    def __init__(self, name, age):
        #self.name -- instance variable, name -- local variable
        self.name = name
        self.age = age

    def student_info(self):
        """This string is called a doc-string and this function prints the student info, hover over function call to see this string or use print_point.__doc__"""
        return f"The student {self.name} is {self.age} years old"

    def __str__(self):
        # overloaded the str function, which is used for type casting but here we are using it for
        return f"The student {self.name} is {self.age} years old"

    def __repr__(self):
        return f"name: {self.name}\nAge: {self.age}"

    def __len__(self):
        # overloaded the len function, which returns the length of student name string
        return len(self.name)

s1 = Students("Wasim", 28)
print(str(s1))
print(str(23)) #normal usage of str function to type cast the int to str
print(repr(s1))

print(len(s1)) #prints the length of student name string, by passing student object

# way to see the doc-string of any class method.
print(s1.student_info.__doc__)

