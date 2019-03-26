from stacks_and_queues.stacks_and_queues import Stack, Node
import sys
sys.path.insert(0, '/home/milo/codefellows/data-structures-and-algorithms/401')


def multi_bracket_validation(input):
    stack = Stack()
    b = {')': '(', ']': '[', '}': '{'}
    for i in range(len(input) - 1):
        if input[i] in b.values():
            stack.push(input[i])
        if input[i] in b.keys():
            if stack.peek() == b[input[i]]:
                stack.pop()
            else:
                return False
    if stack.peek() == None:
        return True
    else:
        return False
