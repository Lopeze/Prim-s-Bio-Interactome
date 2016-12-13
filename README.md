
## Erik Lopez
## Prims Algorithm
## Exploring Python Multithreading and Multiprocessing modules
This repo focuses on experimenting with Multithreading and Multiprocessing python modules. I benchmarked a simple embarrassingly parallel problem with 4 different versions and then tried to mulithread Prims, a greedy minimal spanning tree graph algorithm. I have two versions of Prims which are rather naive but there to see what "performance gain" we can get by attempting parallel code.  
**System**: Genome 3.14.1
### File Hierarchy:
**Embarrassingly Parallel Folder**:
- easybenches.py: 4 different versions of a way to solve an embarrassingly parallel problem
- graphgenforeasy.py: python script to generate a benchmarked graph
- easybenches.png: benchmarked graph  

**There are 3 implementations of Prims**:  
- primbad.py
- primbasic.py
- primthreaded.py  

**Benchmarks for Graphs**:  
- There are two different types of graphs, dense graphs(E = V^n where n = 1.75) and sparse graphs (n = 1.25), and the folders DenseGraphs and SparseGraphs have benchmarks for those graphs respectively.  
- speeds.py: benchmark the graphs of a specific size and write to different text files(change these text files if you want them to write to different files) 

**SparseGraphs**:
- sparsegraphgen.py: script to generate graphs based off data from benchmarking different Prim's versions on sparse graphs
- sparse.png: graph with benchmarked prims algorithm  

**DenseGraphs**:
- densegraphgen.py: script to generate graphs based off data from benchmarking different Prim's versions on dense graphs
- dense.png: graph with benchmarked prims algorithm

**Graph creation**:
- graphgen.py: creates the Erdos Renyi Model graphs for our tests
- io_utils.py: creates our adjacency list needed for input to Prim's algorithm

**Benchmarking**:
- speeds.py: code to calculate how long Prim's will take on a graph

**Biological Dataset**:
- background-interactome-pathlinker-2015:txt: A human interactome dataset fetched from http://www.nature.com/articles/npjsba20162

