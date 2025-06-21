print("----------------------------------------------------")
# Comparison and Conditionals
# Comparison Operators
x = 7
y = 2

# equal operator
print(x == y)

# not equal operator
print(x != y)

# grater than operator
print(x > y)

# smaller than operator
print(x < y)

# greater than or equal to	
print(x >= y)

# smaller than or equal to	
print(x <= y)
print("----------------------------------------------------")
# Logical Operators
x = 8

# and operator
print(x > 5 and x < 9)

# or operator
print(x > 5 or x < 9)

# not operator
print(not(x > 5 and x < 9))
print("----------------------------------------------------")
# If Conditional

age = 19    #15
age_group = "child"
if age > 18:
        age_group = "adult"
        print(f"The age group is {age_group}")

# If else conditionals

wind_speed = 30 # 5
if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")

# If elif else conditionals

grade = 55 # 47 68 73
if grade < 50:
    print("You failed")
elif grade < 60:
    print("You passed")
elif grade < 70:
    print("You got a good pass")
else:
    print("You got an excellent pass")
print("----------------------------------------------------")
# Summary Tasks
temperature1 = 56
temperature2 = 27
if temperature1 == temperature2:
     print("Temperature 1 and Temperature 2 are same.")
else:
     print("Temperature 1 and Temperature 2 are not same.")
print("----------------------------------------------------")
# Python Lists
# 1. Creating a list
city_list = ["Glasgow", "London", "Edinburgh"]

# 2. Accessing a List
print(city_list[2])
print(city_list[1:3])

# 3. Modifying a List
city_list.append("Manchester")
city_list[1] = "Birmingham"
print("----------------------------------------------------")
# 4. Summary Task
colours = ["Purple", "Magenta", "Yellow"]
print(colours)

select_color = colours[1]
print(select_color)

colours[0] = "Cyan"
print(colours)
print(len(colours))

if "red" in colours:
    print("Red is in the list")

selected_color = colours[1:3]
print(selected_color)

print("----------------------------------------------------")
# Python Loops
# 1. While Loops

# 2. For Loops
for city in city_list:
    print(city)

# 3. Loop Keywords: Range, Break and continue
for i in range(4):
    if i == 3:
        break
    print(i)
print("----------------------------------------------------")
# 4. Summary Tasks
# Even Numbers
numbers = list(range(1, 11))
print(numbers)
for num in numbers:
    if num % 2 == 0:
        print(num)
print("----------------------------------------------------")
# Sum of Squares
sum_of_squares = 0
for num in list(range(1,6)):
    sum_of_squares += num ** 2
print(sum_of_squares)
print("----------------------------------------------------")
# Countdown
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("lift off!")
print("----------------------------------------------------")
# Obtain User Input
# User Input and Conditional Statements
age = int(input('Enter your Age:'))
if age < 18:
    print("You are a minor.")
elif age < 65:  
    print("You are an adult.")
else:
    print("You are a senior citizen.")
print("----------------------------------------------------")
# Temprerature Convertor
celsius_input = float(input("Enter the value of temperature in Celsius:"))
print("The temperature you have entered is", celsius_input, "degree celsius")

print("What temperature you want to convert?")
print("1. Fahrenheit")
print("2. Kelvin")
print("3. Both")
input_choice = input("Enter your choice (1/2/3): ")
if input_choice not in ['1', '2', '3']:
    print("Invalid choice. Please enter 1, 2, or 3.")
    exit()
elif input_choice == '1':
    degree_f = float(((celsius_input * 9)/5) + 32)
    print(celsius_input, "degree Celsius is equal to", degree_f, "Fahrenheit")
elif input_choice == '2':
    degree_k = float(celsius_input + 273.15)
    print(celsius_input, "degree Celsius is equal to", degree_k, "Kelvin")
elif input_choice == '3':
    degree_f = float(((celsius_input * 9)/5) + 32)
    print(celsius_input, "degree Celsius is equal to", degree_f, "Fahrenheit")
    degree_k = float(celsius_input + 273.15)
    print(celsius_input, "degree Celsius is equal to", degree_k, "Kelvin")
print("----------------------------------------------------")
