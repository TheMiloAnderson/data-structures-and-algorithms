# Insertion Sort

## Challenge
Write a function for insertion sort that takes in an unsorted array and returns the array sorted using insertion sort.

## Approach & Efficiency
Used nested while loops: The outer loop traverses the array from left to right; the inner loop traverses from the current index backwards, checking the list item against its left neighbor and swapping the values, stopping if/when the neighboring values are in correct order or the beginning of the list is reached. 

The time efficiency is O(N), because the algorithm must iterate over the entire input list at least once. The space efficiency is O(1), because the list is sorted in-place