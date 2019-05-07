""" Topological Sort

"""

from mydigraph import *

def topological_sort(dag):
    """ Runs a topological sort on a directed acyclic graph (DAG)
    Produces a list of topologically sorted vertices
    """
    if dag == None:
        raise InvalidInputException("Dag is null")
    stack_list = []
    top_list = []
    # Utilizes a dictionary to keep track of incoming edges
    vdict = {}
    for vertex in dag.iterVertices():
        # The key is the vertex and the value is the number of incoming edges
        vdict[vertex] = len(dag.incidentEdges(vertex))
        if len(dag.incidentEdges(vertex)) == 0:
            stack_list.append(vertex)
    while not len(stack_list) == 0:
        v = stack_list.pop()
        top_list.append(v)
        for edge in dag.emanantEdges(v):
            w = dag.opposite(v,edge)
            vdict[w] -= 1
            if vdict[w] == 0:
                stack_list.append(w)
    # If value > 0, graph contains cycle
    for vertex in dag.iterVertices():
        if vdict[vertex] > 0:
            raise GraphCycleException("Graph contains cycle(s)")
    return top_list


class GraphCycleException(Exception):
    def __str__(self):
        return "Topological sort failed. A cycle occured."

class InvalidInputException(Exception):
    def __str__(self):
        return "Invalid Input Given."
