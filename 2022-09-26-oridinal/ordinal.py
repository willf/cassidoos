"""

If the units digit is:	0	1	2	3	4-9
This is written after the number	th	st	nd	rd	th
For example: 2nd, 7th, 20th, 23rd, 52nd, 135th, 301st.

Write a function to output the ordinal suffix of a positive integer concatenated to an inputted number.

Example:

> ordinal(3)
> '3rd'

> ordinal(57)
> '57th'
"""

def ordinal(n:int):
    """
    >>> ordinal(3)
    '3rd'
    >>> ordinal(57)
    '57th'
    >>> ordinal(0)
    '0th'
    >>> ordinal(1)
    '1st'
    >>> ordinal(2)
    '2nd'
    >>> ordinal(4)
    '4th'
    >>> ordinal(5)
    '5th'
    >>> ordinal(6)
    '6th'
    >>> ordinal(7)
    '7th'
    >>> ordinal(8)
    '8th'
    >>> ordinal(9)
    '9th'
    >>> ordinal(10)
    '10th'
    >>> ordinal(11)
    '11th'
    >>> ordinal(111)
    '111th'
    >>> ordinal(1111)
    '1111th'
    >>> ordinal(11114)
    '11114th'
    >>> ordinal(123)
    '123rd'
    """
    digits = str(n)
    if len(digits) >= 2:
      last_two_int = int(digits[-2:])
      if 11 <= last_two_int <= 13:
        return f"{n}th"
    last_digit = digits[-1]
    if last_digit == '1':
        return f'{n}st'
    elif last_digit == '2':
        return f'{n}nd'
    elif last_digit == '3':
        return f'{n}rd'
    else:
        return f'{n}th'

if __name__ == "__main__":
    import doctest

    doctest.testmod()
