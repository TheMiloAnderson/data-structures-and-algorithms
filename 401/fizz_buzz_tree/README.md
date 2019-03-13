# Breadth-first binary tree traversal

## Challenge
Write a function called FizzBuzzTree which takes a tree as an argument.
Without utilizing any of the built-in methods available to your language, determine weather or not the value of each node is divisible by 3, 5 or both, and change the value of each of the nodes:
* If the value is divisible by 3, replace the value with “Fizz”
* If the value is divisible by 5, replace the value with “Buzz”
* If the value is divisible by 3 and 5, replace the value with “FizzBuzz”

## Approach & Efficiency
Recursive function, checks values against % 3, % 5, and % 15, invokes self on child nodes.
time: O(N); space: O(1)

## Solution
![whiteboard](assets/milo-cc16-whiteboard.jpg)
