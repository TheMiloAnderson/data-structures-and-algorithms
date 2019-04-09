from graph_edges.graph_edges import GraphEdges
import pytest


@pytest.fixture
def graph():
    g = GraphEdges()
    pan = g.add_vertex('Pandora')
    are = g.add_vertex('Arendelle')
    met = g.add_vertex('Metroville')
    mon = g.add_vertex('Monstropolis')
    nab = g.add_vertex('Naboo')
    nar = g.add_vertex('Narnia')
    g.add_edge(pan, are, 150)
    g.add_edge(pan, met, 82)
    g.add_edge(are, met, 99)
    g.add_edge(are, mon, 42)
    g.add_edge(met, mon, 105)
    g.add_edge(nab, met, 26)
    g.add_edge(nab, mon, 73)
    g.add_edge(nar, met, 37)
    g.add_edge(nar, nab, 250)
    return g


def test_direct_flight_one(graph):
    flights = graph.find_direct_flights([
        'Metroville',
        'Pandora'
    ])
    assert flights == (True, 82)


def test_direct_flights_many(graph):
    flights = graph.find_direct_flights([
        'Arendelle',
        'Monstropolis',
        'Naboo'
    ])
    assert flights == (True, 115)

    flights = graph.find_direct_flights([
        'Arendelle',
        'Monstropolis',
        'Naboo',
        'Metroville',
        'Monstropolis'
    ])
    assert flights == (True, 246)


def test_direct_flights_back_and_forth(graph):
    flights = graph.find_direct_flights([
        'Pandora',
        'Arendelle',
        'Pandora',
        'Arendelle'
    ])
    assert flights == (True, 450)


def test_no_direct_flights_one(graph):
    flights = graph.find_direct_flights([
        'Naboo',
        'Pandora'
    ])
    assert flights == (False, 0)


def test_no_direct_flights_many(graph):
    flights = graph.find_direct_flights([
        'Narnia',
        'Arendelle',
        'Naboo'
    ])
    assert flights == (False, 0)


def test_direct_flights_some_but_not_others(graph):
    flights = graph.find_direct_flights([
        'Arendelle',
        'Monstropolis',
        'Narnia'
    ])
    assert flights == (False, 0)


def test_direct_flights_city_not_in_graph(graph):
    flights = graph.find_direct_flights([
        'Narnia',
        'Arendelle',
        'Bogus City Name'
    ])
    assert flights == (False, 0)
