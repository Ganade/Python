# Write a program that reads a value in meters and displays it converted to centimeters and millimeters.

meters = float(input("Enter a value in meter to be converted in centimeters and millimeters: "))      # reads the value in metters
centimeter = meters * 100     # convert the value from meters to centimeters
millimeters = centimeter * 10       # convert the value from centimeters to millimeters
print(f"you typed {meters} meters, in centimeters this is equivalent to {centimeter} and in millimeters this is "
      f"equivalent to {millimeters}")