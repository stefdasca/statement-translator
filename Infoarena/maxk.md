## Task

Fierce competition! Ojilă is participating today in the bench-level stage of the informatics olympiad. His competitor is Onilă, his colleague and rival. They have to solve a problem, and whoever solves it will advance to the window-row stage. Given an array of $N$ natural numbers and a natural number $K$, the task is to eliminate a subarray of minimal length so that each element in the remaining array appears at most $K$ times.

## Input data

The input file `maxk.in` contains on the first line the numbers $N$ and $K$. The next line contains $N$ natural numbers separated by spaces, representing the elements of the array.

## Output data

The output file `maxk.out` will contain a single number representing the minimal length of the subarray.

## Constraints and clarifications

$1 \leq K,N \leq 1\ 000\ 000$

The elements of the array are non-zero natural numbers less than or equal to $100\ 000$.

## Example

`maxk.in`
```
6 1
3 3 3 2 1 2 3
```

`maxk.out`
```
3
```

## Explanation

The subarray to be eliminated is $3, 3, 2$.