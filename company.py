class Employee:
    """
    Simple Class representing an Employee in any Company.
    Inputs basic details like first & last name, pay
    """

    # Declaring class variables
    count_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # Constructor function which is called automatically Employee object is instantiated
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Incrementing the count of each employee when the constructor is called
        # NOTE: We use <class name>.<class variable> syntax to acces the variable as we want the count_employee to be same in 
        # all the instances
        Employee.count_employee += 1 

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount  # Using self here as raise_amount may be different for different Employees

employee_1 = Employee('Aditya', 'Kumar', 10000)
employee_2 = Employee('Test', 'Name', 12000)

print(employee_1.fullname())
print(employee_2.fullname())

print(employee_1.count_employee)
print(Employee.count_employee)