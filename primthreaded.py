from threading import Thread
import io_utils
import graphgen
def main():
    '''
    Build our graph
    '''

    V = ['A', 'B', 'D', 'C']
    E = [['A','B'], ['A', 'C'],  ['B', 'C'], ['B', 'D']]
    # Weights
    weights = {}
    weights['A', 'B'] = 3
    weights['A', 'C'] = 4
    weights['B', 'C'] = 2
    weights['B', 'D'] = 2
    #print(prims(V, E, weights))

    adjlist = {}
    adjlist['A'] = ['B', 'C']
    adjlist['B'] = ['A', 'C', 'D']
    adjlist['C'] = ['A', 'B']
    adjlist['D'] = ['B']
    print(primsthread(V, E, weights, adjlist, 2))

    
    V, E, weights = io_utils.cgraph('textbookgraph.txt', True)
    adjlist = graphgen.createadj(V, E)
    print("ERRRRRRRRRRRRRRR", weights)
    print("\n HEYO:",adjlist)
    print(V)
    print(primsthread(V, E, weights, adjlist, 2))


def choosesmallest(nodes, preque, xs, index):
    key = "key"
    minn = 1001
    for node in nodes:
        if preque[node][key] < minn:
            minn = preque[node][key]
            minode = node
    xs[index] = (minode, minn)
    return

def primsthread(nodes, edges, weights, adjlist, threadnum):
    '''
    This is the same as primsbasic except that we now have a "multithreaded
    version". GIL still locks us to having one thread execute at a time but
    this for a proof of concept.
    Runtime: O((V^2) / threadnum)
    
    Input:
    Return:

    '''
    nonforest = {} # min weight for each vertex
    forest = {} # what we end with key:value is node->(edge, edgevalue)
    parent = "parent"
    key = "key"
    for node in nodes:
        nonforest[node] = {}
        nonforest[node]['parent'] = 'nil'
        nonforest[node]['key'] = 1000
        forest[node] = {}

    # set our first node to have a distance 0
    nonforest[nodes[0]]['key'] = 0
    lenque = len(nonforest)
    xs = [('nil',1001)] * (lenque // threadnum) # this will contain each answer
                                                # to each thread
    threadslist = [None for i in range(threadnum)] # list containing threads
    nodelist = list(nodes)
    while nonforest: # while the forest is not complete

        division = lenque // threadnum # for when we have 2 threads
        minn = 1001
        
        if division == 0: # serial prims when less elements than threads
            for anode in nonforest:
                if nonforest[anode]['key'] < minn:
                    minn = nonforest[anode]['key']
                    minode = anode
        else:
            left = 0
            right = division
            for i in range(threadnum):
                if i == (lenque - division):
                    threadslist[i] = Thread(target = choosesmallest, args = 
                                            (nodelist[left:], nonforest, xs,
                                             i,))
                else:
                    threadslist[i] = Thread(target = choosesmallest, args = 
                                            (nodelist[left:right], nonforest,
                                             xs, i,))
                    
                threadslist[i].start()
                left = right
                right += division
        
            # Wait for all threads to finish
            for i in range(threadnum):
                threadslist[i].join()
            

            pair = min(xs, key = lambda t: t[1])
            minode = pair[0]

        lenque -= 1 # we are going to take a node out of queue
                    # so we need to account for that
        # save what we just took out of the queue/nforest
        forest[minode]['parent'] = nonforest[minode]['parent']
        forest[minode]['key'] = nonforest[minode]['key']
        del nonforest[minode]
        nodelist.remove(minode)

        # change the weights of nodes in nonforest if they have a 
        # low weight edge that connects node in forest to node in nonforest
        for node in adjlist[minode]:
            if (minode, node) in weights and node in nonforest:
                if weights[(minode, node)] < nonforest[node]['key']:
                    nonforest[node]['key'] = weights[(minode, node)]
                    nonforest[node]['parent'] = minode

            if (node, minode) in weights and node in nonforest:
                if weights[(node, minode)] < nonforest[node][key]:
                    nonforest[node][key] = weights[(node, minode)]
                    nonforest[node][parent] = minode

    return forest

main()
