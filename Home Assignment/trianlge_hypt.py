#Program to find out the hypotenous of triangle

#from math import sqrt
import math
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))

c = math.sqrt(a**2 + b**2)
print("The length of the hypotenuse is", c )
