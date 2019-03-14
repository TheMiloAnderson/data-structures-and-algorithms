from hashtable.hashtable import Hashtable
import pytest


def test_instance_table():
    h = Hashtable()
    assert len(h.table) == 1024


def test_hash_determinism():
    h = Hashtable()
    assert h.hash('Milo') == h.hash('Milo')
    assert h.hash('Jasmin') == h.hash('Jasmin')
    assert h.hash(9) == h.hash(9)


def test_add():
    h = Hashtable()
    h.add('abc', 'def')
    h.add('zyx', 'wvu')
    assert h.table[h.hash('abc')][1] == 'def'
    assert h.table[h.hash('zyx')][1] == 'wvu'
