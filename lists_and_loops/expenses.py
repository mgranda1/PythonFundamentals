# Looping using range()
num_of_expenses = int(input("How many expenses? "))
expenses = []

for i in range(num_of_expenses):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)
print("Sum of the expenses is $", total, sep='')