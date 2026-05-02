# Exploring classes
from employee import Employee, SalaryEmployee, HourlyEmployee, ComissionEmployee

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print("Current employees:")
        for e in self.employees:
            print(f"\t{e.fname} {e.lname}")
        print("\n")


    def pay_employees(self):
        for e in self.employees:
            print(f"Paycheck for {e.fname} {e.lname}")
            print(f"Amount: ${e.calculate_paycheck():,.2f}")
            print("------------------")

def main():
    my_company = Company()

    employee1 = SalaryEmployee("Ari", "Gun", 10400)
    my_company.add_employee(employee1)

    employee2 = HourlyEmployee("Ted", "Donut", 40, 50)
    my_company.add_employee(employee2)

    employee3 = ComissionEmployee("Ross", "Ball", 25000, 10, 10)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()