# Classes for employee.py
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary / 52
    
class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate
    
    def calculate_paycheck(self):
        return self.weekly_hours * self.hourly_rate
    
class ComissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_number, com_rate):
        super().__init__(fname, lname, salary)
        self.sales_number = sales_number
        self.com_rate = com_rate

    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commission = self.sales_number*self.com_rate
        return regular_salary + total_commission