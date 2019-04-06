class Graph(object):
    """ Implements a graph """

    def __init__(self):
        self._vertices = set()

    def add_vertex(self, val):
        vert = Vertex(val)
        self._vertices.add(vert)
        return vert

    def add_edge(self, vert1, vert2, weight=0):
        if vert1 in self._vertices and vert2 in self._vertices:
            vert1.adjacencies.append((vert2, weight))
            vert2.adjacencies.append((vert1, weight))

    def get_vertices(self):
        return self._vertices

    def get_neighbors(self, vert):
        return vert.adjacencies

    def size(self):
        return len(self._vertices)

    def __repr__(self):
        return str(self.__class__) + str(self.__dict__)

    def __str__(self):
        return f'<Graph object with {len(self._vertices)} vertices>'


class Vertex(object):
    """ Implements a vertex object, for use in graphs """

    def __init__(self, val):
        self.value = val
        self.adjacencies = []

    def __repr__(self):
        return str(self.__class__) + str(self.__dict__)

    def __str__(self):
        return f'<Vertex object {self.value}>'
