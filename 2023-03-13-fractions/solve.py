#This week’s question (thanks Tom!):
# Write a function that can do the 4 basic operations
# (add, subtract, multiply and divide) on two fractions.
# Return the most simplified form of the result.
# You can assume a non-zero denominator in the input,
# and don’t use any built-in implementations
# in your language of choice, if you can!
#
#Example:
#
#> fractionMath("3/4", "add", "1/8")
#> "3/2"
#
#> fractionMath("1/8", "multiply", "2/2")
#> "1/8"

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Rational ():
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def a(self):
        return self.numerator

    def b(self):
        return self.denominator

    def __add__(self, other):
        a_prime = self.a() * other.b() + self.b() * other.a()
        b_prime = self.b() * other.b()
        return Rational(a_prime, b_prime).simplify()

    def __sub__(self, other):
        a_prime = self.a() * other.b() - self.b() * other.a()
        b_prime = self.b() * other.b()
        return Rational(a_prime, b_prime).simplify()

    def __mul__(self, other):
        a_prime = self.a() * other.a()
        b_prime = self.b() * other.b()
        m = Rational(a_prime, b_prime).simplify()
        return m

    def __truediv__(self, other):
        a_prime = self.a() * other.b()
        b_prime = self.b() * other.a()
        return Rational(a_prime, b_prime).simplify()

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __repr__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def simplify(self):
        _gcd = gcd(self.numerator, self.denominator)
        return Rational(self.numerator / _gcd, self.denominator / _gcd)

    @classmethod
    def from_string(cls, string):
        numerator = int(string.split("/")[0])
        denominator = int(string.split("/")[1])
        return Rational(numerator, denominator)


def fractionMath(fraction1, operation, fraction2):
    """
    >>> "1. " + fractionMath("2/7", "add", "3/8")
    '1. 37/56'
    >>> "2. " + fractionMath("1/8", "multiply", "2/2")
    '2. 1/8'
    >>> "3. " + fractionMath("3/4", "subtract", "1/8")
    '3. 5/8'
    >>> "4. " + fractionMath("3/4", "divide", "1/8")
    '4. 6/1'
    """
    fraction1 = Rational.from_string(fraction1)
    fraction2 = Rational.from_string(fraction2)
    if operation == "add":
        return str(fraction1 + fraction2)
    elif operation == "subtract":
        return str(fraction1 - fraction2)
    elif operation == "multiply":
        return str(fraction1 * fraction2)
    elif operation == "divide":
        return str(fraction1 / fraction2)
    else:
        return "Invalid operation"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
