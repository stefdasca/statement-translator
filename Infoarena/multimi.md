## Task

Consider the set $[n] = \{1, \dots, n\}$ of the first $n$ natural non-zero numbers. The sets $A_1, \dots, A_m$ cover $[n]$ if and only if for any $1 \leq i \leq n$, there exists $1 \leq j \leq m$ such that $A_j$ contains $i$. The sets $A_1, \dots, A_m$ separate $[n]$ if and only if for any $1 \leq k, p \leq n$, there exists $1 \leq j \leq m$ such that the cardinality of the intersection between $A_j$ and $\{k, p\}$ is $1$ (practically, there is at least one set in which both elements do not simultaneously occur). For a given $n$, find the minimum $m$ such that $A_1, \dots, A_m$ cover and separate the set $[n]$. Also, display the $m$ sets $A_1, \dots, A_m$ that satisfy this property.

## Input data

The file `multimi.in` contains the integer $n$.

## Output data

The first line of the output file `multimi.out` will contain the minimum number $m$ of sets. The next $m$ lines will print the elements of each set. The elements of a set can be displayed in any order and must be separated by a space.

## Constraints and clarifications

$1 \leq n \leq 100000$

## Example

`multimi.in`
```
10
```

`multimi.out`
```
4
8 9 10
4 5 6 7
2 3 6 7 10
1 3 5 7 9
```
