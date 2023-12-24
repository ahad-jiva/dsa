from sys import argv
from stack_array import *


class Vertex:
    def __init__(self, name):
        '''Add whatever parameters/attributes are needed'''
        self.name = name
        self.in_degree = 0
        self.adj_vertices = []


def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * one vertex per line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    if len(vertices) == 0:
        raise ValueError("input contains no edges")
    if len(vertices) % 2 == 1:
        raise ValueError('input contains an odd number of tokens')
    dict_of_vertices = {}
    for i in range(0, len(vertices) - 1, 2):
        if vertices[i] not in dict_of_vertices and vertices[i + 1] not in dict_of_vertices:
            dict_of_vertices[vertices[i]] = Vertex(vertices[i])
            dict_of_vertices[vertices[i + 1]] = Vertex(vertices[i + 1])
            dict_of_vertices[vertices[i]].adj_vertices += [vertices[i + 1]]
            dict_of_vertices[vertices[i + 1]].in_degree += 1
        elif vertices[i] in dict_of_vertices and vertices[i + 1] not in dict_of_vertices:
            dict_of_vertices[vertices[i + 1]] = Vertex(vertices[i + 1])
            dict_of_vertices[vertices[i]].adj_vertices += [vertices[i + 1]]
            dict_of_vertices[vertices[i + 1]].in_degree += 1
        elif vertices[i] not in dict_of_vertices and vertices[i + 1] in dict_of_vertices:
            dict_of_vertices[vertices[i]] = Vertex(vertices[i])
            dict_of_vertices[vertices[i + 1]].in_degree += 1
            dict_of_vertices[vertices[i]].adj_vertices += [vertices[i + 1]]
        elif vertices[i] in dict_of_vertices and vertices[i + 1] in dict_of_vertices:
            dict_of_vertices[vertices[i + 1]].in_degree += 1
            dict_of_vertices[vertices[i]].adj_vertices += [vertices[i + 1]]
    vertex_stack = Stack(69)
    tsorted_vertices = []
    for vertex in dict_of_vertices:
        if dict_of_vertices[vertex].in_degree == 0:
            vertex_stack.push(dict_of_vertices[vertex])
    while not vertex_stack.is_empty():
        popped_vertex = vertex_stack.pop()
        tsorted_vertices.append(popped_vertex.name)
        for adjacent_vertex in popped_vertex.adj_vertices:
            dict_of_vertices[adjacent_vertex].in_degree -= 1
            if dict_of_vertices[adjacent_vertex].in_degree == 0:
                vertex_stack.push(dict_of_vertices[adjacent_vertex])
    if len(tsorted_vertices) == len(dict_of_vertices):
        return '\n'.join(tsorted_vertices)
    elif len(tsorted_vertices) != len(dict_of_vertices):
        raise ValueError("input contains a cycle")


# 100% Code coverage NOT required
def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG.  Use this code 
       if you want to run tests on a file with a list of edges'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()

    vertices = []
    for line in f:
        vertices += line.split()

    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
