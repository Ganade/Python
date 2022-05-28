# Write a program that converts a temperature by typing in degrees Celsius and converts it to degrees Fahrenheit.

temperature = float(input("Enter a temperature in Celsius to be converted in Fahrenheit: ")) # read the temperature in celsius
Fahrenheit = temperature * 1.8 + 32     # calculates the temperature in fahrenheit
print(f"You typed {temperature}ºC and that temperature in fahrenheit will be {Fahrenheit}ºF")
