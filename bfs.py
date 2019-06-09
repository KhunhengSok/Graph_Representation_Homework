from vertex import Vertex
import adj_list_graph 

def breath_first_search(graph, s):

    if isinstance(graph,adj_list_graph.Graph):
        level = {s : 0}
        visited_list = [s]
        frontier = [s]
        i = 1 

        while frontier:
            next = []
            for vertex in frontier:
                for u in graph.get_adj(vertex):
                    if u not in level:
                        visited_list.append(u)
                        next.append(u)
                        level[u] = i 

            i += 1
            frontier = next    
            
        return visited_list
        
    else:
        raise TypeError(f"Expected {adj_list_graph.Graph}. Got {type(graph)} ")