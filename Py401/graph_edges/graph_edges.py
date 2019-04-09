from graph.graph import Graph


class GraphEdges(Graph):
    """ Extends Graph class with methods to find direct flights between cities
    """

    def get_vertex_by_value(self, val):
        """ Accepts val param, returns first vertex with matching value or None
        """
        for v in self._vertices:
            if v.value == val:
                return v
        return None

    def find_direct_flights(self, cities):
        """ Accepts an array of city names, checks if direct flights exist
        between them, and returns a boolean indicating if a direct flight is
        possible as well as an integer representing the cost of the flight

        :param cities: list of city names (graph vertex values)
        :returns: (boolean direct flight, integer cost)
        """
        cost = 0
        city_vertices = [self.get_vertex_by_value(city) for city in cities]
        if None not in city_vertices:
            departing = city_vertices[0]
            for city in city_vertices[1:]:
                found = False
                for direct_path in city.adjacencies:
                    if departing == direct_path[0]:
                        cost += direct_path[1]
                        departing = city
                        found = True
                if not found:
                    return (False, 0)
            return (True, cost)
        return (False, 0)
