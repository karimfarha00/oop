# Question: Employee Management System
# Create a Python program that models an Employee Management System using inheritance.

# Requirements:
# Create a parent class Employee with:

# name (string)
# age (integer)
# salary (float)
# A method display_info() that prints the employee’s details.
# Create two child classes Manager and Developer that inherit from Employee:

# Manager should have an extra attribute department (string).
# Developer should have an extra attribute programming_language (string).
# Override display_info():

# The Manager class should display "Manager of [department]".
# The Developer class should display "Expert in [programming_language]".
# Create instances of both Manager and Developer and call display_info() for each.


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def display_info(self):
        print(f"Employee: {self.name}, Age: {self.age} , Salary: {self.salary}")
    
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
    def display_info(self):
        super().display_info()
        print(f"Manager:{self.department}")
    
class Developer(Employee):
    def __init__(self,name,age,salary,program_lang):
        super().__init__(name,age,salary)
        self.program_lang=program_lang
    
    def display_info(self):
        super().display_info()
        print(f"Expert in: {self.program_lang}")

manager=Manager("Karim",40,2000,"HR")

developer=Developer("Farah",20,6000,"Python")

manager.display_info()
print()
developer.display_info()
print()

    


   
        