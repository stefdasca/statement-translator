Costel has a difficult math assignment: given $N$ non-zero natural numbers, he needs to place 2 multiplication operations and $N-3$ addition operations between these numbers such that the result of the calculations is as large as possible. The order of the given numbers cannot be changed.

For example, if $N=5$ and the numbers are $4, 7, 1, 5, 3$, the operations can be placed as $4 + 7 \cdot 1 + 5 \cdot 3$, or $4 \cdot 7 \cdot 1 + 5 + 3$, etc.

# Task
Write a program that places two multiplication operations and $N-3$ addition operations among the $N$ given values so that the value of the resulting expression is maximized.

# Input data
The input file `expresie.in` has the following structure:

The first line contains a natural number $N$, representing the number of the given elements.  
The next lines contain the $N$ given natural numbers, each on a separate line.

# Output data
The output file `expresie.out` will contain, on the first line, the maximum value obtained by evaluating the expression.

# Constraints and clarifications
- $4 \leq N \leq 1\ 000$
- The given numbers are natural numbers between $1$ and $10\ 000$.

`expresie.in`
```
5
4
7
1
5
3
```
`expresie.out`
```
44
```
## Explanation
The maximum value is obtained by placing the operations in the form $4 \cdot 7 + 1 + 5 \cdot 3$.