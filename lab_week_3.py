name_list = {'Ram', 'Shyam', 'Hari'}

def greet_friends(names):
    for name in names:
        print('Hello', name, '!')

greet_friends(name_list)

# Task Tax Calculation

def calculate_tax(income, tax_rate):
    tax_amount = float(income * tax_rate)
    print('Total Income tax is', tax_amount)

calculate_tax(50000, 0.2)

        
        
