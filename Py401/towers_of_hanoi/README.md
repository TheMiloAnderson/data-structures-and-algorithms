# Towers of Hanoi

## Challenge
I wanted to find a solution to the Towers of Hanoi puzzle on my own -- without looking at anyone else's solution first, this is what I came up with. It's not as elegant as the recursive solution you can find online, but it reliably solves the puzzle for N discs in (2**N - 1) moves

The puzzle starts with three stacks (A, B, & C), and N numbered discs in ascending order on the A stack. The objective of the puzzle is to move the entire A stack to C, obeying the following rules:

* Only one disc can be moved at a time.
* Each move consists of taking the top disc from one of the stacks and placing it on top of another stack of discs, or on an empty stack.
* No larger disc may be placed on top of a smaller disc. 