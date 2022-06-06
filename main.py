from graph import Graph

def main():

    g = Graph()

    g.add_vertex(('A'))
    g.add_vertex(('B'))
    g.add_vertex(('C'))
    g.add_vertex(('D'))
    g.add_vertex(('E'))
    g.add_vertex(('F'))

    g.add_edge('A','B', 2.00)
    g.add_edge('A','F', 9.00)
    g.add_edge('B','C', 8.00)
    g.add_edge('B','D', 15.0)
    g.add_edge('B','F', 6.00)
    g.add_edge('C','D', 1.00)
    g.add_edge('E','C', 7.00)
    g.add_edge('E','D', 3.00)
    g.add_edge('F','B', 6.00)
    g.add_edge('F','E', 3.00)

    print(g)
    # print('DFS METHOD:', g.dfs('A'))
    

    print("Starting BFS with vertex A") 
    for vertex in g.bfs("A"):
        print(vertex, end = "")
    print('\n')

    print("Starting DFS with vertex A") 
    for vertex in g.dfs("A"):
        print(vertex, end = "")
    print('\n')

    # print('BFS METHOD:', g.bfs('A'))
    print('A->F', g.dsp('A','F'))
    print('A->B', g.dsp('A','B'))
    print('A->C', g.dsp('A','C'))
    print('A->D', g.dsp('A','D'))
    print('A->E', g.dsp('A','E'))

if __name__ == '__main__':
    main()