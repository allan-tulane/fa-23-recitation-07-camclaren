from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    # initializes the set of results
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        ###TODO - COMMENT
        node = frontier.pop()
        result.add(node)
        for i in graph[node]:
            if i not in result:
                frontier.add(i)
    return result


def connected(graph):
    ### TODO
    n_nodes = len(graph)
    r = reachable(graph, list(graph.keys())[0])
    
    if (len(r) == n_nodes):
        return True
    else:
        return False


def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    ### TODO
    results = []
    next = set(graph.keys())
    while (len(next) > 0):
        finished = next.pop()
        reach = reachable(graph, finished)
        next = next - reach
        results.append(reach)
    return len(results)

