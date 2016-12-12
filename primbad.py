import io_utils
import graphgen

'''
This is the implementation of a bad prims that has a runtime 
that has E in its asymptotic notation. This is particularly 
bad if you are generating graphs where E = V^n. main function
has a sample graph to test out our version of prims on a very 
small simple graph.
'''
def main():

    V = ['A', 'B', 'D', 'C']
    E = [['A','B'], ['A', 'C'],  ['B', 'C'], ['B', 'D']]
    # Weights
    weights = {}
    weights['A', 'B'] = 3
    weights['A', 'C'] = 4
    weights['B', 'C'] = 2
    weights['B', 'D'] = 2

    # Adjlist 
    adjlist = {}
    adjlist['A'] = ['B', 'C']
    adjlist['B'] = ['A', 'C', 'D']
    adjlist['C'] = ['A', 'B']
    adjlist['D'] = ['B']
    print(primsbad(V, E, weights))

    

def primsbad(nodes, edges, weights):
    '''
    Runtime: O(EV^2)

    This is a quick and fast implementaton of prims aglorithm. While it is not
    technically prims, the motivation for finding the minimal spanning tree is 
    similar by having two sets of nodes, a forest and a nonforest, and iterate 
    through all possible edges looking for edges that have a node in forest and
    one in the nonforest. We then add an edge to the forest if it is the lowest
    weight edge that can be added to our forest.

    Input:
        1. A set of nodes
        2. A set of edges which represent the connections in our graph
        3. A edge weight dictionary
    Return:
        1. A minimal spanning tree that is a dictionary with nodes: parent node
        and edge weight
    '''
    forweight = {} # min weight for each vertex

    forest = [nodes[0]] # place first node into forest and to dictionary
    forweight[nodes[0]] = {}
    forweight[nodes[0]]['key'] = 0
    forweight[nodes[0]]['parent'] = None

    nforest = nodes[1::] # put all nodes except first to the nonforest set


    while nforest: # while the forest is not complete
        edged = []
        minn = 1000
        for edge in edges:
            if weights[edge[0],edge[1]] < minn:
                # check only edges that have a vertex in forest and nforest
                if edge[0] in forest and edge[1] in nforest:
                    minn = weights[edge[0],edge[1]] # value of smallest edge
                    nforout = edge[1] # node that will come out of nforest
                    edged = [edge[0],edge[1]] # saving edge positions
                if edge[1] in forest and edge[0] in nforest: # other case
                    minn = weights[edge[0],edge[1]]
                    nforout = edge[0]
                    edged = [edge[1], edge[0]]

        forweight[edged[1]] = {}
        forweight[edged[1]]['key'] = minn
        forweight[edged[1]]['parent'] = edged[0]

        nforest.remove(nforout)
        forest.append(nforout)

    return forweight

if __name__ == "__main__":
    main()
