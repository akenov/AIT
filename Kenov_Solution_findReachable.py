# Anton Kenov, AIT Task Solution in Python

# Find all nodes that can be reached inside the provided __directed__
# graph starting at the node with the id denoted in `startAt`.
#
# Returns an array of distinct node IDs that can be reached directly
# or indirectly from the starting point.
#
# @param graph the graph to analyze.
# @param startAt the ID of the node from which to start.

#   ASCII representation of graph:
#
#   (1) ----> (2)       (6) ----> (5)
#    ^         |         |
#    |         |         |
#    v         v         v
#   (3) <---> (4) <---- (7)


graph = {
    "nodes": [
        {"id": 1},
        {"id": 2},
        {"id": 3},
        {"id": 4},
        {"id": 5},
        {"id": 6},
        {"id": 7}
    ],
    "edges": [
        {
            "from": 1,
            "to": 2
        },
        {
            "from": 2,
            "to": 4
        },
        {
            "from": 4,
            "to": 3
        },
        {
            "from": 3,
            "to": 1
        },
        {
            "from": 3,
            "to": 4
        },
        {
            "from": 1,
            "to": 3
        },
        {
            "from": 7,
            "to": 4
        },
        {
            "from": 6,
            "to": 5
        },
        {
            "from": 6,
            "to": 7
        }
    ]
}


def follow_path(_start_at, _nodes, _edges):
    _reached = []

    for edge in _edges:
        node_from = edge[0]
        node_to = edge[1]

        if node_from == _start_at and node_from in _nodes and node_to in _nodes:
            _reached.append(node_to)
            _edges.remove(edge)
            _nodes.remove(node_from)
            _reached.extend(follow_path(node_to, _nodes, _edges))

    return _reached


def find_reachable(graph, start_at):
    nodes = []
    for node in graph['nodes']:
        nodes.append(node['id'])

    edges = []
    for edge in graph['edges']:
        edges.append(tuple((edge['from'], edge['to'])))

    outgoing_edges = []
    for out_edge in edges:
        if out_edge[0] == start_at:
            outgoing_edges.append(out_edge)

    reachable = []
    for out_edge in outgoing_edges:
        nodes_init = nodes.copy()

        ignore_edges = outgoing_edges.copy()
        ignore_edges.remove(out_edge)

        single_out_edges = edges.copy()
        for ed in ignore_edges:
            if ed in single_out_edges:
                single_out_edges.remove(ed)

        reachable.extend(follow_path(start_at, nodes_init, single_out_edges))

    return set(reachable)


if __name__ == "__main__":

    for node_ in graph['nodes']:
        reached = find_reachable(graph, node_['id'])
        print('Nodes to be reached from Node#' + str(node_['id']))
        print(reached, end='\n\n')

