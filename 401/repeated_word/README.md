# Find first repeated word in string

## Challenge
Write a function that accepts a lengthy string parameter. Without utilizing any of the built-in library methods available to your language, return the first word to occur more than once in that provided string.

## Approach & Efficiency
We wanted to use a hashtable, becuase this makes additions and lookups more efficient. A python dictionary or set would have fulfilled this function nicely; however the assignment asks that we not use any built-in language constructs, so we used the hashtable classes we wrote previously. 

However, in order to get the function working the way it does in the given examples, it's necessary to strip out punctuation, and this overwhelms whatever efficiency gains we got from using the hashtable. Also, unless the assignment is asking us to iterate & check every single character in the string, which doesn't seem likely, it's better to use regex, but this is a built-in language method. 

This reminds me that this is an artificial situation (whiteboard practice) meant to simulate an artificial situation (whiteboard interview) that itself bears only a tenuous resemblance to challenges you'd face in reality. I guess two nested levels of pretending is where I start to get confused about how best to interpret our goals. 

Efficiency:
time: O(N)
space: O(N)

## Solution
![whiteboard](assets/cc26_whiteboard.jpg)
