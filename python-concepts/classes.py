class Employee:
    company = "Autodesk"

    def __init__(self, salary, name, bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        #if this instance variable is not present then the class variable will be printed
        self.company = company

    def employee_info(self):
        print(f"Employee {self.name} working with {self.company}, earning {self.salary} and has {self.bond} years bond.")
        print("this is a way to print the class variable, it can also be accessed outside of the class:", Employee.company)

emp1 = Employee(70000, "Grok", 2, "Microsoft")
emp1.employee_info()
print("this is instance attribute:", emp1.company)
print("This is class attribute(variable):", Employee.company)

# object introspection
print("all the attributes and methods will be printed from this class:"
      " ", dir(emp1))



