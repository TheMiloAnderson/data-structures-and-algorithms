# Graphs

## Challenge
Implement your own Graph, represented internally as a adjacency list

## Approach & Efficiency
Defined classes for Graph and Vertex. Graph has _vertices attribute, which holds a set of the graph's vertices. Vertex class has value & adjacencies attributes; adjacencies are represented as a tuple of the related vertex object and an edge weight integer.

## API
**AddNode(value)**
Takes in a value for the new node; adds a new node to the graph; returns the added node

**AddEdge(vertex_1, vertex_2, weight)**
Adds a new edge between two vertices in the graph; accepts two vertex objects and a weight integer; both vertexes must already exist in the graph or nothing happens

**GetNodes()**
Returns a set of all of the nodes in the graph

**GetNeighbors(vertex)**
Accepts a vertex object as parameter; returns connected vertices as a list of (vertex, weight) tuples

**Size()**
Returns the total number of vertices in the graph