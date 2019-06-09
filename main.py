from adj_list_graph import Graph
from bfs import breath_first_search
from vertex import Vertex
from dfs import depth_first_search 

bfs_stack = None
dfs_stack = None

def main():
    global bfs_stack, dfs_stack

    graph = Graph()
    initialize_graph(graph)
    print(graph)
    print( [str(s) for s in bfs_stack])
    print( [str(s) for s in dfs_stack])


def initialize_graph(graph):
    global bfs_stack,dfs_stack

    vertex1 = Vertex('a')
    vertex2 = Vertex('b')
    vertex3 = Vertex('c')
    vertex4 = Vertex('s')
    vertex5 = Vertex('z')

    graph.add_vertex(vertex1)
    graph.add_vertex(vertex2)
    graph.add_vertex(vertex3)
    graph.add_edge(vertex1, vertex3 )
    graph.add_edge(vertex4, vertex3 )
    graph.add_edge(vertex2, vertex3)
    graph.add_edge(vertex5, vertex1 )


    bfs_stack = breath_first_search(graph,vertex1)
    dfs_stack = depth_first_search(graph,graph.get_all_vertices,vertex1)

if __name__ == '__main__':
    main()