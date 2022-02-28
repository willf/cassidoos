from itertools import count as iota
from itertools import takewhile, product
import numpy as np


def row(point):
    """
    Given a point, return the row of the point.
    >>> row((0, 1))
    0
    >>> row((1, 0))
    1
    """
    return point[0]


def col(point):
    """
    Given a point, return the column of the point.
    >>> col((0, 1))
    1
    >>> col((1, 0))
    0
    """
    return point[1]


def value_at(point, array):
    """
    Given a point and a 2D array, return the value at the point.
    >>> value_at((0, 0), np.array([[1, 2, 3], [4, 5, 6]]))
    1
    """
    return array[row(point), col(point)]


def iter_len(iterable):
    """
    Given an iterable, return the length of the iterable.
    >>> iter_len(range(5))
    5
    >>> iter_len(())
    0
    """
    return sum(1 for _ in iterable)


def points_left(point, array):
    """
    from a point, return all points to the left of the point (including the point).
    """
    return (
        (row(point), c)
        for c in takewhile(lambda n: n < col(array.shape), iota(col(point)),)
    )


def one_points_left(point, array):
    """
    Given a point in the array, return all points to the left of the point (including the point)
    that have value 1
    """
    return takewhile(
        lambda point: value_at(point, array) == 1, points_left(point, array)
    )


def points_down(point, array):
    """
    from a point, return all points below the point (including the point).
    """
    return (
        (r, col(point))
        for r in takewhile(lambda n: n < row(array.shape), iota(row(point)),)
    )


def one_points_down(point, array):
    """
    Given a point in the array, return all points below of the point (including the point)
    that have value 1
    """
    return takewhile(
        lambda point: value_at(point, array) == 1, points_down(point, array)
    )


def one_retangle_shape(point, array):
    """
    Given a row and column in the array, find the shape of the rectangle of 1s.
    """
    return (
        iter_len(one_points_left(point, array)),
        iter_len(one_points_down(point, array)),
    )


def area_from_shape(shape):
    return row(shape) * col(shape)


def points(array):
    """
    Return all points in the 2d array.
    """
    return product(range(array.shape[0]), range(array.shape[1]))


def rectangle_shapes(array):
    """
    Given a 2D array of 0s and 1s, return the shapes of all rectangles of 1s in the array.
    """
    return (one_retangle_shape(point, array) for point in points(array))


def largest_rectangle(array):
    """
    Given a 2D array of 0s and 1s, return the size of the largest rectangle of 1s in the array.
    Example (javascript version):
    let islands = [
    0,0,0,1,0
    1,1,0,0,1
    1,1,0,0,0
    0,0,1,0,0
    ]

    $ largestRect(islands)
    $ '2x2'
    >>> import numpy as np
    >>> islands = np.array([0,0,0,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0]).reshape(4,5)
    >>> islands
    array([[0, 0, 0, 1, 0],
           [1, 1, 0, 0, 1],
           [1, 1, 0, 0, 0],
           [0, 0, 1, 0, 0]])
    >>> largest_rectangle(islands)
    (2, 2)
    >>> largest_rectangle(np.zeros((10,10)))
    (0, 0)
    >>> largest_rectangle(np.ones((10,10)))
    (10, 10)
    """
    return max(rectangle_shapes(array), key=area_from_shape, default=(0, 0))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
