Ludwig has a permutation $p = (p_1, p_2, \dots, p_N)$ of the set $\{1, 2, \dots, N\}$ and a table where he can place the numbers from the permutation. Ludwig takes the first number from the permutation, namely $p_1$, and places it on the table. The second number, $p_2$, can be placed either to the left of $p_1$ or to the right of $p_1$. At each step, if the numbers $p_1, p_2, \dots, p_i$ have already been placed on the table, then the number $p_{i+1}$ can be placed either to the left of the already placed numbers or to the right of them.

# Task

Help Ludwig determine a way to place the entire permutation on the table such that in the end a new permutation with the minimum number of inversions is obtained.

# Input data

The file `inversiuni.in` contains on the first line the natural number $N$, and on the second line, separated by a space, the numbers $p_1, p_2, \dots, p_N$.

# Output data

The file `inversiuni.out` contains a single natural number representing the minimum number of inversions that can be obtained.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* An inversion in a permutation is a pair of indices $(i, j)$ with $i < j$ and $p_i > p_j$. For example, the permutation $p = (3, 2, 1, 4)$ has the inversion pair $(1, 3)$ because $p_1 > p_3$; another inversion is the pair $(2, 3)$ because $p_2 > p_3$.

# Example 1

`inversiuni.in`
```
4 
2 1 3 4
```

`inversiuni.out`
```
0
```

## Explanation

The elements are placed on the table as follows: 

$2$ \ 
$1 \ 2$ ($1$ is placed to the left) \
$1 \ 2 \ 3$ ($3$ is placed to the right) \
$1 \ 2 \ 3 \ 4$ ($4$ is placed to the right) 

The identical permutation is obtained, which means zero inversions.

# Example 2

`inversiuni.in`
```
4 
2 1 4 3
```

`inversiuni.out`
```
1
```

## Explanation

The elements are placed on the table as follows:

$2$ \ 
$1 \ 2$ ($1$ is placed to the left) \
$1 \ 2 \ 4$ ($4$ is placed to the right) \
$1 \ 2 \ 4 \ 3$ ($3$ is placed to the right) 

A permutation with one inversion is obtained.
