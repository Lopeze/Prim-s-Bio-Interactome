import graphgen
import io_utils

'''
main function runs a sample graph to test on. This file contains
our very simple Prims algorithm that has the expected O(V^2) run
time.
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

    adjlist = {}
    adjlist['A'] = ['B', 'C']
    adjlist['B'] = ['A', 'C', 'D']
    adjlist['C'] = ['A', 'B']
    adjlist['D'] = ['B']
    print(prims(V, E, weights, adjlist))

def prims(nodes, edges, weights, adjlist):
    '''
    This should be the correct implementation of what prims algorithm states in
    "insert textbook here". We start with an arbitrary node in set "forest" and the rest of the nodes are in the set "nonforest". We iteratively add one node from nonforest into forest if and only if the edge that connects the nonforest node to the forest node is the lowest weight edge possible.
    Runtime: O(V^2)
    Input:
        1. a set of nodes for a graph
        2. a set of edges representing a graph
        3. a dictionary of edges and their weights
        4. dictionary of nodes and their adjacent neighbors
    Return:
        a forest representing the minimal spanning tree
    '''
    nonforest = {} # min weight for each vertex
    forest = {} # what we end with key:value is node->(edge, edgevalue)
    parent = "parent"
    key = "key"
    for node in nodes:
        nonforest[node] = {}
        nonforest[node][parent] = 'nil'
        nonforest[node][key] = 1000
        forest[node] = {}

    # set our first node to have a distance 0
    nonforest[nodes[0]][key] = 0
    while nonforest: # while the forest is not complete
        minn = 1001

        # search for the smallest weight edge so we can add a new node to forest
        for anode in nonforest:
            if nonforest[anode][key] < minn:
                minn = nonforest[anode][key]
                minode = anode

        # put our new node and its edge into forest
        forest[minode][parent] = nonforest[minode][parent]
        forest[minode][key] = nonforest[minode][key]
        del nonforest[minode]

        # change the weights of  nodes in nonforest if they have a 
        # low weight edge that connects node in forest to node in nonforest
        for node in adjlist[minode]:
            if (minode, node) in weights and node in nonforest:
                if weights[(minode, node)] < nonforest[node][key]:
                    nonforest[node][key] = weights[(minode, node)]
                    nonforest[node][parent] = minode

            if (node, minode) in weights and node in nonforest:
                if weights[(node, minode)] < nonforest[node][key]:
                    nonforest[node][key] = weights[(node, minode)]
                    nonforest[node][parent] = minode

    return forest

if __name__ == "__main__":
    main()
