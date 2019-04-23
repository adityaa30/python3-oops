class Employee:
    """
    Simple Class representing an Employee in any Company.
    Inputs basic details like first & last name, pay
    """
    def __init__(self, first, last, pay):
        # Constructor function which is called automatically Employee object is instantiated
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

employee_1 = Employee('Aditya', 'Kumar', 10000)
employee_2 = Employee('Test', 'Name', 12000)

print(employee_1.fullname())
print(employee_2.fullname())
