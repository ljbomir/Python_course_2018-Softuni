class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        sa = self.x - other.x
        sb = self.y - other.y
        c = float((sa**2 + sb**2)**0.5)
        return c


n = int(input())
points = []
distances = {}

for item in range(n):
    data = list(map(int, input().split()))
    mypoint = Point(x=data[0], y=data[1])
    points.append(mypoint)

for i in range(0, len(points)):
        j = i+1
        for j in range(j, len(points)):
            dist = points[i].distance(points[j])
            distances[dist] = ((points[i].x,points[i].y),(points[j].x, points[j].y))


sorted_points = sorted(distances.items(), key=lambda x: x[0])

abc = [x for x in sorted_points]
print(abc)
print(f"{sorted_points[0][0]:.3f}")
print(f"{(sorted_points[0][1][0])}")
print(f"{(sorted_points[0][1][1])}")



