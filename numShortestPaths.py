class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input given."

def numShortestPaths(g, start, end):
    """ Finds the number of shortest paths between two nodes in a graph
    Takes in a graph, start node, and end node, and returns an integer
    denoting how many shortest paths there are between the two nodes in
    in the graph.
    """
    if g == None or start == None or end == None:
        raise InvalidInputException("Input is null.")
    if not g.containsVertex(start) or not g.containsVertex(end):
        raise InvalidInputException("Doesn't contain source.")
    nodes = []
    nodes.append(start)
    # Adds two decorations to the vertices
    for node in g.iterVertices():
        node.minCount = float("inf")
        node.numCount = 0
    start.minCount = 0
    while not len(nodes) == 0:
        node = nodes.pop(0)
        # Base case: if node is the end node, return the numCount decoration
        if node == end:
            return node.numCount
        # Decorates neighboring nodes and adds them to the list
        for edge in g.incidentEdges(node):
            new_node = g.opposite(node,edge)
            if new_node.minCount == float("inf"):
                new_node.minCount = node.minCount+1
                nodes.append(new_node)
            if new_node.minCount == node.minCount + 1:
                new_node.numCount = node.numCount + 1
