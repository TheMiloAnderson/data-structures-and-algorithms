from graph.graph import Graph


def test_class():
    assert Graph


def test_instance():
    assert Graph()


def test_add_one_vertext():
    g = Graph()
    v = g.add_vertex('A')
    assert v in g.get_vertices()


def test_add_two_vertices():
    g = Graph()
    v1 = g.add_vertex('A')
    v2 = g.add_vertex('B')
    assert v1.value == 'A'
    assert v1 in g.get_vertices()
    assert v2.value == 'B'
    assert v2 in g.get_vertices()


def test_add_edge():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    g.add_edge(apple, banana, 4)
    for v in g.get_vertices():
        if v.value == 'apple':
            assert (banana, 4) in v.adjacencies
        if v.value == 'banana':
            assert (apple, 4) in v.adjacencies


def test_add_weightless_edge():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    g.add_edge(apple, banana)
    for v in g.get_vertices():
        if v.value == 'apple':
            assert (banana, 0) in v.adjacencies
        if v.value == 'banana':
            assert (apple, 0) in v.adjacencies


def test_add_edge_missing_vertex():
    g = Graph()
    h = Graph()
    apple = g.add_vertex('apple')
    banana = h.add_vertex('banana')
    g.add_edge(apple, banana, 4)
    for v in g.get_vertices():
        if v.value == 'apple':
            assert v.adjacencies == []


def test_get_vertices():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    vertices = g.get_vertices()
    assert vertices == {apple, banana}


def test_get_neighbors():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    cucumber = g.add_vertex('cucumber')
    g.add_edge(apple, banana, 4)
    g.add_edge(apple, cucumber, 5)
    neighbors = g.get_neighbors(apple)
    assert neighbors == [(banana, 4), (cucumber, 5)]


def test_size():
    g = Graph()
    g.add_vertex('apple')
    g.add_vertex('banana')
    g.add_vertex('cucumber')
    assert g.size() == 3


def test_empty():
    g = Graph()
    assert g.get_vertices() == set()
    assert g.size() == 0


def test_breadth_first_traverse():
    g = Graph()
    pan = g.add_vertex('Pandora')
    are = g.add_vertex('Arendelle')
    met = g.add_vertex('Metroville')
    mon = g.add_vertex('Monstropolis')
    nab = g.add_vertex('Naboo')
    nar = g.add_vertex('Narnia')
    g.add_edge(pan, are)
    g.add_edge(are, met)
    g.add_edge(are, mon)
    g.add_edge(met, mon)
    g.add_edge(nab, met)
    g.add_edge(nab, mon)
    g.add_edge(nar, met)
    g.add_edge(nar, nab)
    places = g.breadth_first_traverse
    assert places == [
        Pandora,
        Arendelle,
        Metroville,
        Monstroplolis,
        Narnia,
        Naboo
    ]


def test_breadth_first_traverse_with_islands():
    g = Graph()
    pan = g.add_vertex('Pandora')
    are = g.add_vertex('Arendelle')
    met = g.add_vertex('Metroville')
    mon = g.add_vertex('Monstropolis')
    nab = g.add_vertex('Naboo')
    nar = g.add_vertex('Narnia')
    g.add_edge(pan, are)
    g.add_edge(are, met)
    g.add_edge(are, mon)
    g.add_edge(met, mon)
    g.add_edge(nar, nab)
    places = g.breadth_first_traverse
    assert places == [
        Pandora,
        Arendelle,
        Metroville,
        Monstroplolis
    ]