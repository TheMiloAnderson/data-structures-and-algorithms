from stacks_and_queues.stacks_and_queues import Queue


class Graph(object):
    """ Implements a graph """

    def __init__(self):
        self._vertices = set()

    def add_vertex(self, val):
        """ Creates a new Vertex object with given value, adds it to graph
        collection, and returns the new Vertex object

        :param val: any value
        :returns: new Vertex object
        """
        vert = Vertex(val)
        self._vertices.add(vert)
        return vert

    def add_edge(self, vert1, vert2, weight=0):
        """ Adds an edge between two given nodes, if they both exist in the graph

        :param vert1: Vertex object
        :param vert2: Vertex object
        :param weight: integer; default=0
        """
        if vert1 in self._vertices and vert2 in self._vertices:
            vert1.adjacencies.append((vert2, weight))
            vert2.adjacencies.append((vert1, weight))

    def get_vertices(self):
        """ Returns a set of all vertices in the graph
        """
        return self._vertices

    def get_neighbors(self, vert):
        """ Returns a list of tuples representing vertices connected to
        the given vertex, and the weight of the connection

        :param vert: Vertex object
        :returns: [(vertext obj, weight int)]
        """
        return vert.adjacencies

    def size(self):
        """ Returns an integer count of the number of vertexes in the graph
        """
        return len(self._vertices)

    def breadth_first_traverse(self, start_vert):
        """ Returns a list of graph vertex values in breadth-first order

        :param start_vert: Vertex object
        :returns: list of vertex values
        """
        q = Queue()
        output = []
        q.enqueue(start_vert)
        start_vert.visited = True
        while q.peek():
            vert = q.dequeue()
            output.append(vert.value)
            for v, w in vert.adjacencies:
                if not v.visited:
                    q.enqueue(v)
                    v.visited = True
        # reset .visited so we can traverse again
        for v in self._vertices:
            v.visited = False
        return output

    def does_path_exist(self, vert1, vert2):
        """ Returns boolean indicating whether a path connects two vertices

        :param vert1: Vertex object
        :param vert2: Vertex object
        :returns: boolean
        """
        if vert1.value in self.breadth_first_traverse(vert2):
            return True
        return False

    def __repr__(self):
        return str(self.__class__) + str(self.__dict__)

    def __str__(self):
        return f'<Graph object with {len(self._vertices)} vertices>'


class Vertex(object):
    """ Implements a vertex object, for use in graphs """

    def __init__(self, val):
        self.value = val
        self.adjacencies = []
        self.visited = False

    def __repr__(self):
        return str(self.__class__) + str(self.__dict__)

    def __str__(self):
        return f'<Vertex object {self.value}>'
