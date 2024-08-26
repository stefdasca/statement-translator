# Divk

Given an array of $N$ non-zero natural numbers, for the triplet $(K, A, B)$ provided, we have to answer the question: how many subarrays of the given array have lengths between $A$ and $B$ (inclusive) and have their element sums divisible by $K$?

## Task

Determine the number of subarrays with the stated property.

## Input data

The first line of the file `divk.in` contains four natural numbers $N$, $K$, $A$, and $B$, separated by spaces, having the significance described in the task. Each of the following $N$ lines contain one non-zero natural number, the elements of the array.

## Output data

The first line of the file `divk.out` contains a natural number $T$, the number of subarrays with the required property.

## Constraints and clarifications

$1 < A < B < N \leq 500\,000$  
$2 \leq K \leq 100\,000$  
Each number in the $N$ does not exceed $10\,000\,000$ ($10$ million).  
By subarray, we mean any sequence of terms from the array that are on consecutive positions.

## Example

`divk.in`  
`6 5 2 4`  
`2`  
`9`  
`5`  
`4`  
`1`  
`4`

`divk.out`  
`4`

## Explanation

The subarrays that can be chosen are: $(2 9 5 4)$, $(4 1)$, $(5 4 1)$, and $(1 4)$.