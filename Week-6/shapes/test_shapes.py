import pytest
from shapes import *

@pytest.fixture

def sample_rectangle():
    return Rectangle(Point(3, 3), Point(100, 100))


def test_rectangle_width_height_area(sample_rectangle):
    assert sample_rectangle.get_width() == 97
    assert sample_rectangle.get_height() == 97
    assert sample_rectangle.get_area() == 9409


def test_square(sample_rectangle):
    square = Square(Point(3, 3), 10)
    assert square.get_width() == 10
    assert square.get_height() == 10
    assert square.get_area() == 100


def test_box_volume():
    box = Box(Point(0, 0), Point(10, 10), 5)
    assert box.get_volume() == 500


def test_cube():
    cube = Cube(Point(0, 0), 5)
    assert cube.get_volume() == 125


def test_move_shape():
    rectangle = Rectangle(Point(3, 3), Point(100, 100))
    ShapeUtils.move_shape(rectangle, Point(-1, -1), Point(100, -30))
    assert rectangle.top_left.x == 2
    assert rectangle.top_left.y == 2
    assert rectangle.bottom_right.x == 200
    assert rectangle.bottom_right.y == 70

