class Employee:

    num_of_emps = 0 # Class Variable -> we can call it -> Employee.num_of_emps
    raise_amount = 1.04

    def __init__(self, name, last, pay):  # self --> is instance(emp_1)
        self.name = name  # same as emp_1.name = "Abylai"
        self.last = last  # Attributes
        self.pay = pay  # Attributes
        self.email = name + "." + last + "@company.com"  # Attributes

        Employee.num_of_emps += 1

    def full_name(self):
        return f"{self.name} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # in case if we want override class variable (if we dont -> Employee.rase_amount)

# emp_1 -> instance of Employee class
emp_1 = Employee("Abylai", "Aitbanov", 177)
emp_2 = Employee("Bob", "Aitbanov", 299)

print(Employee.num_of_emps)


print(emp_1.raise_amount)

# emp_1.raise_amount = 1.05 # - > To override it we can do it
emp_1.apply_raise()
# print(emp_1.raise_amount)
# print(emp_1.__dict__)
print(emp_1.pay)