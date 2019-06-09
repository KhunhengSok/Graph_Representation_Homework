from vertex import *
import bfs

'''
    Representing graph using list 


    {
        vertex : neighbor(set)
        'a' : [1,'b']
    }
'''

class Graph:
    def __init__(self):
        self._vertices = dict()
    
    def add_vertex(self, vertex):
        if isinstance(vertex,Vertex):
            if vertex not in self._vertices:
                self._vertices[vertex] = list()
                return True
            else:
                return False
        else:
            raise TypeError("Expectd Vertex's object. Got" + str(type(vertex)))

    def add_edge(self, start_vertex, end_vertex):
        if start_vertex not in self._vertices:
            self.add_vertex(start_vertex)

        if end_vertex not in self._vertices:
            self.add_vertex(end_vertex)

        self._vertices[start_vertex].append(end_vertex)
        self._vertices[end_vertex].append(start_vertex)

    def get_adj(self, vertex):
        if vertex in self._vertices:
            return self._vertices[vertex]
        else:
            return None

    def show_graph(self):
        print(self)
    
    def __str__(self):
        string = ""
        for vertex in self._vertices:
            string += (f"{vertex}'s edges are { [str(_) for _ in self._vertices[vertex] ] } \n"  )
        return string

    def get_all_vertices(self):
        return self._vertices