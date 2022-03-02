from itertools import takewhile, product
import numpy as np
import string

# used for doc testing
def letters_25():
    """
    >>> letters_25()
    array([['A', 'B', 'C', 'D', 'E'],
           ['F', 'G', 'H', 'I', 'J'],
           ['K', 'L', 'M', 'N', 'O'],
           ['P', 'Q', 'R', 'S', 'T'],
           ['U', 'W', 'X', 'Y', 'Z']], dtype='<U1')
    """
    return np.array(sorted(set(string.ascii_uppercase).difference("V"))).reshape(5, 5)


def row(point):
    """
    Given a point, return the row of the point.
    >>> row((0, 1))
    0
    >>> row((1, 0))
    1
    """
    return point[0]


def width(array):
    return array.shape[1]


def height(array):
    return array.shape[0]


def col(point):
    """
    Given a point, return the column of the point.
    >>> col((0, 1))
    1
    >>> col((1, 0))
    0
    """
    return point[1]


# used for doc testing
def value_at(point, array):
    """
    Given a point and a 2D array, return the value at the point.
    >>> value_at((0, 0), np.array([[1, 2, 3], [4, 5, 6]]))
    1
    """
    return array[row(point), col(point)]


def area_from_shape(shape):
    """
    Given a shape, return the area of the shape.
    >>> area_from_shape((2, 3))
    6
    """
    return row(shape) * col(shape)


def area(array):
    """
    Given a 2D array, return the area of the array.
    >>> area(np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    9
    """
    return area_from_shape(array.shape)


def points(array):
    """
    Return all points in the 2d array.
    >>> list(points(np.array([[1, 2, 3], [4, 5, 6]])))
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
    """
    return product(range(array.shape[0]), range(array.shape[1]))


def can_extend_right(base, p, slice):
    """
    Given a slice of an array starting at point p, return whether the slice can be extended to the right.
    >>> arr = letters_25()
    >>> point = (2,4)
    >>> value_at(point, arr)
    'O'
    >>> can_extend_right(arr, point, arr[2:4, 4:5])
    False
    >>> can_extend_right(arr, (2,3), arr[2:4, 3:4])
    True
    """
    return col(p) + width(slice) < width(base)


def can_extend_down(base, p, slice):
    """
    Given a slice of an array starting at point p, return whether the slice can be extended downwards.
    >>> arr = letters_25()
    >>> point = (2,4)
    >>> value_at(point, arr)
    'O'
    >>> can_extend_down(arr, point, arr[2:5, 4:5])
    False
    >>> can_extend_down(arr, point, arr[2:4, 4:5])
    True
    """
    return row(p) + height(slice) < height(base)


def extend_right(base, p, slice):
    """
    Given a slice of an array starting at point p, return the slice extended to the right.
    >>> arr = letters_25()
    >>> point = (2,4)
    >>> value_at(point, arr)
    'O'
    >>> extend_right(arr, point, arr[2:4, 4:5])
    >>> extend_right(arr, (2,3), arr[2:4, 3:4])
    array([['N', 'O'],
           ['S', 'T']], dtype='<U1')
    """
    if not can_extend_right(base, p, slice):
        return None
    return base[row(p) : row(p) + height(slice), col(p) : col(p) + width(slice) + 1]


def extend_down(base, p, slice):
    """
    Given a slice of an array starting at point p, return the slice extended downwards.
    >>> arr = letters_25()
    >>> point = (2,4)
    >>> value_at(point, arr)
    'O'
    >>> extend_down(arr, point, arr[2:5, 4:5])
    >>> extend_down(arr, point, arr[2:4, 4:5])
    array([['O'],
           ['T'],
           ['Z']], dtype='<U1')
    """
    if not can_extend_down(base, p, slice):
        return None
    return base[row(p) : row(p) + height(slice) + 1, col(p) : col(p) + width(slice)]


def extend_diagonally(base, p, slice):
    """
    Given a slice of an array starting at point p, return the slice extended diagonally.
    >>> arr = letters_25()
    >>> point = (2,4)
    >>> value_at(point, arr)
    'O'
    >>> extend_diagonally(arr, point, arr[2:5, 4:5])
    >>> extend_diagonally(arr, (2,2), arr[2:4, 2:4])
    array([['M', 'N', 'O'],
           ['R', 'S', 'T'],
           ['X', 'Y', 'Z']], dtype='<U1')
    """
    if not (can_extend_down(base, p, slice) and can_extend_right(base, p, slice)):
        return None
    return base[row(p) : row(p) + height(slice) + 1, col(p) : col(p) + width(slice) + 1]


def point_to_slice(base, p):
    """
    Given a point in the array, return the slice of the array that extends from the point.
    >>> arr = letters_25()
    >>> point = (2,3)
    >>> value_at(point, arr)
    'N'
    >>> point_to_slice(arr, point)
    array([['N']], dtype='<U1')
    """
    return base[row(p) : row(p) + 1, col(p) : col(p) + 1]


def all_ones(slice):
    """
    Given a slice of an array, return whether the slice is all ones.
    >>> arr = np.ones((3,3))
    >>> all_ones(arr[:,:])
    True
    >>> arr = np.zeros((3,3))
    >>> all_ones(arr[:,:])
    False
    """
    return slice.all()


def array_to_point_slices(base):
    """
    generate a list of (point, point slice) for every point in the base array.
    """
    return ((p, point_to_slice(base, p)) for p in points(base))


def rectangles_of_one(base):
    """
    Given a base array, generate list of all (point, rectangle) where the rectangle is all ones.

    """
    stack = []
    for p, slice in array_to_point_slices(base):
        stack.append((p, slice))
    while stack:
        p, slice = stack.pop()
        if all_ones(slice):
            yield p, slice
        if can_extend_right(base, p, slice):
            stack.append((p, extend_right(base, p, slice)))
        if can_extend_down(base, p, slice):
            stack.append((p, extend_down(base, p, slice)))
        if can_extend_right(base, p, slice) and can_extend_down(base, p, slice):
            stack.append((p, extend_diagonally(base, p, slice)))


def max_point_and_rectangle_of_one(base):
    """
    Given a base array, return the largest rectangle of one and its point.
    >>> max_point_and_rectangle_of_one(np.ones((3,3)))[1].shape
    (3, 3)
    >>> max_point_and_rectangle_of_one(np.zeros((3,3)))[1].shape
    (0, 0)
    
    """
    return max(
        rectangles_of_one(base),
        key=lambda pair: area(pair[1]),
        default=(None, np.ones((0, 0))),
    )


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
    >>> area_from_shape(largest_rectangle(a24.reshape(8, 3)))
    4
    >>> area_from_shape(largest_rectangle(a24.reshape(4, 6)))
    3
    >>> area_from_shape(largest_rectangle(a24.reshape(6, 4)))
    4
    >>> a60 = np.array([[1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1]])
    >>> a60.reshape(6, 10)
    array([[1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
           [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
           [1, 1, 0, 1, 0, 0, 0, 1, 1, 1],
           [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
           [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
           [1, 1, 1, 0, 0, 1, 0, 1, 0, 1]])
    >>> area_from_shape(largest_rectangle(a60.reshape(6, 10)))
    6
    >>> area_from_shape(largest_rectangle(a60.reshape(10, 6)))
    4
    """
    return max_point_and_rectangle_of_one(array)[1].shape


if __name__ == "__main__":
    import doctest

    doctest.testmod()
