from threading import Thread
from multiprocessing import Process
import timeit

def main():
    '''
    The benchmarking section of the code
    '''
    t = 0
    sizel, threadedl, nonthreadedl, multiprocessl, simplel = ([] for i in range
                                                              (5))
    d = 250
    iters = 100
    while d <= 400000:
        print("About to start iterations with size {:d}".format(d))
        d = d * 2
        t = timeit.timeit(stmt = "threads({:d})".format(d), 
                          setup = "from __main__ import threads, testmethread", number = iters)
        t = t / iters
        print("Time for threads is: {:f}".format(t))

        t = timeit.timeit(stmt = "nothreads({:d})".format(d), 
                          setup = "from __main__ import nothreads, testmethread", number = iters)
        t = t / iters
        print("Time for nothreads is: {:f}".format(t))


        t = timeit.timeit(stmt = "mutliproc({:d}, 4)".format(d), 
                          setup = "from __main__ import mutliproc, testmethread", number = iters)
        t = t / iters
        print("Time for mutliproc is: {:f}".format(t))

        t = timeit.timeit(stmt = "serial({:d})".format(d), 
                          setup = "from __main__ import serial, testmethread", number = iters)
        t = t / iters
        print("Time for serial is: {:f}".format(t))
        print("\n\n")

def testmethread(xs, left, right):
    '''
    This is the embarrassinly parallel code that will be run to benchmark
    the threaded, multiprocessed, serial w/ overhead, and basic serial version
    
    Input:
        1. a list of elements
        2. a left bound that determines what elements work on
        3. a right bound
    '''
    i = left
    while i < right:
        if xs[i] % 2:
            xs[i] += 1
        i += 1
    return

def serial(size):
    '''
    This is the serial version of doing an embarrassingly parallel task in 
    serial without creating any artifical overhead.
    Input:
        size of list that will be worked on in serial
    '''
    xs = [1 for i in range(size)]
    testmethread(xs, 0, size)
    return

def threads(size):
    '''
    This is the threaded version

    Input:
        size of list that will be split up by threads
    '''
    xs = [i-1 for i in range(size)]
    threadshere = [None] * 2
    division = size // len(threadshere)
    left = 0
    right = division
    for i in range(2):
        threadshere[i] = Thread(target = testmethread, args = (xs, left, right,))
        threadshere[i].start()
        left = right
        right += division

    for node in threadshere:
        node.join()

        return

def nothreads(size):
    '''
    This is imitating both the threaded and the multiprocessed version by 
    creating the same amount of containers needed, but does all the work 
    serially.

    Input:
        size of list that will be worked on serially
    '''
    xs = [i for i in range(size)]
    threadshere = [None] * 4
    division = size // len(threadshere)
    left = 0
    right = division
    for i in range(4):
        testmethread(xs, left, right)
        left = right
        right += division

    return


def mutliproc(size, cores):
    '''
    This is a multiproccessed version
    Input:
        size of list that processes split up and work on
    '''
    xs = [i for i in range(size)]
    threadshere = [None] * cores 
    division = size // cores
    left = 0
    right = division
    for i in range(cores):
        threadshere[i] = Process(target = testmethread, args = (xs, left, 
                                                                right,))
        threadshere[i].start()
        left = right
        right += division

    for node in threadshere:
        node.join()

    return

if __name__ == "__main__":
    main()
