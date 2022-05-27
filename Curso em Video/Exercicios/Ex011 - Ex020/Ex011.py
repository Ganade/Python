# Write a program that reads the width and height of a wall in meters, calculates its area and the amount of paint
# needed to paint it, knowing that each liter of paint paints an area of 2 square meters.

width = float(input("Enter the width of the wall to be painted: "))     # read the width of the wall
height = float(input("Enter the height of the wall to be painted: "))   # read the height of the wall
area = width * height   # calculate the area of the wall
print(f"For the wall with the dimensions {width:.3} x {height:.3} meters, you will have an area of {area:.3} and will "
      f"need {area/2:.3} liters of paint")

