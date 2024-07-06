Today, *Șarpele* learned about the divisibility of whole numbers in his mathematics class. The teacher assigned him a homework exercise where he is given $n$ and $q$ numbers, and for each number $X$ out of the $q$ numbers, he must find how many of the $n$ numbers are multiples of $X$.

# Task
Help *Șarpele* with his homework.

# Input data
The first line contains the natural number $n$.  
The second line contains the $n$ whole numbers, separated by a space; let's denote each of these numbers with $v$.  
The third line contains the natural number $q$.  
The following $q$ lines each contain an integer $X$.

# Output data
For the $q$ lines, print, in the order they appear in the input file, the answers to the $q$ numbers.

# Constraints and clarifications
* $1 \leq n, q \leq 1\ 000\ 000$;
* $-1\ 000\ 000 \leq v, X \leq 1\ 000\ 000$.

## Subtask 1 (20 points)
* $1 \leq n, q, v, X \leq 1\ 000$.

## Subtask 2 (30 points)
* $1 \leq n, q \leq 1\ 000$.

## Subtask 3 (50 points)
* Without constraints.

# Example
`stdin`
```
5
2 4 5 6 7
3
2
3
0
```
`stdout`
```
3
1
0
```