
expense = {}
phone = float(input('Phone monthly installment: $'))
rent = float(input('Rent monthly installment: $'))
electric = float(input('Electric monthly installment: $'))
expense['phone'] = phone
expense['rent'] = rent
expense['electric'] = electric
total_expense = sum(expense.values())

income = {}
job = float(input('What is your primary income: $'))
side_hustle_1 = float(input('What is your side income: $'))
side_hustle_2 = float(input('What is your side income: $'))
income['job'] = job
income['side_hustle_1'] = side_hustle_1
income['side_hustle_2'] = side_hustle_2
total_income = sum(income.values())

print('Your monthly budget is', '$',total_income - total_expense)
