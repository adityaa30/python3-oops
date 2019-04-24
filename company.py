from datetime import datetime


# Dunder methods: Methods with the format __<method name>__ (Double underscore = Dunder)

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
        # self.email = first + '.' + last + '@company.com'

        # Incrementing the count of each employee when the constructor is called
        # NOTE: We use <class name>.<class variable> syntax to acces the variable as we want the count_employee to be same in
        # all the instances
        Employee.count_employee += 1

    # Property decorator makes methods to be accesible like an attribute
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
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

    @staticmethod
    def is_workday(day):
        # Static method has similar logic as the class but does not have class instance as argument
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # Dunder methods
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        # Operator overriding -> addition (+)
        # Returs the total pay of the current & other employee
        return self.pay + other.pay


class Developer(Employee):
    """
    Class inheriting properties of Employee class
    """
    # Changing the raise amount only for developers. Thereby, only Developers will be affected
    # Not breaking any code in Employee class
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # Using parent's class constructor to initialize variables of parent class. (Clean code)
        # Employee.__init__(self, first, last, pay) also works
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    # Dunder methods
    def __repr__(self):
        return f"Developer('{self.first}', '{self.last}', {self.pay})"


class Manager(Employee):
    """
    Class inheriting properties of Employee class
    """

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print(f'-> {employee.fullname()}')

    # Dunder methods
    def __repr__(self):
        return f"Manager('{self.first}', '{self.last}', {self.pay})"


dev_1 = Developer('Aditya', 'Kumar', 12000, 'Python')
dev_2 = Developer('Test', 'Name', 10000, 'Java')

print(dev_1 + dev_2)
print(dev_1.email)
