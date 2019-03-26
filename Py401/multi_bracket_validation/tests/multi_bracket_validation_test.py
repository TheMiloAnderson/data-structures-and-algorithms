from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation


def test_balanced():
    s = 'a(b[c{d}e]f)g'
    assert multi_bracket_validation(s)


def test_unbalanced():
    s = 'qwerty([{])poiuy'
    assert not multi_bracket_validation(s)


def test_closing_first():
    s = 'kcT)dk('
    assert not multi_bracket_validation(s)


def test_not_closed():
    s = 'z(y[x{wvu}t]s'
    assert not multi_bracket_validation(s)
