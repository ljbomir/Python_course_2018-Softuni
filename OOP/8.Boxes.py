class Point:
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def measure_distance(self,other):
        x = abs(self.x - other.x)
        y = abs(self.y - other.y)
        return (x**2 + y**2) ** 0.5


class Box:
    def __init__(self, x, y, k, z):

        """"x = u l p ,
        y = u r p ,
        k = b l p ,
        z = b r p """

        self.x = x
        self.y = y
        self.k = k
        self.z = z
        self.width  = Point.measure_distance(self.x, self.y)
        self.height = Point.measure_distance(self.x, self.k)
        self.perimeter = self.width*2 + self.height*2
        self.area = self.width*self.height
        pass

data = input()
list_boxes = []

while data != "end":
    upper_left = data.split(" | ")[0]
    upper_right = data.split(" | ")[1]
    bottom_left = data.split(" | ")[2]
    bottom_right = data.split(" | ")[3]

    upper_left_point = Point((int(upper_left.split(":")[0])),(int(upper_left.split(":")[1])))
    upper_right_point = Point((int(upper_right.split(":")[0])),(int(upper_right.split(":")[1])))
    bottom_left_point  =  Point((int(bottom_left.split(":")[0])),(int(bottom_left.split(":")[1])))
    bottom_right_point =  Point((int(bottom_right.split(":")[0])),(int(bottom_right.split(":")[1])))

    myBox = Box(upper_left_point,upper_right_point,bottom_left_point,bottom_right_point)
    list_boxes.append(myBox)

    data = input()

for box in list_boxes:
    print(f"Box: {int(box.width)}, {int(box.height)}")
    print(f"Perimeter: {int(box.perimeter)}")
    print(f"Area: {int(box.area)}")


