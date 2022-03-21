#
# Given a list of times in a 24-hour period, return the smallest interval between two times in the list.
#
# For example,
# >> smallestTimeInterval(['01:00', '08:15', '11:30', '13:45', '14:10', '20:05'])
# >> '25 minutes'
def smallestTimeInterval(times):
    """
    Given a list of times in a 24-hour period, return the smallest interval between two times in the list. 
    Assumes that the times are in the format 'hh:mm'.
    Assumes that the times are sorted.
    >>> smallestTimeInterval(['01:00', '08:15', '11:30', '13:45', '14:10', '20:05'])
    '25 minutes'
    >>> smallestTimeInterval(['01:00'])
    '0 minutes'
    >>> smallestTimeInterval(['01:00', '01:00'])
    '0 minutes'
    >>> smallestTimeInterval([])
    '0 minutes'
    """
    intervals = []
    for i in range(len(times) - 1):
        intervals.append(time_to_minutes(times[i + 1]) - time_to_minutes(times[i]))
    min_interval = min(intervals) if intervals else 0

    return f'{min_interval} {pluralize("minute", min_interval)}'


def time_to_minutes(time):
    """
    Given a time in the format 'hh:mm', return the number of minutes since midnight.
    >>> time_to_minutes('00:00')
    0
    >>> time_to_minutes('01:00')
    60
    >>> time_to_minutes('12:00')
    720
    """
    hours, minutes = time.split(":")
    return int(hours) * 60 + int(minutes)


def pluralize(word, count):
    """
    Given a word and a count, return the pluralized version of the word.
    >>> pluralize('cat', 1)
    'cat'
    >>> pluralize('cat', 2)
    'cats'
    """
    if count == 1:
        return word
    else:
        return word + "s"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
