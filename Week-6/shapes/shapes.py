class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def get_width(self):
        return self.bottom_right.x - self.top_left.x

    def get_height(self):
        return self.bottom_right.y - self.top_left.y

    def get_area(self):
        return self.get_width() * self.get_height()

    def __str__(self):
        return f"Rectangle({self.top_left},{self.bottom_right})"


class Square(Rectangle):
    def __init__(self, top_left, side_length):
        bottom_right = Point(top_left.x + side_length, top_left.y + side_length)
        super().__init__(top_left, bottom_right)


class Box(Rectangle):
    def __init__(self, top_left, bottom_right, height):
        self.height = height
        super().__init__(top_left, bottom_right)

    def get_volume(self):
        return self.get_area() * self.height


class Cube(Box):
    def __init__(self, top_left, side_length):
        super().__init__(top_left, Point(top_left.x + side_length, top_left.y + side_length), side_length)


class ShapeUtils:
    @staticmethod
    def move_shape(shape, top_left_shift, bottom_right_shift):
        shape.top_left.x += top_left_shift.x
        shape.top_left.y += top_left_shift.y
        shape.bottom_right.x += bottom_right_shift.x
        shape.bottom_right.y += bottom_right_shift.y
