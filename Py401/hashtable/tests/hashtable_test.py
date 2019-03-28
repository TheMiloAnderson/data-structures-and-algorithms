from ..hashtable import Hashtable
from ...linked_list.linked_list import LinkedList
import pytest


def test_instance_table():
    h = Hashtable()
    assert len(h.table) == 1024


def test_hash_determinism():
    h = Hashtable()
    assert h.hash('Milo') == h.hash('Milo')
    assert h.hash('Jasmin') == h.hash('Jasmin')
    assert h.hash('foo') == h.hash('oof')
    assert h.hash(9) == h.hash(9)


def test_add():
    h = Hashtable()
    h.add('abc', 'def')
    h.add('zyx', 'wvu')
    assert h.table[h.hash('abc')].head.value[1] == 'def'
    assert h.table[h.hash('zyx')].head.value[1] == 'wvu'


def test_collide():
    h = Hashtable()
    h.add('foo', 'bar')
    h.add('oof', 'rab')
    assert h.table[h.hash('foo')].head.next.value[1] == 'bar'
    assert h.table[h.hash('oof')].head.value[1] == 'rab'


def test_get():
    h = Hashtable()
    h.add('abc', 'def')
    h.add('zyx', 'wvu')
    h.add('foo', 'bar')
    h.add('oof', 'rab')
    assert h.get('abc') == 'def'
    assert h.get('foo') == 'bar'
    assert h.get('oof') == 'rab'


def test_contains():
    h = Hashtable()
    h.add('abc', 'def')
    h.add('zyx', 'wvu')
    h.add('foo', 'bar')
    h.add('oof', 'rab')
    assert h.contains('abc') is True
    assert h.contains('oof') is True
    assert h.contains('dar') is False
