# Exercise 1: Temperature Converter
    #Create a program that converts temperatures between Celsius and Fahrenheit.
        #Instructions:
            #1.	Ask the user to input a temperature.
            #2.	Ask the user to select the conversion type: from Celsius to Fahrenheit or from Fahrenheit to Celsius.
            #3.	Perform the appropriate conversion and print the result.


print('='*30)
print("Welcome to Temperature Converter!\n")

# Ask the user to input a temperature.
initial_temperature = float(input('Enter temperature: '))

# Ask the user to select the conversion type: from Celsius to Fahrenheit or from Fahrenheit to Celsius.
print('CONVERSION TYPE\n')
conversion_type = int(input(f"1. Celcius to Fahrenheit \n"
                      f"2. Fahrenheit to Celcius\n"
                      f"Enter here: "))
# Perform the appropriate conversion
# Display result
