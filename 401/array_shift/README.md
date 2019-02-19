# Insert and shift middle index of array

## Challenge
Write a function that takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Approach and efficiency
Find the middle index of the given array; iterate over given array below midpoint, appending elements to new array; append new value to new array; iterate over given array above midpoint, appending elements to new array.
Big O: space -> O(N); time -> O(N)

## Solution
![array_shift whiteboard](assets/array_shift.jpg)