# Python program for for converting temperatures from Celsius to Fahrenheit and Kelvin
print("Welcome to the Temperature Converter!")

celsius_input = float(input("Enter the value of temperature in Celsius:"))
print("The temperature you have entered is", celsius_input, "degree celsius")

degree_f = float(((celsius_input * 9)/5) + 32)
degree_k = float(celsius_input + 273.15)

print("Converted Temperatures:")
print(celsius_input, "degree Celsius is equal to", degree_f, "Fahrenheit")
print(celsius_input, "degree Celsius is equal to", degree_k, "Kelvin")