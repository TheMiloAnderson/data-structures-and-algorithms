def fizz_buzz_tree(tree, curr=None):
    if not curr:
        curr = tree.root

    if curr.value % 15 == 0:
        curr.value = 'FizzBuzz'
    elif curr.value % 3 == 0:
        curr.value = 'Fizz'
    elif curr.value % 5 == 0:
        curr.value = 'Buzz'

    if curr.l_child:
        fizz_buzz_tree(tree, curr.l_child)

    if curr.r_child:
        fizz_buzz_tree(tree, curr.r_child)
