var_1 = True # Type = bool
var_2 = 1 # Type = int
var_3 = 3.14159 # Type = float
var_4 = "Hello World" # Type = str

print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

my_int = 5
my_float = 5.5
my_bool = True

print(my_int)
print(my_float)
print(my_bool)

my_int_float = float(my_int)
my_float_int = int(my_float)
my_bool_int = int(my_bool)

print(my_int_float)
print(my_float_int)
print(my_bool_int)

#Addition
result_addition = 10 + 5
print("Addition:", result_addition)
#Subtraction
result_subtraction = 20 - 8
print("Subtraction:", result_subtraction)
#Multiplication
result_multiplication = 6 * 4
print("Multiplication:", result_multiplication)
#Division
result_division = 15 / 3
print("Division:", result_division)
#Floor Division
result_floor_division = 17 // 4
print("Floor Division:", result_floor_division)
#Modulus
result_modulus = 17 % 4
print("Modulus:", result_modulus)
#Exponentiation
result_exponentiation = 2 ** 3
print("Exponentiation:", result_exponentiation)

num1 = 4
num2 = 9
average = float((num1 + num2)/2)
print("The average of ", num1, "and ", num2, "is ", average)

# Calculate the Area of a Rectangle
length = 12
width = 6
# Formula for area of rectangle 
area = length * width
# Printing out area of the rectangle with value of length and width
print("The area of rectangle having length:", length, "&", width, "is", area)

# Modify Strings
my_string = "This class covers OOP"
print(my_string)

my_uppercase_string = my_string.upper()
my_lowercase_string = my_string.lower()
my_new_string = my_string.replace("OOP", "Object Oriented Programming")
my_string_length = len(my_string)

# Task with f strings
my_name = "Sanjiv Shrestha"
number_of_classes = 3
campus = "University of the West of Scotland, London Campus"
# Using f strings to print out variables
my_text = f"My name is {my_name} and I am studying {number_of_classes} classes in {campus}"
print(my_text)
