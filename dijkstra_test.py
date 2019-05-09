#!/usr/bin/python

import dijkstra
import mygraph
reload(dijkstra)
reload(mygraph)
from dijkstra import *
from mygraph import *
import pytest

# Checks InvalidInputException error
def invalidinput_test():
    with pytest.raises(InvalidInputException):
        g = None
        src = GraphVertex("src")
        dijkstra(g,src)
    with pytest.raises(InvalidInputException):
        g = MyGraph()
        src = None
        dijkstra(g,src)
    with pytest.raises(InvalidInputException):
        g = MyGraph()
        src = GraphVertex("src")
        dijkstra(g,src)

# Checks if shortest path graph is returned
def shortpath_test():
    g = MyGraph()
    v0 = GraphVertex("v0")
    v1 = GraphVertex("v1")
    v2 = GraphVertex("v2")
    g.insertVertex(v0)
    g.insertVertex(v1)
    g.insertVertex(v2)

    e0 = GraphEdge("e0", 8)
    e1 = GraphEdge("e1", 3)
    e2 = GraphEdge("e2", 4)
    g.insertEdge(v0, v2, e0)
    g.insertEdge(v0, v1, e1)
    g.insertEdge(v1, v2, e2)

    ret = dijkstra(g, v0)

    assert e1 in ret.edges()
    assert e2 in ret.edges()
    assert e0 not in ret.edges()

# Runs tests
def get_tests():
    return [invalidinput_test,shortpath_test]


# The mainline runs all of the test functions in the list returned by get_tests
if __name__ == '__main__' :
    print 'Running tests...'
    for test in get_tests():
        test()
    print 'All tests passed!'
