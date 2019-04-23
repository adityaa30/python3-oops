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
        # Using self here as raise_amount may be different for different Employees
        self.pay = self.pay * self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        # Class method which changes the values of a class variable which is reflected in all the instances
        # By convention, it should be called by the class itself (not the instance)
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_string):
        # Alternative classmethod constructor to create instance by extracting details from a string
        first, last, pay = employee_string.split('-')
        return cls(first, last, int(pay))


employee_1 = Employee('Test', 'Name', 12000)
employee_2 = Employee.from_string('Aditya-Kumar-10000')

print(employee_1.fullname())
print(employee_2.fullname())
