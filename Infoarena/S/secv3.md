# Sequence 3

The tests for this problem are not well constructed to correctly distinguish inefficient or incorrect solutions. If you want to help us improve the quality of the tests for this problem, please click here! Gigel is a person with a very rich imagination, especially when he sleeps! One night he dreamed that he had a very bizarre task to complete: he had to choose a subarray (a subsequence of elements that appear in consecutive positions in the initial sequence) from $ N$ elements for which the cost and time are known. The chosen subarray had to be of minimum length $ L$ and maximum length $ U$, and the sum of the costs of the elements in the subarray divided by the sum of the times of the elements in the subarray had to be maximal.

## Task

In a short time, Gigel's dream turned into a nightmare because he cannot solve the task! Write a program to help him!

## Input data

The first line in the input file `secv3.in` contains the numbers $ N$, $ L$ and $ U$ separated by spaces. The second line contains $ N$ natural numbers representing the costs of the elements of the subarray, and the third line contains $ N$ natural numbers representing the times of the elements of the subarray.

## Output data

The first line of the output file `secv3.out` should contain a real number with two decimal precision, representing the maximum value of the sum of the costs of the elements in the subarray divided by the sum of the times of the elements in the subarray.

## Constraints and clarifications

$1 \leq L \leq U \leq N \leq 30\ 000$  
The cost and time of an element are natural numbers in the interval $[1, 1\ 000]$  
The number written in the output file will be considered correct only if the absolute value of the difference between your result and the jury's result is less than or equal to $10^{-2}$

## Example

`secv3.in`  
```
5 1 2  
1 1 3 2 5  
4 2 5 3 6  
```

`secv3.out`  
```
0.83
```