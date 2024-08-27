# Tree

A company has $N$ employees numbered from $1$ to $N$. The employees are organized in a hierarchy in the form of a tree (a connected graph without cycles). Thus, each employee has exactly one direct superior (except for the owner of the company), and an employee can have several direct subordinates. The owner of the company is numbered $1$. An employee $A$ is subordinate to another employee $B$ if one of the following conditions is met:
  - $A$ is a direct subordinate of $B$
  - $A$ is one of the subordinates of another subordinate of $B$

Due to the very high profits obtained by the company, employees will receive certain sums of money as bonuses. For strict record-keeping, the company's accountant must perform $M$ operations of two types:
  - given $p$ and $s$, all subordinates of node $p$ (including node $p$) will receive the sum of money $s$
  - given a number $s$, an employee who has received the sum $s$ up to that point must be identified

It should be noted that some employees can be rewarded multiple times, while others may not receive anything.

## Task

Write a program that receives $N$, $M$, the structure of the employees, and the $M$ operations, and for each type 2 operation outputs the requested value.

## Input data

The file `arbore.in` will contain on the first line the numbers $N$ and $M$ separated by a space. The next $N-1$ lines contain two integers $p$ and $q$ signifying that "there is a direct relationship between employee $p$ and employee $q$". The next $M$ lines each contain one operation per line. The first number on the line is $1$ or $2$, indicating the type of operation to be described. In the case of a type 1 operation, the numbers $p$ and $s$ will follow, and in the case of a type 2 operation, a single number $s$ will follow.

## Output data

The file `arbore.out` will contain the index of an employee who has received the respective sum of money up to that point for each type 2 operation. If there is no such employee, it should display $-1$. It does not matter which employee's index you will display, as long as they have received the sum $s$.

## Constraints

$1 \leq N, M \leq 100\ 000$

for a type 1 operation we have $1 \leq s \leq 10$

for a type 2 operation we have $0 \leq s \leq 1\ 000\ 000$

50% of the tests used in evaluation will not contain more than 100 type 2 operations

## Example

`arbore.in`

```
6 6
1 2
1 3
3 4
3 5
4 6
1 1 1
1 2 4
2 5
2 1
1 3 3
2 4
```

`arbore.out`

```
1
1
3
2
```