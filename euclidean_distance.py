points = []
num_points = int(input("Enter the number of points: "))

for i in range(num_points):
    x = float(input(f"Enter x coordinate for point {i+1}: "))
    y = float(input(f"Enter y coordinate for point {i+1}: "))
    points.append((x, y))

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)
print(f"The minimum Euclidean distance is: {min_distance}")
