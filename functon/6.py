#6.Define a function to calculate the area of a circle using its radius.

def circle_area(radius):
    return 3.14159 * radius * radius

r = float(input("Enter the radius of the circle: "))
print(f"Area of the circle = {circle_area(r)}")