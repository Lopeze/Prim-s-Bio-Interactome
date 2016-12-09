import matplotlib.pyplot as plt
import math
import random

def main():
    '''
    Create 3 graphs and plot their degree distribution
    '''
    # complete graph
    V1 = ["A"+str(n) for n in range(100)]
    E1 = complete(V1)
    V1, E1 = avgneighdeg(V1, E1)
    # sparse graph using erdos
    V2, E2 = erdos_renyi(100, 150)
    V2, E2 = avgneighdeg(V2, E2)

    # semi-dense graph
    V3, E3 = erdos_renyi(100,800)
    V3, E3 = avgneighdeg(V3, E3)

    plot_deg_dist(V2,E2,V1,E1,V3,E3)

def complete(V, weightmax = 15):
    edges = []
    for x in V:
        for y in V:
            if x != y:
                if [x,y] not in edges and [y,x] not in edges:
                    edges.append([x,y])
    if weightmax != 15: # we create weights
        weights = {}
        for edge in edges:
            weights[edge[0], edge[1]] = random.uniform(1, weightmax)
        return edges, weights
    return edges

def erdos_connected(n, connect):
    '''
    Given n nodes and a connected value function will create
    (n ** connected) edges. This will be a connected graph

    Input:
        1. n nodes
        2. connected exponent
    Output:
        1. list of edges
        2. a list of nodes
    '''
    V = ["node" + str(i+1) for i in range(n)]
    E = []
    # Do the minimum and add 
    for i in range(len(V)):
        if i == (len(V) - 1):
            E.append([V[i], V[0]])
        else:
            E.append([V[i], V[i+1]])
    counter = int((n ** connect) - n)
    
    while counter > 0:
        u = random.choice(V)
        v = random.choice(V)
        if u != v:
            if [u,v] not in E and [v,u] not in E:
                E.append([u,v])
                counter -= 1

    return V, E  # return the vertices and edges
                
def bamodel2(t, Vnum):
    V = []
    E = []
    i = 0
    for i in range(Vnum):
        node = 'A' + str(i)
        V.append(node)
        degreelist.append(node)

    
    n = len(V) 
    while t != 0:
        target = 'A' + str(n)
        source = random.choice(degreelist)
        source2 = random.choice(degreelist)
        while source2 == source:
            source2 = random.choice(degreelist)
        V.append(target)
        E.append([source,target])
        E.append([source2,target])

        degreelist.append(source)
        degreelist.append(target)
        degreelist.append(source2)
        degreelist.append(target)
        n += 1
        t -= 1

    return V,E

                
def bamodel(t,V,E):
    # t = time to build
    # V is the set of vertices
    # E is the set of edges
    # first build big list of degrees
    degreelist = []
    for edge in E:
        degreelist += edge[0]
        degreelist += edge[1]

    n = len(V) + 1 
    while t != 0:
        target = str(n)
        source = random.choice(degreelist)
        source2 = random.choice(degreelist)
        while source2 == source:
            source2 = random.choice(degreelist)
            V.append(target)
            E.append([source,target])
            E.append([source2,target])

        degreelist.append(source)
        degreelist.append(target)
        degreelist.append(source2)
        degreelist.append(target)
        n += 1
        t -= 1

    return V,E

def createweights(edges):
    # Given a list of edges, create random weights for each edge

    weights = {}
    for edge in edges:
        weights[edge[0],edge[1]] = random.randint(1, 100)
    return weights

def createadj(nodes, edges):
    # Given a list of nodes and edges, create the adjacency list

    adjlist = {}
    for node in nodes:
        adjlist[node] = []
    for edge in edges:
        adjlist[edge[0]].append(edge[1])
        adjlist[edge[1]].append(edge[0])
    return adjlist

def avgneighdeg(V,E):
    # Given a list of nodes and edges, find the average neighbor degree
    # Output a list of degrees and its avgneighbors degree

    # make a dictionary mapping nodes to their degree
    degreedict = {}
    tnode = len(V)
    for n in V:
        if n not in degreedict:
            degreedict[n] = 0
        for x in V:
            if [n,x] in E or [x,n] in E:
                degreedict[n] += 1
    # Now we go through each node, finding the neighbors. Once we have neighbors we will lookup their degree and take the mean
    neighdeg = {}
    for n in V:
        # list of neighbors
        templ = []
        degree = 0
        for x in V:
            if [n,x] in E or [x,n] in E:
                templ.append(x)
        for x in templ:
            degree += degreedict[x]
        if len(templ) != 0:
            avgdegree = degree / len(templ)
        # assign n's value to be the avg degree of its neighbors
        neighdeg[n] = avgdegree
    # neighdeg now has each node with its avg neighbor degree
    degree = []
    avgdegree = []
    for n in neighdeg:
        degree.append(degreedict[n])
        avgdegree.append(neighdeg[n])
    return degree,avgdegree
        

def plot_deg_dist(x1,y1,x2,y2,x3,y3):
    fig = plt.figure(figsize=(10,6)) # make a 10" wide by 6" tall figure

    plt.subplot(1,3,1)              # in a 1-by-2 grid, 1st subplot
    plt.plot(x1,y1,'ro')             # plot a red line with circles
    plt.xlabel('degree')
    plt.ylabel('average neighbor degree')
    plt.title("Sparse graph")

    plt.subplot(1,3,2)              # in a 1-by-2 grid, 2nd subplot
    plt.plot(x2,y2,'ro')       # plot a blue line with squares
    plt.xlabel('degree')
    plt.ylabel('average neighbor degree')
    plt.title("Dense graph")

    plt.subplot(1,3,3)              # in a 1-by-2 grid, 2nd subplot
    plt.plot(x3,y3,'ro')       # plot a blue line with squares
    plt.xlabel('degree')
    plt.ylabel('average neighbor degree')
    plt.title("Semi-Dense graph")
    
    plt.tight_layout()              # make the labels "snap" to the grid
                                    # this may emit a warning, which is OK
    plt.savefig("GenData.png")    # save figure as PNG
    plt.savefig("GenData.pdf")    # optionally, save figure as PDF
    print('wrote to Networks.png')
    return


     
if __name__ == "__main__":
    main()
