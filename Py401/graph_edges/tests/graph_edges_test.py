from graph_edges.graph_edges import GraphEdges


def test_direct_flights():
    g = GraphEdges()
    pan = g.add_vertex('Pandora')
    are = g.add_vertex('Arendelle')
    met = g.add_vertex('Metroville')
    mon = g.add_vertex('Monstropolis')
    nab = g.add_vertex('Naboo')
    nar = g.add_vertex('Narnia')
    g.add_edge(pan, are, 150)
    g.add_edge(are, met, 99)
    g.add_edge(are, mon, 42)
    g.add_edge(met, mon, 105)
    g.add_edge(nab, met, 26)
    g.add_edge(nab, mon, 73)
    g.add_edge(nar, met, 37)
    g.add_edge(nar, nab, 250)

    flights = g.find_direct_flights([Metroville, Pandora])
    assert flights == (True, 82)

    flights = g.find_direct_flights([Arendelle, New Monstropolis, Naboo])
    assert flights == (True, 115)

    flights = g.find_direct_flights([Naboo, Pandora])
    assert flights == (False, 0)

    flights = g.find_direct_flights([Narnia, Arendelle, Naboo])
    assert flights == (False, 0)
