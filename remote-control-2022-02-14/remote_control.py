import networkx as nx
from typing import List, Tuple
from collections import Counter


def ngrams(letters: List[str], n: int) -> List[Tuple]:
    """
    Given a list of letters, write a function that returns a list of all possible ngrams of length N.

    >>> list(ngrams(['a'], 2))
    []
    >>> list(ngrams(['a', 'b', 'c'], 2))
    [('a', 'b'), ('b', 'c')]

    >>> list(ngrams(['a', 'b', 'c', 'd'], 2))
    [('a', 'b'), ('b', 'c'), ('c', 'd')]

    >>> list(ngrams(['a', 'b'],2))
    [('a', 'b')]

    """
    sequences = [letters[i:] for i in range(n)]
    return zip(*sequences)


def sort_path(path: List[str]) -> List[str]:
    d = {"up": 4, "down": 3, "right": 2, "left": 1, "select": 0}
    p = sorted(path, key=lambda x: d.get(x, 1), reverse=True)
    return p


def setup_graph() -> nx.Graph:
    """
    This week’s question:
    Given a QWERTY keyboard grid, write a function that returns a graph of the keyboard.

    """
    g = nx.DiGraph()
    letters = [
        ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
        ["a", "s", "d", "f", "g", "h", "i", "j", "k", "l"],
        ["z", "x", "c", "v", "b", "n", "m", ",", ".", "/"],
    ]
    transposed_letters = list(zip(*letters))
    for row in letters:
        for letter in row:
            g.add_node(letter)
    for row in letters:
        g.add_edges_from(ngrams(row, 2), direction="right")
        g.add_edges_from([(b, a) for a, b in ngrams(row, 2)], direction="left")

    for row in transposed_letters:
        g.add_edges_from(ngrams(row, 2), direction="down")
        g.add_edges_from([(b, a) for a, b in ngrams(row, 2)], direction="up")
    return g


def path_equivalent(path1: List[str], path2: List[str]) -> bool:
    return Counter(path1) == Counter(path2)


def path_to_edge_labels(path: List[str], g: nx.Graph) -> List[str]:
    """
    >>> g = setup_graph()
    >>> path = ['down', 'down', 'right', 'right']
    >>> path_equivalent(path, path_to_edge_labels(nx.shortest_path(g, 'q', 'c', weight="weight"),g))
    True
    """
    labels = [g.edges[a, b]["direction"] for a, b in ngrams(path, 2)]
    sorted_labels = sort_path(labels)
    return sorted_labels


def path_to_direction_string(path: List[str], g: nx.Graph) -> str:
    """
    >>> g = setup_graph()
    >>> path = ['down', 'down', 'right', 'right']
    >>> path_to_direction_string(path, g)
    'down, down, right, right, select'
    """
    return ", ".join(path) + ", select"


def remote_control(word: str, starting_from: str = "q") -> str:
    """
    This week’s question:
    Given a QWERTY keyboard grid and a remote control with arrows and a “select” button,
    write a function that returns the buttons you have to press to type a certain word.
    The cursor will always start in the upper left at the letter Q.

    Note that there are a number of different shortest paths from one letter to another.

    Example:

    > remote_control('car')
    'down, down, right, right, select, left, left, up, select, up, right, right, right, select'

    > remote_control('hello')
    'down, down, right, right, select, left, left, up, select, up, right, right, right, select, down, down, right, right, select, left, left, up, select, up, right, right, right, select'

    >>> Counter('down, down, right, right, select, left, left, up, select, up, right, right, right, select'.split(', ')) == Counter(remote_control('car').split(', '))
    True
    """
    g = setup_graph()
    directions = []
    for a, b in ngrams(list(starting_from + word), 2):
        path = nx.shortest_path(g, a, b)
        labels = path_to_edge_labels(path, g)
        directions.append(path_to_direction_string(labels, g))
    return ", ".join(directions)


if __name__ == "__main__":
    import doctest
    import argparse

    parser = argparse.ArgumentParser("Print remote control directions")
    parser.add_argument("-w", "--word", help="Word to type")
    parser.add_argument("--letter", help="Starting letter", default="q")
    parser.add_argument("-t", "--test", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    if args.test or args.verbose or (args.word is None):
        doctest.testmod(verbose=args.verbose)
    else:
        print(remote_control(args.word, args.letter))
