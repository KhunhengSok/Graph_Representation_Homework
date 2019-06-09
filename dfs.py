from vertex import Vertex
import adj_list_graph 

visited_list = {}

def depth_first_search(graph, vertices, starting_index, recursive = True):
    visited_list[starting_index] = None

    if recursive:
        _dfs_recursive(graph,vertices,starting_index)
    
    return visited_list

def _dfs_recursive(graph, vertices, starting_index):
    global visited_list
    for vertex in graph.get_adj(starting_index):
        if vertex not in visited_list:
            visited_list[vertex] = None
            _dfs_recursive(graph,vertices,vertex)
    