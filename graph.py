'''
CREATED BY: JARED RAY NELSON
DATE: 06-24-2021
CLASS: CS2420
'''

import math
class Graph():
    '''
    IMPLEMENTS A GRAPH
    '''
    def __init__(self):
        '''
        HAS SEVERAL METHODS WHICH KEEP TRACK
        OF VERTICES, EDGE WEIGHT, CONNECTIONS
        AND DFS VISITED
        '''
        self.verteces = []
        self.edge_weight = {}
        self.edge_connections = {}
        self.dfs_visted = []

    def __str__(self):
        '''
        PRINT METHOD
        '''
        tmp_str = ''
        tmp_str += 'digraph G {'
        for i in self.edge_weight.keys():
            tmp_str += ('\n   '+i[0] +' -> ' + i[1] +
                    ' [label=\"'+ str(self.edge_weight[i]) +
                    '\",'+'weight=\"'+str(self.edge_weight[i])+
                    '\"];')
        tmp_str += '\n}\n'
        return tmp_str


    def add_vertex(self, label):
        '''
        ADDS A VERTEX TO THE GRAPH
        '''
        if not isinstance(label, str):
            raise ValueError
        self.verteces.append(label)
        self.edge_connections[label] = []
        return self

    def add_edge(self, source, destination, weight):
        '''
        THIS WILL PIECE TOGETHER THE VERTECES & CREATE
        A GRAPH, THEN THE TOTAL GRAPH WILL BE RETURNED
        '''
        if not ((isinstance(weight, float)) or (isinstance(weight, int))):
            raise ValueError

        if not (source in self.verteces and destination in self.verteces):
            raise ValueError

        self.edge_weight[(source, destination)] = weight
        self.edge_connections[source].append(destination)
        return self

    def get_weight(self, source, destination):
        '''
        RETURNS A FLOAT OF THE WEIGHT VALUE
        '''
        if not (source in self.verteces and destination in self.verteces):
            raise ValueError
        if not (source, destination) in self.edge_weight.keys():
            return math.inf
        if self.edge_weight[(source, destination)]:
            return float(self.edge_weight[(source, destination)])

    def bfs(self, start_vertex):
        '''
        BREADTH FIRST SEARCH
        RETURNS LIST OF TRAVERSED
        ALGORITHM
        '''
        traversed_verteces = []
        Q = []
        if start_vertex not in self.verteces:
            raise ValueError
        Q.append(start_vertex)
        while Q:
            if self.edge_connections[start_vertex] == []:
                traversed_verteces.append(Q.pop(0))
                if Q == []:
                    break
                start_vertex = Q[0]
                continue
            for i in self.edge_connections[start_vertex]:
                if not (i in traversed_verteces or i in Q):
                    Q.append(i)
            traversed_verteces.append(Q.pop(0))
            if Q:
                start_vertex = Q[0]

        return traversed_verteces

    def dfs(self, start_vertex):
        '''
        SIMILAR TO PREORDER
        RETURNS A LIST OF THE
        VERTICES
        '''
        self.dfs_visted = []
        self._dfs(start_vertex)
        return self.dfs_visted

    def _dfs(self, start_vertex):
        if start_vertex not in self.verteces:
            raise ValueError
        if start_vertex in self.dfs_visted:
            return

        if start_vertex not in self.dfs_visted:
            self.dfs_visted.append(start_vertex)

        if self.edge_connections[start_vertex] == []:
            return

        for i in self.edge_connections[start_vertex]:
            self._dfs(i)
        return

    def dijkstra(self, source_vertex):
        '''
        IMPLEMENTS DIJKSTRA'S METHOD AND FINDS THE DISTANCE OF
        PATH.
        '''
        return self._dijkstra(self.verteces, self.edge_weight, source_vertex)

    def _dijkstra(self, verteces, edges, source_vertex):
        '''
        HELPER FUNCTION FOR DIJKSTRA
        '''
        path_lengths = {v: float(math.inf) for v in verteces}
        path_lengths[source_vertex] = 0
        # previous_vertex = None

        adjacent_nodes = {v: {} for v in verteces}
        paths_source_2_destination = {v: [] for v in verteces}
        # {'A':[], 'B':[], 'C':[], 'D':[], 'E':[], 'F':[], 'G':[]}
        paths_source_2_destination[source_vertex].append(source_vertex)

        for (source, destination), dist_between_source_n_destination in edges.items():
            adjacent_nodes[source][destination] = dist_between_source_n_destination
            adjacent_nodes[destination][source] = dist_between_source_n_destination

        temp_nodes = [v for v in verteces]
        while temp_nodes:
            upper_bounds = {v: path_lengths[v] for v in temp_nodes}
            smallest_path_len = min(upper_bounds, key=upper_bounds.get)

            # POSSIBLE FUNCTION CALL
            previous_vertex = temp_nodes.pop(temp_nodes.index(smallest_path_len))

            for destination, distance in adjacent_nodes[smallest_path_len].items():
                path_lengths[destination] = (min(path_lengths[destination],
                                        path_lengths[smallest_path_len] + distance))

        return path_lengths, adjacent_nodes


    def dsp(self, source_vertex, destination_vertex):
        '''
        RETURNS TUPLE OF (VALUE OF SHORTEST PATH &
        [PATH SOURCE TO DESTINATION])
        '''
        if source_vertex == destination_vertex:
            return (0, [source_vertex])
        # THESE ARE ALL INFINITIY
        path_lengths = {v: float(math.inf) for v in self.verteces}
        path_lengths[source_vertex] = 0
        # previous_vertex = None

        adjacent_nodes = {v: {} for v in self.verteces}
        paths_source_2_destination = {v: [] for v in self.verteces}
        paths_source_2_destination[source_vertex] = [source_vertex]
        # {'A':[], 'B':[], 'C':[], 'D':[], 'E':[], 'F':[], 'G':[]}
        for (source, destination), dist_between_source_n_destination in self.edge_weight.items():
            adjacent_nodes[source][destination] = dist_between_source_n_destination
            # IF YOU WANT TO MAKE THIS BIDIRECTIONAL, UNCOMMENT THE LINE BELOW.
            # adjacent_nodes[destination][source] = dist_between_source_n_destination
        # THE CASE THAT IT'S NOT CONNECTED TO ANYTHING.


        if adjacent_nodes[source_vertex] == {}:
            if destination_vertex == source_vertex:
                return (math.inf, paths_source_2_destination[destination_vertex])
            else:
                return (math.inf, [])

        temp_nodes = [v for v in self.verteces]
        while temp_nodes:
            upper_bounds = {v: path_lengths[v] for v in temp_nodes}
            smallest_path_len = min(upper_bounds, key=upper_bounds.get)

            temp_nodes.pop(temp_nodes.index(smallest_path_len))

            for dest, distance in adjacent_nodes[smallest_path_len].items():
                if dest == source_vertex:
                    continue
                else:
                    path_lengths[dest] = (min(path_lengths[dest],
                                    path_lengths[smallest_path_len] + distance))
                    if (path_lengths[smallest_path_len] + distance) == path_lengths[dest]:
                        paths_source_2_destination[dest] = (paths_source_2_destination[smallest_path_len]
                                                         + [dest])

        return (path_lengths[destination_vertex], paths_source_2_destination[destination_vertex])


    def dsp_all(self, source_vertex):
        '''
        PRINTS THE PATH TO EACH NODE FROM THE SOURCE
        '''
        all_destinations = {}

        for destination in self.verteces:
            all_destinations[destination] = self.dsp(source_vertex, destination)[1]

        return all_destinations

