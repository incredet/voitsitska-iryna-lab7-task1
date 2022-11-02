"""
lab 7 task 1 submission
"""
# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.

def get_graph_from_file(file_name: str) -> list:
    """
    Read graph from file and return a list of edges.
    Args:
        file_name: a path to file
    Returns:
        list; list of edges
    >>> get_graph_from_file("/home/iryna/Documents/OP/w7/voitsitska-iryna-lab7-task1/data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(file_name, 'r', encoding = "utf-8") as file:
        output = []
        for i in file.readlines():
            output.append(i.strip().split(","))
        output = [ [int(i) for i in item] for item in output]
    return output

def to_edge_dict(edge_list: list) -> dict:
    """
    Convert a graph from list of edges to dictionary of vertices.
    Args:
        edge_list: list of edges
    Returns:
        dict: dict that represents a graph
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

def is_edge_in_graph(graph: dict, edge: tuple) -> bool:
    """
    Return True if graph contains a given edge and False otherwise.
    Args:
        graph: a graph
        edge: edge to check
    Returns:
        bool: if the graph contains the edge
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    return edge in [(key, val) for key, value in graph.items() for val in value]

def add_edge(graph: dict, edge: tuple) -> dict: #check this function
    """
    Add a new edge to the graph and return new graph.
    Args:
        graph: a graph
        edge: edge to add
    Returns:
        the graph w the edge
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    >>> add_edge({1: [2], 2: [1]}, (1, 3))
    {1: [2, 3], 2: [1], 3: [1]}
    """
    if edge[0] not in graph.keys():
        graph.setdefault(edge[0], [])
    if edge[1] not in graph.keys():
        graph.setdefault(edge[1], [])
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
    return graph

def del_edge(graph: dict, edge: tuple) -> dict: #check this function and make it right
    """
    Delete an edge from the graph and return a new graph.
    Args:
        graph: a graph
        edge: edge to delete
    Returns:
        the graph w/out the edge
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    try:
        graph[edge[0]].remove(edge[1])
        graph[edge[1]].remove(edge[0])
        return graph
    except KeyError:
        try:
            graph[edge[0]].remove(edge[1])
            return graph
        except KeyError:
            try:
                graph[edge[1]].remove(edge[0])
                return graph
            except KeyError:
                return graph

def add_node(graph: dict, node: int) -> dict:
    """
    Add a new node to the graph and return a new graph.
    Args:
        graph: dict that represents a graph
        node: node to add
    Returns:
        dict: the graph w node
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    >>> add_node({1: [2], 2: [1]}, 1)
    {1: [2], 2: [1]}
    """
    if node not in graph.keys():
        graph[node] = []
    return graph

def del_node(graph: dict, node: int) -> dict:
    """
    Delete a node and all incident edges from the graph.
    Args:
        graph: dict that represents a graph
        node: int, node to delete
    Returns:
        dict: dict w/out node
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    for value in graph.values():
        if node in value:
            value.remove(node)
    try:
        del graph[node]
        return graph
    except KeyError:
        return graph

def convert_to_dot(graph: dict) -> None:
    """
    Args:
        graph: dictionary that represents a graph
    Returns:
        the function returns None
    Save the graph to a file in a DOT format.
    >>> convert_to_dot({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]})
    """
    with open('w7/voitsitska-iryna-lab7-task1/graph.DOT', 'w', encoding = "utf-8") as file:
        dotlines = "digraph {\n"
        for key, value in graph.items():
            for val in value:
                dotlines += f"{key} -> {val}\n"
        dotlines += "}"
        file.write(dotlines)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
