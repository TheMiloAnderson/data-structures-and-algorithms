from left_join.left_join import left_join_hashmaps
from hashtable.hashtable import Hashtable


def test_tables_with_matches():
    ht_left = Hashtable()
    ht_left.add('fond', 'enamoured')
    ht_left.add('wrath', 'anger')
    ht_left.add('outfit', 'garb')
    ht_left.add('guide', 'usher')

    ht_right = Hashtable()
    ht_right.add('fond', 'averse')
    ht_right.add('wrath', 'delight')
    ht_right.add('flow', 'jam')
    ht_right.add('guide', 'follow')

    joined_vals = left_join_hashmaps(ht_left, ht_right)
    assert len(joined_vals) == 4
    assert ['fond', 'enamoured', 'averse'] in joined_vals
    assert ['wrath', 'anger', 'delight'] in joined_vals
    assert ['outfit', 'garb', None] in joined_vals
    assert ['guide', 'usher', 'follow'] in joined_vals


def test_tables_without_matches():
    ht_left = Hashtable()
    ht_left.add('fond', 'enamoured')
    ht_left.add('wrath', 'anger')
    ht_left.add('outfit', 'garb')
    ht_left.add('guide', 'usher')

    ht_right = Hashtable()
    ht_right.add('fonder', 'averse')
    ht_right.add('wrathful', 'delight')
    ht_right.add('flowing', 'jam')
    ht_right.add('guides', 'follow')

    joined_vals = left_join_hashmaps(ht_left, ht_right)
    assert len(joined_vals) == 4
    assert ['fond', 'enamoured', None] in joined_vals
    assert ['wrath', 'anger', None] in joined_vals
    assert ['outfit', 'garb', None] in joined_vals
    assert ['guide', 'usher', None] in joined_vals


def test_empty_left_table():
    ht_left = Hashtable()

    ht_right = Hashtable()
    ht_right.add('fond', 'averse')
    ht_right.add('wrath', 'delight')
    ht_right.add('flow', 'jam')
    ht_right.add('guide', 'follow')

    joined_vals = left_join_hashmaps(ht_left, ht_right)
    assert len(joined_vals) == 0


def test_empty_right_table():
    ht_left = Hashtable()
    ht_left.add('fond', 'enamoured')
    ht_left.add('wrath', 'anger')
    ht_left.add('outfit', 'garb')
    ht_left.add('guide', 'usher')

    ht_right = Hashtable()

    joined_vals = left_join_hashmaps(ht_left, ht_right)
    assert len(joined_vals) == 4
    assert ['fond', 'enamoured', None] in joined_vals
    assert ['wrath', 'anger', None] in joined_vals
    assert ['outfit', 'garb', None] in joined_vals
    assert ['guide', 'usher', None] in joined_vals
