from stacks_and_queues.stacks_and_queues import Stack


class Tower(Stack):

    def __init__(self, id):
        self.id = id
        self.nxt = None

    def all_vals(self):
        output = []
        curr = self.top
        while curr:
            output.insert(0, curr.value.num)
            curr = curr.nxt
        return output

    def __str__(self):
        return str(self.id) + ': ' + str(self.all_vals())


class Disc(object):

    def __init__(self, num):
        self.num = num
        self.backwards = None


def setup_towers():
    a = Tower('A')
    b = Tower('B')
    c = Tower('C')
    a.nxt = b
    b.nxt = c
    c.nxt = a
    discs = [Disc(i) for i in range(6, 0, -1)]
    for i in discs:
        a.push(i)
    towers = [a, b, c]
    go = True
    while go:
        for tower in towers:
            if c.all_vals() != [6, 5, 4, 3, 2, 1]:
                yield tower
            else:
                go = False
                print('Congratulations, you won!')


for tower in setup_towers():
    input('----- move -----')
    print(tower, tower.nxt, tower.nxt.nxt, sep='\n')
    for nxt in [tower.nxt, tower.nxt.nxt]:
        disc = tower.peek()
        # skip if no disc to move
        if disc:
            nxt_disc = nxt.peek()
            # don't go backwards
            if disc.backwards != nxt:
                # move into empty stacks
                if not nxt_disc:
                    print(f'move {disc.num} from {tower.id} to {nxt.id}')
                    nxt.push(tower.pop())
                    disc.backwards = tower
                # only move odd to even, even to odd, and smaller to larger
                elif disc.num % 2 != nxt_disc.num % 2 and disc.num < nxt_disc.num:
                    print(f'move {disc.num} from {tower.id} to {nxt.id}')
                    nxt.push(tower.pop())
                    disc.backwards = tower
    print(tower, tower.nxt, tower.nxt.nxt, sep='\n')
