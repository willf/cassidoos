from itertools import takewhile, product
import numpy as np

## TODO : THIS IS ALL WRONG !!!


def trues(iterable):
    """
    Given an iterable, all the truthy values are returned.
    >>> list(trues([1, 0, None, '', [], {}, False]))
    [1]
    """
    return filter(None, iterable)


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


def is_one_at(point, array):
    """
    Given a point and a 2D array, return True if the point is a 1 in the array.
    """
    return value_at(point, array) == 1


def iter_len(iterable):
    """
    Given an iterable, return the length of the iterable.
    >>> iter_len(range(5))
    5
    >>> iter_len(())
    0
    """
    return sum(1 for _ in iterable)


def points_right(point, array):
    """
    from a point, return all points to the right the point (including the point).
    >>> list(points_right((0, 0), np.array([[1, 2, 3], [4, 5, 6]])))
    [(0, 0), (0, 1), (0, 2)]
    """
    return ((row(point), c) for c in range(col(point), col(array.shape)))


def points_down(point, array):
    """
    from a point, return all points below the point (including the point).
    >>> list(points_down((0, 0), np.array([[1, 2, 3], [4, 5, 6]])))
    [(0, 0), (1, 0)]
    """
    return ((r, col(point)) for r in range(row(point), row(array.shape)))


def points_down_right(point, array):
    """
    Given a point in the array, return all points to the right and below the point (including the point).
    >>> list(points_down_right((0, 0), np.zeros((6,10))))
    [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    >>> list(points_down_right((2, 3), np.zeros((6,10))))
    [(2, 3), (3, 4), (4, 5), (5, 6)]
    """
    return zip(
        [row(p) for p in points_down(point, array)],
        [col(p) for p in points_right(point, array)],
    )


def one_points(points, array):
    """
  Given a list of points and a 2D array, take all points in the list that have value 1 in the array
  until you hit a zero
  >>> list(one_points([(0,0), (1,1), (2,2)], np.ones((10,10))))
  [(0, 0), (1, 1), (2, 2)]
  >>> list(one_points([(0,0), (1,1), (2,2)], np.zeros((10,10))))
  []
  >>> list(one_points([(0,0), (1,1), (2,2)], np.array([[1, 1, 1], [1, 1, 1], [0, 0, 0]])))
  [(0, 0), (1, 1)]
  """
    return takewhile(lambda p: value_at(p, array) == 1, points,)


def one_retangle_shape(point, array):
    """
    Given a row and column in the array, find the shape of the rectangle of 1s.
    """
    return (
        iter_len(one_points(points_down(point, array), array)),
        iter_len(one_points(points_right(point, array), array)),
    )


def rectangular_extensions(point, array):
    """
    Given a point in the array, get rectangles of 1s that extend from the point.
    """
    return trues(
        (
            one_right_extension(start_point, current_end, array)
            # + right_extension(start_point, current_end, array)
            # + square_extension(start_point, current_end, array)
        )
    )


def area_from_shape(shape):
    """
    Given a shape, return the area of the shape.
    >>> area_from_shape((2, 3))
    6
    """
    return row(shape) * col(shape)


def points(array):
    """
    Return all points in the 2d array.
    >>> list(points(np.array([[1, 2, 3], [4, 5, 6]])))
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
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
    >>> islands = np.array([0,0,0,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0]).reshape(4,5)
    >>> islands
    array([[0, 0, 0, 1, 0],
           [1, 1, 0, 0, 1],
           [1, 1, 0, 0, 0],
           [0, 0, 1, 0, 0]])
    >>> largest_rectangle(islands)
    (2, 2)
    >>> largest_rectangle(np.zeros((5,10)))
    (0, 0)
    >>> largest_rectangle(np.ones((5,10)))
    (5, 10)
    >>> a24 = np.array([1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1])
    >>> a24.reshape(8,3)
    array([[1, 1, 0],
           [1, 1, 0],
           [1, 0, 1],
           [1, 0, 1],
           [0, 1, 1],
           [0, 0, 1],
           [1, 0, 0],
           [1, 0, 1]])
    >>> largest_rectangle(a24.reshape(8, 3))
    (1, 3)
    >>> largest_rectangle(a24.reshape(4, 6))
    (1, 2)
    >>> largest_rectangle(a24.reshape(6, 4))
    (2, 2)
    >>> a60 = np.array([[1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1]])
    >>> a60.reshape(6, 10)
    array([[1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
           [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
           [1, 1, 0, 1, 0, 0, 0, 1, 1, 1],
           [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
           [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
           [1, 1, 1, 0, 0, 1, 0, 1, 0, 1]])
    >>> largest_rectangle(a60.reshape(6, 10))
    (2, 3)
    >>> area_from_shape(largest_rectangle(a60.reshape(10, 6)))
    3
    """
    return max(rectangle_shapes(array), key=area_from_shape, default=(0, 0))


def extensions(point, array):
    """
    Given a point in the array, get rectangles of 1s that extend from the point.
    """
    keepers = []
    r, c = point
    slice = array[r : c + 1, r : c + 1]
    print("slice", slice)
    stack = [slice]
    print("stack is", stack)
    if stack:
        print("there is a stack")
    else:
        print("there is no stack")
    while stack:
        current_slice = stack.pop()
        print(current_slice)
        if current_slice.all():
            keepers.append(current_slice)
            (row_, col_) = current_slice.shape
            print("row_, col_", row_, col_)
            if c + col_ + 1 < array.shape[1]:
                stack.append(array[r + row_ : c + col_, r + row_ : c + col_ + 1])
            # if row(point) + 2 < row_:
            #     stack.append(
            #         array[
            #             row(point) + 1 : col(point) + 2, row(point) + 1 : col(point) + 1
            #         ]
            #     )
            # if col(point) + 2 < col_ and row(point) + 2 < row_:
            #     stack.append(
            #         array[
            #             row(point) + 1 : col(point) + 2, row(point) + 1 : col(point) + 2
            #         ]
            #     )
    print("no more stack")
    return keepers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
