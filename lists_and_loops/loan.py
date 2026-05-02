# Loan calculator
money_owed = float(input('How much money do you owe, in dollars?\n'))
apr = float(input('What is annual percentage rate of the loan? '))
payment = float(input('What is your montly payment? '))
months = int(input('For how many months? '))

montly_rate = apr/100/12
for i in range(months):
    # Calculate interest to pay
    interest_paid = money_owed*montly_rate

    # Add in interest
    money_owed += interest_paid
    if money_owed - payment < 0:
        print('Last payment was ', money_owed)
        print('You paid loan in', i+1, 'months')

    # Make payment
    money_owed -= payment
    print("Paid", payment, "of which", interest_paid, 'was interest', end='')
    print("Now I owe", money_owed)
   