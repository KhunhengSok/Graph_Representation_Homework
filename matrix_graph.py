from pprint import pprint 
from vertex import *
from collections import OrderedDict 

'''
    Representing graph by using matrices

       1  2  3  4  5
    1  0  1  1  0  0
    2  1  1  0  0  1
    3  1  0  0  1  1
    4  0  1  0  0  1
    5  0  0  1  1  0

    0|true for no edges 
    1|false for edges 
'''


class Graph:
    def __init__(self):
        self._GRAPH = None #2D Square List
        self._vertices_index = OrderedDict() 

    def add_vertex(self, vertex):
        if isinstance(vertex,Vertex):
            if self._GRAPH is None:
                self._GRAPH = [[1]]
                # self._GRAPH.append(1)
                self._vertices_index[vertex] = 0   #index of vertex is 0 since it's first element
            else:
                for row in self._GRAPH:
                    row.append(0)  #append 0 to each row
                self._GRAPH.append( [0 for i in range( len(self._GRAPH[0] ))])  #append entire row( all 0) to the self._GRAPH
                self._vertices_index[vertex] = len(self._GRAPH[0]) -1 #save the index of vertex in eslf._vertice_index
                self._GRAPH[-1][-1] =1
            
        else:
            raise TypeError("Expected Vertex's object. Got" + str(type(vertex)))

    def add_edge(self, start_vertex, end_vertex):
        if isinstance(start_vertex,Vertex) and isinstance(end_vertex,Vertex):
            if start_vertex not in self._vertices_index:
                self.add_vertex(start_vertex)
            if end_vertex not in self._vertices_index:
                self.add_vertex(end_vertex)

            index1 = self._vertices_index.get(start_vertex)
            index2 = self._vertices_index.get(end_vertex)

            self._GRAPH[index1][index2] = 1
            self._GRAPH[index2][index1] = 1


    def __str__(self):
        string = "  "

        for vertex in self._vertices_index:
            string += f'{vertex} '

        vertices_name = list(self._vertices_index.keys())
        string += '\n'
        for index, i in enumerate(self._GRAPH):
            string += str(vertices_name[index]) + ' '
            for j in i:
                string += str(j) + " "
            string += '\n'
        return string        

    def show_graph(self):
        print(self.__str__)

def main():
    graph = Graph()
    vertex1 = Vertex('a')
    vertex2 = Vertex('b')
    vertex3 = Vertex('c')
    vertex4 = Vertex('s')
    vertex5 = Vertex('z')


    graph.add_vertex(vertex1)
    graph.add_vertex(vertex2)
    graph.add_vertex(vertex3)
    graph.add_vertex(vertex4)
    graph.add_vertex(vertex5)

    graph.add_edge(vertex1,vertex3)
    graph.add_edge(vertex1,vertex5)
    graph.add_edge(vertex3,vertex2)
    
    print(graph)


if __name__ == "__main__":
    main()