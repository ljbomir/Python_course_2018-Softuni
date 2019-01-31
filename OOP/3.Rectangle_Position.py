class Rectangle:
    def __init__(self,left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.right = self.left + self.width
        self.bottom = self.top + self.height


    def is_inside(self, other):
        if  self.left >= other.left \
            and self.right <= other.right \
            and self.top >= other.top  \
            and self.bottom <= other.bottom:

            return "Inside"
        else:
            return "Not inside"


data = list(map(int, input().split()))
r1 = Rectangle(data[0],data[1],data[2],data[3])

data = list(map(int, input().split()))
r2 = Rectangle(data[0],data[1],data[2],data[3])

print(r1.is_inside(r2))

