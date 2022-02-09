# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

cel = float(input('Enter Celsius Temperature: '))
fer = cel * 9 / 5 + 32

print('Fahrenheit Temperature: ', fer)