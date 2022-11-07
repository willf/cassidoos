# Anti-divisor formula

# Given an integer n, then its anti-divisors can be generated from the numbers 2n-1, 2n and 2n+1.
#
# For example 20 creates the numbers 39,40 and 41.
# The odd anti-divisors are therefore 3 and 13.
# The only odd divisor of 40 is 5, hence the only even anti-divisor of 20 is 8.
# The anti-divisors of 20 are therefore 3, 8 and 13.


def divisors(n):
    """
    Return a list of divisors of n, greater than 1
    >>> divisors(1)
    []
    >>> divisors(2)
    [2]
    >>> divisors(3)
    [3]
    >>> divisors(4)
    [2, 4]
    >>> divisors(5)
    [5]
    >>> divisors(6)
    [2, 3, 6]
    """
    return [i for i in range(2, n+1) if n % i == 0]

def odd_divisors(n):
    """ Return a list of odd divisors of n.
    >>> odd_divisors(1)
    []
    >>> odd_divisors(2)
    []
    >>> odd_divisors(3)
    [3]
    >>> odd_divisors(4)
    []
    >>> odd_divisors(5)
    [5]
    >>> odd_divisors(6)
    [3]
    """
    return [i for i in divisors(n) if i % 2 == 1]

# The divisors of 2n-1 and 2n+1 are the odd anti-divisors of n.
def odd_anti_divisors(n):
    """
    Return a list of odd anti-divisors of n.
    The divisors of 2n-1 and 2n+1 are the odd anti-divisors of n.
    >>> odd_anti_divisors(20)
    [3, 13]
    """
    return [d for d in divisors(2*n-1) +  divisors(2*n+1) if d < n]
# The even anti-divisors come from 2n. Find odd divisors of 2n, say r, then 2n/r is an even anti-divisor of n.
def even_anti_divisors(n):
    """
    Return a list of even anti-divisors of n.
    The even anti-divisors come from 2n. Find odd divisors of 2n, say r, then 2n/r is an even anti-divisor of n.
    >>> even_anti_divisors(20)
    [8]
    """
    return [2*n // r for r in odd_divisors(2*n) if 2*n // r < n]

def anti_divisors(n):
    """
    Return a list of anti-divisors of n.

    >>> anti_divisors(20)
    [3, 8, 13]

    """
    return sorted(odd_anti_divisors(n) + even_anti_divisors(n))

def table_test():
    """
    >>> anti_divisors(2)
    []
    >>> anti_divisors(3)
    [2]
    >>> anti_divisors(4)
    [3]
    >>> anti_divisors(5)
    [2, 3]
    >>> anti_divisors(6)
    [4]
    >>> anti_divisors(7)
    [2, 3, 5]
    >>> anti_divisors(8)
    [3, 5]
    >>> anti_divisors(9)
    [2, 6]
    >>> anti_divisors(10)
    [3, 4, 7]
    >>> anti_divisors(11)
    [2, 3, 7]
    >>> anti_divisors(12)
    [5, 8]
    >>> anti_divisors(13)
    [2, 3, 5, 9]
    >>> anti_divisors(14)
    [3, 4, 9]
    >>> anti_divisors(15)
    [2, 6, 10]
    >>> anti_divisors(16)
    [3, 11]
    >>> anti_divisors(17)
    [2, 3, 5, 7, 11]
    >>> anti_divisors(18)
    [4, 5, 7, 12]
    >>> anti_divisors(19)
    [2, 3, 13]
    >>> anti_divisors(20)
    [3, 8, 13]
    >>> anti_divisors(21)
    [2, 6, 14]
    >>> anti_divisors(22)
    [3, 4, 5, 9, 15]
    >>> anti_divisors(23)
    [2, 3, 5, 9, 15]
    >>> anti_divisors(24)
    [7, 16]
    >>> anti_divisors(25)
    [2, 3, 7, 10, 17]
    >>> anti_divisors(26)
    [3, 4, 17]
    >>> anti_divisors(27)
    [2, 5, 6, 11, 18]
    >>> anti_divisors(28)
    [3, 5, 8, 11, 19]
    >>> anti_divisors(29)
    [2, 3, 19]
    >>> anti_divisors(30)
    [4, 12, 20]
    >>> anti_divisors(31)
    [2, 3, 7, 9, 21]
    >>> anti_divisors(32)
    [3, 5, 7, 9, 13, 21]
    >>> anti_divisors(33)
    [2, 5, 6, 13, 22]
    >>> anti_divisors(34)
    [3, 4, 23]
    >>> anti_divisors(35)
    [2, 3, 10, 14, 23]
    >>> anti_divisors(36)
    [8, 24]
    >>> anti_divisors(37)
    [2, 3, 5, 15, 25]
    >>> anti_divisors(38)
    [3, 4, 5, 7, 11, 15, 25]
    >>> anti_divisors(39)
    [2, 6, 7, 11, 26]
    >>> anti_divisors(40)
    [3, 9, 16, 27]
    >>> anti_divisors(41)
    [2, 3, 9, 27]
    >>> anti_divisors(42)
    [4, 5, 12, 17, 28]
    >>> anti_divisors(43)
    [2, 3, 5, 17, 29]
    >>> anti_divisors(44)
    [3, 8, 29]
    >>> anti_divisors(45)
    [2, 6, 7, 10, 13, 18, 30]
    >>> anti_divisors(46)
    [3, 4, 7, 13, 31]
    >>> anti_divisors(47)
    [2, 3, 5, 19, 31]
    >>> anti_divisors(48)
    [5, 19, 32]
    >>> anti_divisors(49)
    [2, 3, 9, 11, 14, 33]
    >>> anti_divisors(50)
    [3, 4, 9, 11, 20, 33]
    >>> anti_divisors(51)
    [2, 6, 34]
    >>> anti_divisors(52)
    [3, 5, 7, 8, 15, 21, 35]
    >>> anti_divisors(53)
    [2, 3, 5, 7, 15, 21, 35]
    >>> anti_divisors(54)
    [4, 12, 36]
    >>> anti_divisors(55)
    [2, 3, 10, 22, 37]
    >>> anti_divisors(56)
    [3, 16, 37]
    >>> anti_divisors(57)
    [2, 5, 6, 23, 38]
    >>> anti_divisors(58)
    [3, 4, 5, 9, 13, 23, 39]
    >>> anti_divisors(59)
    [2, 3, 7, 9, 13, 17, 39]
    >>> anti_divisors(60)
    [7, 8, 11, 17, 24, 40]
    >>> anti_divisors(61)
    [2, 3, 11, 41]
    >>> anti_divisors(62)
    [3, 4, 5, 25, 41]
    >>> anti_divisors(63)
    [2, 5, 6, 14, 18, 25, 42]
    >>> anti_divisors(64)
    [3, 43]
    >>> anti_divisors(65)
    [2, 3, 10, 26, 43]
    >>> anti_divisors(66)
    [4, 7, 12, 19, 44]
    >>> anti_divisors(67)
    [2, 3, 5, 7, 9, 15, 19, 27, 45]
    >>> anti_divisors(68)
    [3, 5, 8, 9, 15, 27, 45]
    >>> anti_divisors(69)
    [2, 6, 46]
    >>> anti_divisors(70)
    [3, 4, 20, 28, 47]
    >>> anti_divisors(71)
    [2, 3, 11, 13, 47]
    >>> anti_divisors(72)
    [5, 11, 13, 16, 29, 48]
    >>> anti_divisors(73)
    [2, 3, 5, 7, 21, 29, 49]
    >>> anti_divisors(74)
    [3, 4, 7, 21, 49]
    >>> anti_divisors(75)
    [2, 6, 10, 30, 50]
    >>> anti_divisors(76)
    [3, 8, 9, 17, 51]
    >>> anti_divisors(77)
    [2, 3, 5, 9, 14, 17, 22, 31, 51]
    >>> anti_divisors(78)
    [4, 5, 12, 31, 52]
    >>> anti_divisors(79)
    [2, 3, 53]
    >>> anti_divisors(80)
    [3, 7, 23, 32, 53]
    >>> anti_divisors(81)
    [2, 6, 7, 18, 23, 54]
    >>> anti_divisors(82)
    [3, 4, 5, 11, 15, 33, 55]
    >>> anti_divisors(83)
    [2, 3, 5, 11, 15, 33, 55]
    >>> anti_divisors(84)
    [8, 13, 24, 56]
    >>> anti_divisors(85)
    [2, 3, 9, 10, 13, 19, 34, 57]
    >>> anti_divisors(86)
    [3, 4, 9, 19, 57]
    >>> anti_divisors(87)
    [2, 5, 6, 7, 25, 35, 58]
    >>> anti_divisors(88)
    [3, 5, 7, 16, 25, 35, 59]
    >>> anti_divisors(89)
    [2, 3, 59]
    >>> anti_divisors(90)
    [4, 12, 20, 36, 60]
    >>> anti_divisors(91)
    [2, 3, 14, 26, 61]
    >>> anti_divisors(92)
    [3, 5, 8, 37, 61]
    >>> anti_divisors(93)
    [2, 5, 6, 11, 17, 37, 62]
    >>> anti_divisors(94)
    [3, 4, 7, 9, 11, 17, 21, 27, 63]
    >>> anti_divisors(95)
    [2, 3, 7, 9, 10, 21, 27, 38, 63]
    >>> anti_divisors(96)
    [64]
    >>> anti_divisors(97)
    [2, 3, 5, 13, 15, 39, 65]
    >>> anti_divisors(98)
    [3, 4, 5, 13, 15, 28, 39, 65]
    >>> anti_divisors(99)
    [2, 6, 18, 22, 66]
    >>> anti_divisors(100)
    [3, 8, 40, 67]

    """
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
