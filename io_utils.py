'''

I/O functions
-cgraph(file)-> nodes, edges, weighted(optional)
-adj_ls(nodes, edges, directed/undirected(optional)
-adj_matrix(nodes, edges, directed/undirected(optional)

I have created some optional boolean values that you can use to make the
function work on undirected or directed graphs, and whether the graph has 
edge weights or not.

'''


def cgraph(filee, weights = False):
    ''' 
    With a file  we will extract a graph of nodes and edges
    
    Input:
        1. file containing nodes and edges
        2. optional input that decides if graph has weights
    Return:
        1. A list of nodes
        2. A list of edges where edges are list pairs
    '''
    nodes = []
    edges = []
    weighted = {}

    filee = open(filee)

    for line in filee:
        info = line.split()
        if info[0] not in nodes:
            nodes.append(info[0])
        if info[1] not in nodes:
            nodes.append(info[1])
        edges.append([info[0],info[1]])
        if weights == True:
            weighted[info[0],info[1]] = int(info[2])
    if weights == True:
        return nodes, edges, weighted
    else:
        return nodes, edges


def adj_ls(nodes, edges, directed = False, weights = None):
    '''
    From the nodes and edges make an adjacency list

    Input:
        1. a list of nodes
        2. a list of edges
        3. optional boolean for directed edges
        4. optional argument if weights are already created
    Return:
        A dictionary where each node has a list of nodes as its neighbors
    '''
    adjlist = {}
    # if weights None:
    for node in nodes:
        adjlist[node] = []
        for edge in edges:
            if directed == True:
                if node in edge[0]:
                    if edge[1] not in adjlist[node]:
                        adjlist[node].append(edge[1])
            else:
                if node == edge[0]:
                    if edge[1] not in adjlist[node]:
                        adjlist[node].append(edge[1])
                if node == edge[1]:
                    if edge[0] not in adjlist[node]:
                        adjlist[node].append(edge[0])
    # else:
    #     for weight in weights:
    #         adjlist[weight] = adjlist[
            

    return adjlist


def adj_matrix(nodes, edges, directed = False):
    '''
    This function creates an adjacency matrix from a list of nodes and edges
    and boolean value whether

    Input:
        1. A list of nodes
        2. A list of edges
        3. True/False if directed or undirected graph
    Return:
        A list of lists representing an adjacency matrix
    '''
    matrix = []
    for node in nodes:
        helplist = []
        for node2 in nodes:
            if directed == False:
                if [node, node2] in edges or [node2, node] in edges:
                    helplist.append(1)
                else:
                    helplist.append(0)
            else:
                if [node, node2] in edges:
                    helplist.append(1)
                else:
                    helplist.append(0)
        matrix.append(helplist)
    return matrix
            


# def cgraphw(filee, delimeter):
#     '''
#     With a file we will extract a graph of nodes,edges, and weights
#     corresponding to them

#     Input:
#         A file containing graph information
#     Return:
#         A list of 
    
#     '''
#     nodes = []
#     edges = []
#     weights = {}
    
#     for line in filee:
#         info = line.split()
#         nodes.append(info[0])
#         nodes.append(info[1])
#         weights[info[0],info[1]] = info[2]
#         edges.append(info)
#     return nodes, edges, weights
