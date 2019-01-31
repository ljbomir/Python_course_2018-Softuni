import math


class Point:
   def __init__(self,x,y):
       self.x = x
       self.y = y


def calc_distance(a,b):
    c = math.sqrt(a**2 + b**2)
    return c


data = list(map(float, input().split()))
first_point = Point(data[0],data[1])

data = list(map(float, input().split()))
second_point = Point(data[0],data[1])

side_a = abs(first_point.x - second_point.x)
side_b = abs(first_point.y - second_point.y)

side_c = calc_distance(side_a, side_b)

print(f"{side_c:.3f}")
