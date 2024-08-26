## Task

Given an array with $N$ elements and $M$ queries. For each query, two values $a$ and $b$ are given, and the Value God must decide if the sequence is Poor or King. For this, you have to display the maximum value in that sequence.

## Input data

The input file `saracsaurege.in` will contain the first line with 2 natural numbers $N$ and $M$. The second line will contain $N$ numbers representing the given array. The next $M$ lines will contain 2 numbers $a$ and $b$, representing the queries sorted by $b - a$.

## Output data

The output file `saracsaurege.out` will contain $M$ values representing the answer to the $M$ queries.

## Constraints

$1 \leq N \leq 50\ 000$ 

$1 \leq M \leq 1\ 000\ 000$ 

The $M$ queries are sorted in descending order by $b - a$. 

Watch out for the memory limit! Try to solve the problem with $O(n \cdot \log n + m)$ time and $O(n)$ memory :)

## Example

`saracsaurege.in`
```
5 3 
7 6 9 3 8 
2 5 
1 2 
4 4
```

`saracsaurege.out`
```
9 
7 
3
```