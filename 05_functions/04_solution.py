import math
def area_and_circumference(radius):
   area = math.pi * radius ** 2
   circumference = 2 * math.pi * radius
   return area, circumference


a,c= area_and_circumference(5)

print("Area:", a, "\nCircumference:", c)