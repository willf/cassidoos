import networkx as nx


"""
This week's question:
Given an n x m matrix where all of the units are 0s except for an 1 for “start”, 
a 2 for “end”, and 3s for walls, 
find the shortest paths that you can take to get from 1 to 2, 
while working around 3s.
"""


# convert an n x m matrix to list of edges
# At i, j, there is a path from i to i+i if matrix[i+1,j] =! 3 and i+1 < n
# At i, j, there is a path from i to j+1 if matrix[i,j+1] =! 3 and j+1 < m
# If matrix[i,j] = 1, then i is the start node
# If matrix[i,j] = 2, then j is the end node
def matrix_to_edge_list(matrix):
    """
    >>> matrix_to_edge_list([])
    (None, None, [])
    >>> matrix_to_edge_list([[1, 0, 0], [0, 0, 2]])
    ('0,0', '1,2', [('0,0', '1,0', 'right'), ('0,0', '0,1', 'down'), ('0,1', '1,1', 'right'), ('0,1', '0,2', 'down'), ('0,2', '1,2', 'right'), ('1,0', '1,1', 'down'), ('1,1', '1,2', 'down')])
    """
    start_node = None
    end_node = None
    n = len(matrix)
    if n == 0:
        return start_node, end_node, []
    m = len(matrix[0])
    edges = []
    for i in range(n):
        for j in range(m):
            node_name = f"{i},{j}"
            # start node?
            if matrix[i][j] == 1:
                start_node = node_name
            # end node?
            if matrix[i][j] == 2:
                end_node = node_name
            if i + 1 < n and matrix[i + 1][j] != 3:
                edges.append((node_name, f"{i+1},{j}", "right"))
                # edges.append((i, i + i))
            if j + 1 < m and matrix[i][j + 1] != 3:
                edges.append((node_name, f"{i},{j+1}", "down"))
                # edges.append((i, j + 1))
    return (start_node, end_node, edges)


def matrix_to_graph(matrix):
    start_node, end_node, edges = matrix_to_edge_list(matrix)
    G = nx.DiGraph()
    for a, b, direction in edges:
        G.add_edge(a, b, direction=direction)
    return (start_node, end_node, G)


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
    [['right', 'down', 'down'], ['down', 'right', 'down'], ['down', 'down', 'right']]
    >>> start_to_end([[1, 3, 0], [0, 0, 2]])
    [['right', 'down', 'down']]
    """
    start_node, end_node, G = matrix_to_graph(grid)
    paths = nx.all_simple_paths(G, source=start_node, target=end_node)
    return [path_directions(G, path) for path in paths]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
