## Task

Bored during the counseling and career guidance class (abbreviated as c.c.g.), Cash wrote on a piece of paper the natural numbers from $1$ to $N$ and asked himself the following question: How could he split the numbers into two disjoint sets (two sets that do not share any elements) such that the absolute difference between the sum of the elements of the two sets is minimal? Determine the minimal absolute difference as well as one way to form the two sets. If there are multiple solutions, you can display any of them.

## Input data

The file `multimi2.in` contains $N$ on the first line, with the meaning from the problem statement.

## Output data

The file `multimi2.out` contains a number $D_{min}$ on the first line representing the minimal absolute difference between the sum of the elements of the two sets. The second line contains a number $NR1$ representing the number of elements in the first set, followed by the elements of the first set separated by spaces on the next line. The subsequent line contains the number $NR2$ (the number of elements in the second set), followed by the elements of the second set separated by spaces.

## Constraints and clarifications

$2 \leq N \leq 1\,000\,000$

## Example

`multimi2.in`
```
3
```
`multimi2.out`
```
0
2
1 2
1
3
```