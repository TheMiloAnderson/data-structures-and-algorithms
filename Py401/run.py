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


def setup_towers(n):
    a = Tower('A')
    b = Tower('B')
    c = Tower('C')
    a.nxt = b
    b.nxt = c
    c.nxt = a
    discs = [Disc(i) for i in range(n, 0, -1)]
    for i in discs:
        a.push(i)
    curr = a
    count = 0
    while c.all_vals() != [i for i in range(n, 0, -1)]:
        yield curr
        curr = curr.nxt
        count += 1
    print(f'Congratulations, you won in {count} moves!')


for tower in setup_towers(16):
    # input('----- move -----')
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
