import timeit
import random
# my modules
import graphgen
import io_utils
import primbasic
import primbad
import primthreaded

##           TEST GRAPH HERE ##
# V = ['A', 'B', 'D', 'C']
# E = [['A','B'], ['A', 'C'],  ['B', 'C'], ['B', 'D']]
# # Weights
# weights = {}
# weights['A', 'B'] = 3
# weights['A', 'C'] = 4
# weights['B', 'C'] = 2
# weights['B', 'D'] = 2
# #print(sprimamat.prims(V, E, weights))

# adjlist = {}
# adjlist['A'] = ['B', 'C']
# adjlist['B'] = ['A', 'C', 'D']
# adjlist['C'] = ['A', 'B']
# adjlist['D'] = ['B']
# #print(sprimamat.prims2(V, E, weights, adjlist))

iters = 10

def tests():
    pass
#################################build a complete graph and test

# Ve = [str(i) for i in range(50)]
# Ee = graphgen.complete(Ve)

# weightse = graphgen.createweights(Ee)
# adjliste = graphgen.createadj(Ve, Ee)

# t = 0
# t += timeit.timeit(stmt = "prims2(Ve, Ee, weightse, adjliste)", 
#                    setup = "from sprimamat import prims2; from __main__ import Ve, Ee, weightse, adjliste", number = iters)

# print("Mean time per PRIMS: " + str(t / iters))

## can build s,ss,t based off erdos and ba?
#################################### build a sparse graph and test

# V, E = graphgen.erdos_connected(500, 1.75)
# print("here")
# weights = graphgen.createweights(E)
# adjlist = graphgen.createadj(V, E)
# print("done with prep")
# t = 0
# t += timeit.timeit(stmt = "prims2(V, E, weights, adjlist)", 
#                    setup = "from sprimamat import prims2; from __main__ import V, E, weights, adjlist", number = iters)



# print("Mean time for sparse graph Prims2: " + str(t / iters))

# t = 0
# t += timeit.timeit(stmt = "prims(V, E, weights)", 
#                    setup = "from sprimamat import prims; from __main__ import V, E, weights", number = iters)
# print("Mean time for sparse graph Prims1: " + str(t / iters))

# t = 0
# t += timeit.timeit(stmt = "primsRIGHT(V, E, weights,adjlist)", 
#                    setup = "from sprimamat import primsRIGHT; from __main__ import V, E, weights, adjlist", number = iters)
# print("Mean time for sparse graph PrimsRIGHT: " + str(t / iters))
#################################### build a semi-sparse graph and test
'''
V, E = graphgen.erdos_connected(300, 1.5)
print("here")
weights = graphgen.createweights(E)
adjlist = graphgen.createadj(V, E)
print("done with prep")
t = 0
t += timeit.timeit(stmt = "prims2(V, E, weights, adjlist)", 
                   setup = "from sprimamat import prims2; from __main__ import V, E, weights, adjlist", number = iters)

print("Mean time for semi-sparse graph: " + str(t / iters))
'''
#################################### build a thick graph and test
'''
V, E = graphgen.erdos_connected(300, 1.75)
print("here")
weights = graphgen.createweights(E)
adjlist = graphgen.createadj(V, E)
print("done with prep")
t = 0
t += timeit.timeit(stmt = "prims2(V, E, weights, adjlist)", 
                   setup = "from sprimamat import prims2; from __main__ import V, E, weights, adjlist", number = iters)

print("Mean time for thick graph: " + str(t / iters))
'''
#################################### parse real graph and test
# V, E, weights = io_utils.cgraph('humanpathlinker.txt', True)
# print(len(V)) # 12065
# print(len(E)) # 159864




size = 0
t = 0
density = 1.25 # the density of our graph (#(V^density) edges)

with open("ignoretest2.txt", "a") as myfile:
    myfile.write("[")

while size <= 2000:
    size += 100
    V, E = graphgen.erdos_connected(size, density)
    weights = graphgen.createweights(E)
    adjlist = graphgen.createadj(V, E)
    
    # my naive prims
    t = timeit.timeit(stmt = "primsbad(V, E, weights)".format(V, E, weights),
                       setup = "from primbad import primsbad; from __main__ import V, E, weights", number = iters)
    t = t / iters
    print("bad:",t)
    
    # regular prims
    t = timeit.timeit(stmt = "prims(V, E, weights, adjlist)".format(V, E, 
                                                                    weights, 
                                                                    adjlist),
                       setup = "from primbasic import prims; from __main__ import V, E, weights, adjlist", number = iters)
    t = t / iters
    print("reg",t)
    
    # prims multithreaded
    t = timeit.timeit(stmt = "primsthread(V, E, weights, adjlist, 2)".format(V,
                                                                              E, weights, adjlist, 2), setup = "from primthreaded import primsthread; from __main__ import V, E, weights, adjlist", number = iters)
    t = t / iters
    print("thread",t)
    

    with open("ignoretest.txt", "a") as myfile:
        myfile.write(str(t) + ',')
    print(t)
with open("ignoretest.txt", "a") as myfile:
    myfile.write("]")
    

