from graph.graph import Graph


class GraphEdges(Graph):
    """ Extends Graph class with method to find direct flights between cities
    """

    def find_direct_flights(self, cities):
        """ Accepts an array of city names, checks if direct flights exist
        between them, and returns a boolean indicating if a direct flight is
        possible as well as an integer representing the cost of the flight

        :param cities: list of city names (graph vertex values)
        :returns: (boolean direct flight, integer cost)
        """

        pass