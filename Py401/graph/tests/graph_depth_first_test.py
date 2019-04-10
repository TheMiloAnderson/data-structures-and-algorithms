from graph.graph import Graph


def test_depth_first_traverse():
    graph = Graph()
    a = graph.add_vertex('A')
    b = graph.add_vertex('B')
    c = graph.add_vertex('C')
    d = graph.add_vertex('D')
    e = graph.add_vertex('E')
    f = graph.add_vertex('F')
    g = graph.add_vertex('G')
    h = graph.add_vertex('H')
    graph.add_edge(a, b)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(c, g)
    graph.add_edge(d, e)
    graph.add_edge(d, h)
    graph.add_edge(d, f)
    graph.add_edge(f, h)
    assert graph.depth_first_traverse(a) == [
        'A',
        'B',
        'C',
        'G',
        'D',
        'E',
        'H',
        'F'
    ]


def test_depth_first_traverse_with_diff_root():
    graph = Graph()
    a = graph.add_vertex('A')
    b = graph.add_vertex('B')
    c = graph.add_vertex('C')
    d = graph.add_vertex('D')
    e = graph.add_vertex('E')
    f = graph.add_vertex('F')
    g = graph.add_vertex('G')
    h = graph.add_vertex('H')
    graph.add_edge(a, b)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(c, g)
    graph.add_edge(d, f)
    graph.add_edge(d, e)
    graph.add_edge(d, h)
    graph.add_edge(f, h)
    assert graph.depth_first_traverse(e) == [
        'E',
        'D',
        'A',
        'B',
        'C',
        'G',
        'F',
        'H'
    ]
    assert graph.depth_first_traverse(d) == [
        'D',
        'A',
        'B',
        'C',
        'G',
        'F',
        'H',
        'E'
    ]


def test_islands_depth_first_traverse():
    graph = Graph()
    a = graph.add_vertex('A')
    b = graph.add_vertex('B')
    c = graph.add_vertex('C')
    d = graph.add_vertex('D')
    e = graph.add_vertex('E')
    f = graph.add_vertex('F')
    g = graph.add_vertex('G')
    h = graph.add_vertex('H')
    graph.add_edge(a, d)
    graph.add_edge(c, g)
    graph.add_edge(d, e)
    graph.add_edge(d, h)
    graph.add_edge(d, f)
    graph.add_edge(f, h)
    assert graph.depth_first_traverse(a) == [
        'A',
        'D',
        'E',
        'H',
        'F'
    ]