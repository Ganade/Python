# Write a program that reads a value in meters and displays it converted to centimeters and millimeters.

meters = float(input("Enter a value in meter to be converted in centimeters and millimeters: "))
centimeter = meters * 100
millimeters = centimeter * 10
print(f"you typed {meters} meters, in centimeters this is equivalent to {centimeter} and in millimeters this is "
      f"equivalent to {millimeters}")