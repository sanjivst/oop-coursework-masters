# Printing list of names
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

# Compound Interest
def compound_interest(principal, interest_rate, duration):
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None
    if duration < 0:
        print("Please enter a positive number of years")
        return None
    for i in range(1, duration + 1):
        investment_value = principal * (1 + interest_rate) ** i
        print(f"The total amount of money earned by the investment is {int(investment_value)} £")
        return investment_value

compound_interest_amount = compound_interest(1000, 0.5, 1)
print(compound_interest_amount)

# Assertion and Errors
# Syntax Error
print("Hello, World!") 

# Name Error
favorite_color = "blue"
print("My favorite color is", favorite_color) 

# Value Error
number1 = 5
number2 = 3 
result = number1 + number2 
print("The sum is:", result) 

# Index Error
fruits = ["apple", "banana", "cherry"] 
print(fruits[2]) 

# Indentation Error
time = 11 
if time < 12: 
    print("Good morning!")  
        
        
