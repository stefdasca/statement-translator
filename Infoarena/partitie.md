## Task

Given a finite set $M$. A partition of set $M$ is defined as a set of subsets $S_1, S_2 \dots S_K$ $(K ≥ 1)$ with the properties:
- the union of the $K$ subsets results in the set $M$
- the intersection of any two distinct subsets is the empty set

Given the set $M$ with $N$ elements and the natural number $D$, determine the minimum number of subsets in which $M$ can be partitioned such that for any subset $S_i$ with a cardinality of at least $2$ in the partition, the absolute difference between any $2$ elements in $S_i$ is greater than or equal to $D$.

## Input data

The input file `partitie.in` contains on the first line the natural numbers $N$ and $D$. Each of the next $N$ lines contains a number, indicating an element of the set $M$.

## Output data

The output file `partitie.out` will contain on the first line the minimum number of subsets in a partition that satisfies the given condition. The following $N$ lines contain the partition of the elements of the set $M$. Thus, line $i+1$, with $i$ from $1$ to $N$, contains the number of the subset in which the element from line $i+1$ of the input file is placed. If there are multiple possible solutions, any one of them can be displayed.

## Constraints and clarifications

$D$ and the elements of the set $M$ are natural numbers in the interval $[1, 10^9]$

Points for a test are obtained only if both the number of subsets and the partitioning of the elements into subsets are correct.

There will be $10$ tests for evaluation, each worth $10$ points. The table below shows the values of $N$ for each test:

$T1 \quad T2 \quad T3 \quad T4 \quad T5 \quad T6 \quad T7 \quad T8 \quad T9 \quad T10$

$11 \quad 50 \quad 1014 \quad 5950 \quad 20000 \quad 67901 \quad 150099 \quad 195993 \quad 269956 \quad 300000$

## Example

`partitie.in`

```
5 3
9
2
11
5
3
```

`partitie.out`

```
2
1
1
2
1
2
```

## Explanation

Subset $1$ is $\{9, 2, 5\}$, and subset $2$ is $\{11, 3\}$. Thus, the difference between any two numbers in the same subset is at least $3$. The given set cannot be partitioned into fewer than $2$ subsets such that the given property is respected.