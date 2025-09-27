import math
import pytest
from geometry.shapes import Circle, Triangle


def test_circle_area():
    c = Circle(1)
    assert math.isclose(c.area(), math.pi, rel_tol=1e-9)


def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(0)


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0, rel_tol=1e-9)


def test_triangle_invalid_sides():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)


def test_triangle_is_right():
    t = Triangle(3, 4, 5)
    assert t.is_right()
    t2 = Triangle(2, 3, 4)
    assert not t2.is_right()