"""
This week’s question:
Implement a simple version of autocomplete, where given an input string s and a dictionary of words dict, return the word(s) in dict that partially match s (or an empty string if nothing matches).

Example:

let dict = ['apple', 'banana', 'cranberry', 'strawberry']

$ simpleAutocomplete('app')
$ ['apple']

$ simpleAutocomplete('berry')
$ ['cranberry', 'strawberry']

$ simpleAutocomplete('fart')
$ []

"""


class AutoComplete:
    def __init__(self, words):
        self.words = words

    def simple_autocomplete(self, s):
        """
        >> a = AutoComplete(['apple', 'banana', 'cranberry', 'strawberry'])
        >> a.simple_autocomplete('app')
        ['apple']
        >> a.simple_autocomplete('berry')
        ['cranberry', 'strawberry']
        >> a.simple_autocomplete('fart')
        []
        """
        return [word for word in self.words if word.contains(s)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
