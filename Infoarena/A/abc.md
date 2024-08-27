ABC

Haralambie received the following problem as a homework assignment in computer science: Given an array $A$ of $N$ distinct, non-zero natural numbers, each less than or equal to a given natural number $B$. In addition, a natural number $C$ is also provided. The task is to determine an array $D$ of $N$ distinct, non-zero natural numbers, each less than or equal to $B$, such that their sum is equal to $C$, and the maximum term of the array $|A_i - D_i|$ is minimized.

## Task

Help Haralambie and determine an array $D$ that meets the given conditions.

## Input data

The file `abc.in` contains the natural numbers $N$, $B$, and $C$ on the first line, separated by spaces. The next line contains the $N$ numbers of array $A$, separated by spaces.

## Output data

The file `abc.out` will contain the elements of array $D$, separated by spaces on the first and only line. If there are multiple solutions, you may print any of them.

## Constraints and clarifications

$1 \leq N \leq 30000$

$1 \leq B \leq 65535$

$1 \leq C \leq 2147483647$

For all the tests used in the evaluation, there will be a solution.

## Example

`abc.in`
```
6 10 38
1 3 4 7 9 10
```
`abc.out`
```
2 4 5 8 9 10
```