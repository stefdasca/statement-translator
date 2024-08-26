## Task

Given the interval $[a, b]$ (all numbers from $a$ to $b$, including both $a$ and $b$), you need to answer $Q$ queries of the form $T\ A$, where $T$ is the type of the query and $A$ is its argument, with the following meanings:
$T = 1$: how many numbers in the interval are divisible by $A$
$T = 2$: how many pairs of distinct numbers in the interval, divisible by $A$, can be formed
$T = 3$: how many pairs of distinct numbers in the interval have a product greater than $A$

## Input data

The input file `interval.in` contains the following:
- The first line contains two natural numbers, $a$ and $b$, separated by a space, representing the interval endpoints.
- The second line contains a number $Q$, the number of queries, and the next $Q$ lines contain pairs of two natural numbers, $T$ and $A$, with the meaning given in the statement.

## Output data

The output file `interval.out` will contain the answers to the $Q$ queries, placed on separate lines.

## Constraints and clarifications

$1 \leq a < b \leq 1\ 000\ 000\ 000$

$b - a \leq 10\ 000\ 000$

$1 \leq Q \leq 20\ 000$

$1 \leq A \leq 10^{18}$

There will be a maximum of $10$ queries of type $3$ in a test.

10% of tests contain only queries of type $1$

20% of tests contain only queries of type $2$

30% of tests contain only queries of type $3$

50% of tests contain queries of type $1$, $2$, and $3$

The results of the queries do not exceed $18$ digits.

## Example

`interval.in`
```
7 10
3
1 10
2 2
3 10
```

`interval.out`
```
1
1
6
```

## Explanation

The interval $[7, 10]$ consists of the numbers $7$, $8$, $9$, $10$. There are 3 queries:
For $1\ 10$, the number of values divisible by $10$ is $1$.
For $2\ 2$, there is one pair of numbers divisible by $2$, the pair $(8, 10)$.
For $3\ 10$, there are $6$ pairs of numbers whose product is greater than $10$: $(7,8)$, $(8, 9)$, $(7, 10)$, $(8, 10)$, $(7,9)$, $(9, 10)$.