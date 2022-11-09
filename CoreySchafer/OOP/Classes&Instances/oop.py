class Employee:
    
    def __init__(self, name, last, pay): # self --> is instance(emp_1)
        self.name = name # same as emp_1.name = "Abylai"
        self.last = last # Attributes
        self.pay = pay # Attributes
        self.email = name + "." + last + "@company.com" # Attributes

    def full_name(self):
        return f"{self.name} {self.last}"


# emp_1 -> instance of Employee class
emp_1 = Employee("Abylai", "Aitbanov", 177)
emp_2 = Employee("Bob", "Aitbanov", 299)

print(emp_1.email)
print(emp_2.email)

print(Employee.full_name(emp_1))
print(emp_1.full_name())
print(emp_2.full_name())



# emp_1.name = "Abylai"