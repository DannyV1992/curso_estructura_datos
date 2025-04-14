from GraphKruskal import Graph

def main():
    #g = Graph(4)
    #g.addEdge(0, 1, 10)
    #g.addEdge(0, 2, 6)
    #g.addEdge(0, 3, 5)
    #g.addEdge(1, 3, 15)
    #g.addEdge(2, 3, 4)
    g = Graph(9)
    g.addEdge(0,1,4)
    g.addEdge(0,8,8)
    g.addEdge(1,2,8)
    g.addEdge(1,8,11)
    g.addEdge(2,7,2)
    g.addEdge(2,5,4)
    g.addEdge(2,3,7)
    g.addEdge(3,4,9)
    g.addEdge(3,5,14)
    g.addEdge(4,5,10)
    g.addEdge(5,6,2)
    g.addEdge(6,8,1)
    g.addEdge(6,7,6)
    g.addEdge(7,8,7)

    # Function call
    g.KruskalMST()
 

if __name__ == "__main__":
    main()