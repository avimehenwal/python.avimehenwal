#!/usr/bin/env python

"""
AUTHOR    : avimehenwal
CREATED   : So 20. Jan 17:52:13 CET 2019
FILENAME  : breadth_first_search.py
PROJECT   : Graph/tree traversal algorithms

There are two popular options for representing a graph,
the first being an adjacency matrix (effective with dense graphs)and
second an adjacency list (effective with sparse graphs).
I have opted to implement an adjacency list which stores each node in
a dictionary along with a set containing their adjacent nodes.
As the graph is undirected each edge is stored in both incident nodes adjacent sets.
"""

# MAIN

# Adjacency list representation
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    """ Depth first search
    >>> stack.append(['e','f'])
    ['a', 'b', 'c', ['e', 'f']]
    >>> stack.extend(['g','h'])
    ['a', 'b', 'c', ['e', 'f'], 'g', 'h']
    """
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

if __name__ == "__main__":
    traverse = dfs(graph, 'A')
    print(traverse)


# END

