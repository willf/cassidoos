import random

from scipy.stats import chisquare

# Problem statement:
# You are given a string S, and you want to determine the probability
# That it is a random login of a certain kind.
# That is:
# 1. Each character is a hexadecimal digit
# 2. The characters appear 'randomly', that is, the probability of
#    any character appearing is the same.
# This looks like a random login: d15fa42ddc93870c9058
# This does not look like a random login: Bob
# This looks like a random login: 5204c7a926182a1b
# This does not look like a random login: willf
# This might be a random login, it's hard to say: a73676b
# This does not look like a random login: 1234567890

# Write a function that takes a string and returns a float
# representing the probability that it is a random login.
#
# Example:
#
# >>> random_hex_string_score('d15fa42ddc93870c9058')
# 1.0
# >>> random_hex_string_score('Bob')
# 0.0
# >>> random_hex_string_score('5204c7a926182a1b')
# 1.0
# >>> random_hex_string_score('willf')
# 0.0
# >>> random_hex_string_score('a73676b')
# 0.5
# >>> random_hex_string_score('1234567890')
# 0.0
# >>> random_hex_string_score('1234567890abcdef')
# 1.0
# >>> random_hex_string_score('1234567890abcdefg')
# 0.0

def is_valid_hex_string(s):
    """
    We are going to assume that the string is already lowercased.
    >>> is_valid_hex_string('d15fa42ddc93870c9058')
    True
    >>> is_valid_hex_string('Bob')
    False
    >>> is_valid_hex_string('5204c7a926182a1b')
    True
    >>> is_valid_hex_string('willf')
    False
    >>> is_valid_hex_string('a73676b')
    True
    >>> is_valid_hex_string('1234567890')
    True
    >>> is_valid_hex_string('1234567890abcdef')
    True
    >>> is_valid_hex_string('1234567890abcdefg')
    False
    """
    for char in s:
        if not is_valid_hex_char(char):
            return False
    return True

def is_valid_hex_char(char):
    """
    WE are going to assume that the string is already lowercased.
    >>> is_valid_hex_char('d')
    True
    >>> is_valid_hex_char('B')
    False
    >>> is_valid_hex_char('5')
    True
    >>> is_valid_hex_char('w')
    False
    """
    return char in '0123456789abcdef'

def is_next_hex_digit(char1, char2):
    """
    Is char2 the next hex digit after char1?
    >>> is_next_hex_digit('0', '1')
    True
    >>> is_next_hex_digit('1', '2')
    True
    >>> is_next_hex_digit('2', '4')
    False
    """
    if not is_valid_hex_char(char1) or not is_valid_hex_char(char2):
        return False
    return char2 == hex(int(char1, 16) + 1)[2:]

def has_sequential_hex_digits(s, min_length=4):
    """
    >>> has_sequential_hex_digits('d15fa42ddc93870c9058')
    False
    >>> has_sequential_hex_digits('Bob')
    False
    >>> has_sequential_hex_digits('5204c7a926182a1b')
    False
    >>> has_sequential_hex_digits('willf')
    False
    >>> has_sequential_hex_digits('a73676b')
    False
    >>> has_sequential_hex_digits('1234567890')
    True
    >>> has_sequential_hex_digits('1234567890abcdef')
    True
    >>> has_sequential_hex_digits('1234567890abcdefg')
    True
    >>> has_sequential_hex_digits('1234567890abcdefg1234567890abcdefg')
    True
    >>> has_sequential_hex_digits('1234567890abcdefg1234567890abcdef')
    True

    """
    current_sequence_length = 0
    for i in range(len(s) - 1):
        if is_next_hex_digit(s[i], s[i + 1]) or is_next_hex_digit(s[i+1], s[i]):
            current_sequence_length += 1
        else:
            current_sequence_length = 0
        if current_sequence_length >= min_length:
            return True
    return False

def random_hex_string_of_length(length):
    """
    Return a random hex string of the given length.
    >>> len(random_hex_string_of_length(16))
    16
    >>> len(random_hex_string_of_length(32))
    32
    >>> is_valid_hex_string(random_hex_string_of_length(16))
    True

    """
    return ''.join([random.choice('0123456789abcdef') for i in range(length)])

def observed_frequencies(s):
    """
    >>> observed_frequencies('d15fa42ddc93870c9058')
    [2, 1, 1, 1, 1, 2, 0, 1, 2, 2, 1, 0, 2, 3, 0, 1]
    """
    observed = [0] * 16
    for char in s:
        observed[int(char, 16)] += 1
    return observed

def chi_statistic(s):
    """
    We are going to assume that the string is already lowercased.
    We are going to assume that the string includes only valid hex characters.
    >>> chi_statistic(random_hex_string_of_length(16)) > 0.01
    True
    >>> chi_statistic('0000') < 0.0001
    True
    """
    observed = observed_frequencies(s)
    return chisquare(observed).pvalue



def random_hex_string_score(login):
    """
    >>> random_hex_string_score('d15fa42ddc93870c9058') > 0.01
    True
    >>> random_hex_string_score('D15FA42DDC93870C9058') > 0.01
    True
    >>> random_hex_string_score('Bob') < 0.0001
    True
    >>> random_hex_string_score('5204c7a926182a1b') > 0.01
    True
    >>> random_hex_string_score('willf') < 0.0001
    True
    >>> random_hex_string_score('a73676b') > 0.0001
    True
    """

    if len(login) == 0:
        return 0.0
    login = login.lower()
    if not is_valid_hex_string(login):
        return 0.0
    if has_sequential_hex_digits(login):
        return 0.0
    return chi_statistic(login)

if __name__ == '__main__':
    import doctest
    doctest.testmod() # Run with python3 -m doctest -v random_hex_string_score.py
