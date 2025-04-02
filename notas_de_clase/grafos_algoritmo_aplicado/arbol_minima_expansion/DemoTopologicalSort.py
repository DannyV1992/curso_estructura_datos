from GraphVariant1 import Graph

def main():
    #g = Graph(6)
    #g.addEdge(5, 2)
    #g.addEdge(5, 0)
    #g.addEdge(4, 0)
    #g.addEdge(4, 1)
    #g.addEdge(2, 3)
    #g.addEdge(3, 1)

    g = Graph(8)
    g.addEdge(0, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 2)
    g.addEdge(3, 2)
    g.addEdge(4, 3)
    g.addEdge(4, 7)
    g.addEdge(5, 4)
    g.addEdge(5, 7)
    g.addEdge(6, 7)

    print ("Following is a Topological Sort of the given graph")
 
    # Function Call
    g.topologicalSort()


if __name__ == "__main__":
    main()