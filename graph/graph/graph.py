class Node:
   
    def __init__(self,value):
        self.value = value

class Edge:


  def __init__(self, vertex, weight):
    self.vertex = vertex
    self.weight = weight

class Graph:

    def __init__(self):
         self.__adjacency_list = {}

    def add_node(self, value):
        """
            Arguments: value
            Returns: The added node
            Add a node to the graph
        """
        v = Node(value)
        self.__adjacency_list[v] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """ Arguments: 2 nodes to be connected by the edge, weight (optional)
            Returns: nothing
            Adds a new edge between two nodes in the graph
            If specified, assign a weight to the edge
            Both nodes should already be in the Graph
        """
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")
      
        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)


    def get_nodes(self):
        """
            Arguments: none
            Returns all of the nodes in the graph as a collection (set, list, or similar)

        """
        return self.__adjacency_list.keys()
    
    def get_neighbors(self, vertex):
        """
            Arguments: node
            Returns a collection of edges connected to the given node
            Include the weight of the connection in the returned collection
        """
        return self.__adjacency_list.get(vertex, [])

    def size(self):
        """
            Arguments: none
            Returns the total number of nodes in the graph
        """
        return len(self.__adjacency_list)