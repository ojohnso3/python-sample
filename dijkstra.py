from heappriorityqueue import *
from mygraph import *

def dijkstra(g, src):
    """ Calculates the shortest path tree from the source in the input
    connected graph g using Dijkstra's algorithm.
    Runs in O((|E| + |V|) log |V|) time using a HeapPriorityQueue data structure.
    """
    if g == None or src == None:
        raise InvalidInputException("Null input.")
    if not g.containsVertex(src):
        raise InvalidInputException("Doesn't contain source.")
    new_graph = MyGraph()
    PQ = HeapPriorityQueue()
    # Sets all decorations for nodes and adds nodes into PQ and new_graph
    for v in g.iterVertices():
        v.dist = float("inf")
        v.prev = None
        v.entry = PQ.push(v.dist,v)
        new_graph.insertVertex(v)
    src.dist = 0
    PQ.replaceKey(src.entry,src.dist)
    while not PQ.isEmpty():
        u = PQ.pop().value()
        # Replaces node costs depending on incoming edges
        for edge in g.incidentEdges(u):
            v = g.opposite(u,edge)
            if u.dist + edge.element() < v.dist:
                v.dist = u.dist + edge.element()
                v.prev = u
                PQ.replaceKey(v.entry,v.dist)
    # Constructs new_graph with all nodes and certain edges
    for v in g.iterVertices():
        if not v.prev == None:
            new_graph.insertEdge(v,v.prev,g.connectingEdge(v,v.prev))
    return new_graph


class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input Given."
