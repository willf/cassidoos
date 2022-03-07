"""
Implement a Hashmap from scratch without any existing libraries in your preferred language.

A Hashmap should:

- Be empty when initialized
- Have the function put(int key, int value) which inserts a (key, value) pair
  into the hashmap. If the key already exists, update the corresponding value.
- Have the function get(int key) which returns the value to which
  the specified key is mapped, or -1 if there’s no mapping for the key.
- Have the function remove(key) which removes the key and its value if it
  exists in the map.
"""


class AssociationList:
    def __init__(self):
        self.map = []

    def put(self, key, value):
        """
        Inserts a (key, value) pair into the AssociationList. If the key already exists,
        update the corresponding value.
        >>>
        >>> h = AssociationList()
        >>> h.put(1, 2)
        >>> h.get(1)
        2
        >>> h.put(1, 3)
        >>> h.get(1)
        3
        """
        for i, (k, _) in enumerate(self.map):
            if k == key:
                self.map[i] = (key, value)
                return
        else:
            self.map.append((key, value))

    def get(self, key):
        """
        Returns the value to which the specified key is mapped,
        or -1 if there’s no mapping for the key.
        >>>
        >>> h = AssociationList()
        >>> h.put(1, 2)
        >>> h.get(1)
        2
        >>> h.get(2)
        -1
        """
        for k, v in self.map:
            if k == key:
                return v
        return -1

    def remove(self, key):
        """
        Removes the key and its value if it exists in the map.
        >>>
        >>> h = AssociationList()
        >>> h.put(1, 2)
        >>> h.remove(1)
        >>> h.get(1)
        -1
        >>> h.remove(2) # should not error
        >>> h.get(2)
        -1
        """
        for i, (k, v) in enumerate(self.map):
            if k == key:
                del self.map[i]
                return


class HashMap(AssociationList):
    """
    >>> h = HashMap()
    >>> h.put(1, 2)
    >>> h.get(1)
    2
    >>> h.put(1, 3)
    >>> h.get(1)
    3
    >>> h.remove(1)
    >>> h.get(1)
    -1

    """

    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
