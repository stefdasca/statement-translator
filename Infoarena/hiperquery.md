## Hiperquery

A circular array of natural numbers $V$ of length $N$, indexed from $1$, is given. The numbers in the array are within the closed interval $[1, N]$, and the first and last positions are considered adjacent. The following operations are defined:
- **Update $X$, $Y$**: the element at position $X$ becomes $Y$
- **Rotate $X$**: rotate the array $X$ positions to the right (the array $[1, 2, 3, 4]$ rotated one position to the right becomes $[4, 1, 2, 3]$)
- **Query $L$ $R$ $X$**: how many numbers in the subarray are equal to $X$. There can be queries where $L > R$, in which case we want the number of numbers in the array that are equal to $X$

Given the initial array, the task is to process a given sequence of operations.

## Input data

The first line of the input file `hiperquery.in` contains the number $N$. The next line contains $N$ natural numbers which form the array $V$. The next line contains a number $M$ followed by $M$ lines that describe the given operations:
- For update: $1$ $X$ $Y$
- For rotation: $2$ $X$
- For query: $3$ $L$ $R$ $X$

## Output data

The output file `hiperquery.out` will contain the answers to the queries, each on a new line.

## Constraints and clarifications

Subtasks:
- Subtask 1 (10 points) 
  $1 \leq N \leq 1000$
- $1 \leq M \leq 1000$
- Subtask 2 (30 points) 
  $1 \leq N \leq 100000$ 
- $1 \leq M \leq 100000$
- There are no operations of type $1$
- Subtask 3 (30 points) 
  $1 \leq N \leq 100000$
- $1 \leq M \leq 100000$
- There are no operations of type $2$
- Subtask 4 (30 points) 
  $1 \leq N \leq 100000$
- $1 \leq M \leq 100000$

## Examples

`hiperquery.in`
```
4 
4 1 3 1 
6 
3 2 4 1 
3 1 4 3 
3 2 1 1 
1 1 2 
2 1 
3 1 1 2 
```
`hiperquery.out`
```
2 
2 
2 
1
```
For the first query, the subarray is: $[4, 1, 3, 1]$  
For the second query, the subarray is $[4, 1, 3, 1]$  
For the third query, the subarray is the entire array.  
After the first update, the array becomes: $[2, 1, 3, 1]$  
After the rotation, the array becomes: $[3, 1, 2, 1]$  
For the last query, the subarray is: $[3, 1, 2, 1]$