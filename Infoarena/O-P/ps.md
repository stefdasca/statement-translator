# Ps

Just before the last session, the $N$ students in group $236$ had to face a new obstacle: the Probability and Statistics assignment. As with any other assignment, solving it was postponed until the last day. Thus, the WhatsApp group chat "exploded", as everyone wanted to finish the assignment as quickly as possible and, of course, with as little effort as possible. Gathering information about each student's assignments, they noticed the following:
Each student was given a "personalized" assignment.
There are a total of $M$ distinct problems selected from a collection (unfortunately without answers at the end).
Each of the $M$ problems is present in at least one student's assignment.
Any of the $M$ problems appear in at most two assignments.
Each assignment contains at least one problem and at most two problems.
A student can now solve any problem that is in their assignment. After solving it, they will upload the solution to the WhatsApp chat, and any other student who had that problem in their assignment will not have to solve it anymore.

## Task

Given the information about each student's assignments, determine an optimal assignment of problems so that each student solves a minimum number of problems, thereby minimizing the maximum number of problems solved by any student.

## Input data

The input file `ps.in` contains on the first line three integers, $N$ (the number of students), $M$ (the number of problems), $K$. Each of the following $K$ lines will contain two integers, separated by a space, $s$ and $p$, representing an association where the assignment of student number $s$ contains problem $p$.

## Output data

The output file `ps.out` should contain on the first line the minimum value of the maximum number of problems that a student will solve. On the second line, $M$ numbers separated by a space will be displayed. The $i$-th number represents the index of the student who solves problem $i$, in the optimal case.

## Constraints

$1 \leq N \leq 100\,000$

Both students and problems are 1-indexed.

If there are multiple distributions of problems corresponding to the optimal solution, any of them may be displayed.

For tests worth $30$ points, $1 \leq N \leq 2\,000$

## Example

`ps.in`
```
5 5 8
1 1
1 2
2 1
2 3
3 2
3 3
4 5
5 4
```

`ps.out`
```
1
1 3 2 5 4
```

`ps.in`
```
6 1 1
1 1
```

`ps.out`
```
1
1
```