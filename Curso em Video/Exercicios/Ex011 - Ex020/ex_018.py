"""
exercise 018 - Sine, Cosine and Tangent
"""
# Write a program that reads any angle and displays the sine, cosine and tangent of that angle on
# the screen.

from math import sin, cos, tan, radians

# reads an angle
ang = float(input("Enter an angle in degrees to calculate sine, cosine, and tangent: "))
# Transform the angle in radians
ang_rad = radians(ang)
# Calcutate the sine
sine = sin(ang_rad)
# Calculate the cosine
cosi = cos(ang_rad)
# Calculate the Tangent
tang = tan(ang_rad)
# Show the results
print(f"for angle {ang_rad} sine is {sine:.2f}, cosine is {cosi:.2f} and tangent is {tang:.2f}")
