# Singly Linked List
Class that implements a singly linked list

## Challenge
The challenge was to implement a linked list in Python, with methods to add nodes, search node values, and return a collection of all values.

## Approach and Efficiency
The LinkedList class uses the Node class to manage linked list nodes. The insert() method adds a new node at the head position, with an efficiency of O(1). The includes() method iterates through node values, stopping when the value is found or the last node is reached; the efficiency of this method is O(N). The print() method is a simple traversal and concatenation, efficiency O(N)

The append() method adds a new node at the end of the linked list; insert_before() and insert_after() insert nodes before or after the given value. All of these methods have a Big O efficiency of Time: O(N); Space: O(1).

The find_from_end method accepts an integer, and returns the value of the node is that is k nodes from the end of the list. Time and space efficiency are both O(N)

The ll_zip function in ll_merge/ll_merge.py accepts two linked lists as arguments, and combines them into one with alternating nodes. The time/space is O(N) and O(1), respectively.

**April 3, 2019:**
- [x] Using Test Driven Development add Iterable features to LinkedList and BinaryTree/BinarySearchTree implementations
- [x] Pass all tests for LinkedList

## Solution
![linked list whiteboard](assets/linked_list.jpg)