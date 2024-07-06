Andrei is a student passionate about informatics. Today he learned about the greatest common divisor of two numbers and has the homework to find how many pairs of numbers $p$ and $q$ ($p \leq q$) that are coprime exist, such that $p \cdot q = n$. Help him find the answer using an efficient program.

# Task
Given $t$ and $t$ natural numbers $n$. For each number $n$, display how many pairs $p$ and $q$ exist with the property described in the statement.

# Input data
The input file `produs.in` contains on the first line the number $t$. The second line contains $t$ natural numbers.

# Output data
The output file `produs.out` contains $t$ lines, where line $i$ contains the answer for the $i$-th number.

# Constraints and clarifications
* $1 \leq t \leq 4 \cdot 10^5$
* $1 \leq n \leq 4 \cdot 10^6$
* $(p, q)$ and $(q, p)$ are different pairs.
* For $40$ points, $n \leq 10^5$ and the tests are generated randomly.
* For $80$ points, $n \leq 10^6$.

# Example
`produs.in`
```
4
1 6 9 7
```
`produs.out`
```
0
4
2
2
```

## Explanation
For $6$, the $4$ pairs are $(1, 6)$, $(6, 1)$, $(2, 3)$, $(3, 2)$.