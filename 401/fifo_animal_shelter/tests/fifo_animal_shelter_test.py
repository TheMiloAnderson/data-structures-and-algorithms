from fifo_animal_shelter.fifo_animal_shelter import Animal, AnimalShelter


def test_enqueue_one():
    fas = AnimalShelter()
    fas.enqueue(Animal('cat', 'a'))
    assert fas.dequeue('cat').name == 'a'


def test_enqueue_many():
    fas = AnimalShelter()
    fas.enqueue(Animal('cat', 'a'))
    fas.enqueue(Animal('cat', 'b'))
    fas.enqueue(Animal('cat', 'c'))
    assert fas.dequeue('cat').name == 'a'
    assert fas.dequeue('cat').name == 'b'
    assert fas.dequeue('cat').name == 'c'
    assert not fas.dequeue('cat')


def test_dequeue_both():
    fas = AnimalShelter()
    fas.enqueue(Animal('cat', 'a'))
    fas.enqueue(Animal('cat', 'b'))
    fas.enqueue(Animal('dog', 'c'))
    fas.enqueue(Animal('cat', 'd'))
    fas.enqueue(Animal('dog', 'e'))
    fas.enqueue(Animal('dog', 'f'))
    assert fas.dequeue('cat').name == 'a'
    assert fas.dequeue('dog').name == 'c'
    assert fas.dequeue('cat').name == 'b'
    assert fas.dequeue('dog').name == 'e'
    assert fas.dequeue('cat').name == 'd'
    assert fas.dequeue('dog').name == 'f'
    assert not fas.dequeue('cat')


def test_dequeue_neither():
    fas = AnimalShelter()
    fas.enqueue(Animal('cat', 'a'))
    fas.enqueue(Animal('parrot', 'b'))
    fas.enqueue(Animal('dog', 'c'))
    assert not fas.dequeue('parrot')
