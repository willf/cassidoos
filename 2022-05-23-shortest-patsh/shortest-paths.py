import networkx as nx


"""
This week's question:
Given an n x m matrix where all of the units are 0s except for an 1 for “start”, 
a 2 for “end”, and 3s for walls, 
find the shortest paths that you can take to get from 1 to 2, 
while working around 3s.

Example (TypeScript):

let grid = [
[1,0,0],
[0,0,2]
]

let grid2 = [
[1,3,0],
[0,0,2]
]

$ startToEnd(grid)
$ [['right', 'right', 'down'], ['right', 'down', 'right'], ['down', 'right', 'right']]

$ startToEnd(grid2)
$ [['down', 'right', 'right']]
"""


def transpose(list_of_lists):
    return list(map(list, zip(*list_of_lists)))


def matrix_to_graph(matrix):
    start_node = None
    end_node = None
    n = len(matrix)
    if n == 0:
        return start_node, end_node, []
    m = len(matrix[0])
    G = nx.DiGraph()
    for i in range(n):
        for j in range(m):
            node_name = f"{i},{j}"
            # start node?
            node_color = matrix[i][j]
            node_hash = {"name": node_name, "color": node_color, "i": i, "j": j}
            G.add_node(node_name, **node_hash)
            node = G.nodes[node_name]
            if matrix[i][j] == 1:
                start_node = node
            # end node?
            if matrix[i][j] == 2:
                end_node = node
            matrix[i][j] = node
    for row in matrix:
        for first, second in n_grams(row, 2):
            if first["color"] != 3 and second["color"] != 3:
                G.add_edge(first["name"], second["name"], direction="right")
                G.add_edge(second["name"], first["name"], direction="left")
    for column in transpose(matrix):
        for first, second in n_grams(column, 2):
            if first["color"] != 3 and second["color"] != 3:
                G.add_edge(first["name"], second["name"], direction="down")
                G.add_edge(second["name"], first["name"], direction="up")
    return (start_node["name"], end_node["name"], G)


def n_grams(input, n):
    """
    >>> list(n_grams([1, 2, 3, 4, 5], 2))
    [(1, 2), (2, 3), (3, 4), (4, 5)]
    """
    return zip(*[input[i:] for i in range(n)])


def path_directions(G, path):
    return [G[u][v]["direction"] for u, v in n_grams(path, 2)]


def start_to_end(grid):
    """
    >>> start_to_end([[1, 0, 0], [0, 0, 2]])
    [['right', 'right', 'down'], ['right', 'down', 'right'], ['down', 'right', 'right']]
    >>> start_to_end([[1, 3, 0], [0, 0, 2]])
    [['down', 'right', 'right']]
    >>> start_to_end([[1],[2]])
    [['down']]
    >>> start_to_end([[1,2]])
    [['right']]
    >>> start_to_end([[1],[3],[2]])
    []
    >>> start_to_end([[1,3,2]])
    []
    >>> start_to_end([[1,3,2],[0,0,0]])
    [['down', 'right', 'right', 'up']]
    >>> start_to_end([[1, 3, 2, 0], [0, 0, 3, 0], [3, 0, 0, 0]])
    [['down', 'right', 'down', 'right', 'right', 'up', 'up', 'left']]
    >>> len(start_to_end([[1, 0, 0], [0, 0, 0], [0, 0, 2]]))
    6
    """
    start_node, end_node, G = matrix_to_graph(grid)
    paths = nx.all_shortest_paths(G, source=start_node, target=end_node)
    try:
        return [path_directions(G, path) for path in paths]
    except nx.exception.NetworkXNoPath:
        return []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # print(start_to_end([[1, 3, 2]]))
