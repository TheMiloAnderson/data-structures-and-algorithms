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
    if n % 2 == 0:
        a.nxt = b
        b.nxt = c
        c.nxt = a
    else:
        a.nxt = c
        b.nxt = a
        c.nxt = b
    discs = [Disc(i) for i in range(n, 0, -1)]
    for i in discs:
        a.push(i)
    curr = a
    while c.all_vals() != [i for i in range(n, 0, -1)]:
        print(a, b, c, sep='\n')
        yield curr
        curr = curr.nxt
    print(a, b, c, sep='\n')


move_count = 0
for tower in setup_towers(int(input('How many discs in the stack? '))):
    print('----- move -----')
    for nxt in [tower.nxt, tower.nxt.nxt]:
        disc = tower.peek()
        # skip if no disc to move; don't reverse previous move
        if disc and disc.backwards != nxt:
            nxt_disc = nxt.peek()
            # move into empty stacks
            if not nxt_disc:
                print(f'move {disc.num} from {tower.id} to {nxt.id}')
                nxt.push(tower.pop())
                disc.backwards = tower
                move_count += 1
            # only move odd to even, even to odd, and smaller to larger
            elif disc.num % 2 != nxt_disc.num % 2 and disc.num < nxt_disc.num:
                print(f'move {disc.num} from {tower.id} to {nxt.id}')
                nxt.push(tower.pop())
                disc.backwards = tower
                move_count += 1
print(f'Congratulations, you won in {move_count} moves!')
