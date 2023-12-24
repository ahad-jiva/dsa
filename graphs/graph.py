from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key):
        '''Add other Attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.visited = False
        self.color = None


class Graph:
    '''Add additional helper methods if necessary.'''

    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        # This method should call add_vertex and add_edge!!!
        self.graph = {}
        with open(filename) as graph:
            edges = graph.readlines()
        for edge in edges:
            edge = edge.strip()
            vertex_pair = edge.split()
            self.add_vertex(vertex_pair[0])
            self.add_vertex(vertex_pair[1])
            self.add_edge(vertex_pair[0], vertex_pair[1])

    def add_vertex(self, key):
        # Should be called by init
        '''Add vertex to graph only if the vertex is not already in the graph.'''
        if key not in self.graph:
            self.graph[key] = Vertex(key)

    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex ID's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.graph[v1].adjacent_to += [v2]
        self.graph[v2].adjacent_to += [v1]

    def get_vertex(self, key):
        '''Return the Vertex object associated with the ID. If ID is not in the graph, return None'''
        if key in self.graph:
            return self.graph[key]
        return None

    def get_vertices(self):
        '''Returns a list of ID's representing the vertices in the graph, in ascending order'''
        list_of_keys = list(self.graph.keys())
        list_of_keys.sort()
        return list_of_keys

    def conn_components(self):
        '''Return a Python list of lists.  For example: if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending alphabetical order) in the connected component represented by that list.
           The overall list will also be in ascending alphabetical order based on the first item in each sublist.'''
        # This method MUST use Depth First Search logic!
        for vertex in self.graph:
            self.graph[vertex].visited = False
        list_of_lists = []
        visited_stack = Stack(len(self.graph))
        for vertex in self.graph:
            if self.graph[vertex].visited is False:
                component = []
                visited_stack.push(vertex)
                while not visited_stack.is_empty():
                    root = visited_stack.pop()
                    component.append(root)
                    self.graph[root].visited = True
                    for vertices in self.graph[root].adjacent_to:
                        if not self.graph[vertices].visited:
                            self.graph[vertices].visited = True
                            visited_stack.push(vertices)
                if len(component) != 0:
                    component.sort()
                    list_of_lists.append(component)
        sorted_list_of_lists = sorted(list_of_lists)
        return sorted_list_of_lists

    def is_bipartite(self):
        '''Return True if the graph is bipartite, False otherwise.'''
        # This method MUST use Breadth First Search logic!
        for vertex in self.graph:
            self.graph[vertex].visited = False
            self.graph[vertex].color = None
        color_queue = Queue(len(self.graph))
        for vertex in self.graph:
            if self.graph[vertex].color is None:
                self.graph[vertex].color = 0
                color_queue.enqueue(vertex)
                while not color_queue.is_empty():
                    root = color_queue.dequeue()
                    root_color = self.graph[root].color
                    for adj_vert in self.graph[root].adjacent_to:
                        if self.graph[adj_vert].color == root_color:
                            return False
                        elif self.graph[adj_vert].color is None:
                            if root_color == 0:
                                self.graph[adj_vert].color = 1
                            else:
                                self.graph[adj_vert].color = 0
                            color_queue.enqueue(adj_vert)
        return True
