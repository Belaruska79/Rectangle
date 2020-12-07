class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area (self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a**2

class Circle:
    def __init__(self,a):
        self.a = a
    def get_area_circle(self):
        return self.a**2*3.14


rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),square_2.get_area_square())

circle_1 = Circle(5)
print(circle_1.get_area_circle())


figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())
