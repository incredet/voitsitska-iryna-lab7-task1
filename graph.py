"""
lab 7 task 1 submission
"""
# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.

def get_graph_from_file(file_name: str) -> list:
    """
    (str) -> (list)
    Read graph from file and return a list of edges.
    >>> get_graph_from_file("/home/iryna/Documents/OP/w7/voitsitska-iryna-lab7-task1/data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(file_name, 'r', encoding = "utf-8") as file:
        output = []
        for i in file.readlines():
            output.append(i.strip().split(","))
        output = [ [int(i) for i in item] for item in output]
    return output

def to_edge_dict(edge_list):
    """
    (list) -> (dict)
    Convert a graph from list of edges to dictionary of vertices.
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    output = {}
    for item in edge_list:
        for value in item:
            output.setdefault(value, [])
        output[item[0]].append(item[1])
        output[item[1]].insert(0, item[0])
    return output

def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> bool
    Return True if graph contains a given edge and False otherwise.
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    return edge in [(key, val) for key, value in graph.items() for val in value]

def add_edge(graph, edge):
    """
    (dict, tuple) -> dict 
    Add a new edge to the graph and return new graph.
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
    return graph

def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)
    Delete an edge from the graph and return a new graph.
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    graph[edge[0]].remove(edge[1])
    graph[edge[1]].remove(edge[0])
    return graph

def add_node(graph, node):
    """
    (dict, int) -> (dict)
    Add a new node to the graph and return a new graph.
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    graph[node] = []
    return graph

def del_node(graph, node):
    """
    (dict, int) -> (dict)
    Delete a node and all incident edges from the graph.
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    pass

def convert_to_dot(graph):
    """
    (dict) -> (None)
    Save the graph to a file in a DOT format.
    """
    

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
