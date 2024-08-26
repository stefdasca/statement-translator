## Task

In search of ways to get pocket money to make your student life more pleasant, you found a job advertisement for "IT system administrator assistant for school," which you applied for and got hired. Of course, during the pandemic, helping with school administration is more difficult than it seems. More precisely, the task now is to divide a class of $N$ students into multiple rooms (assumed to have infinite capacity) along a long corridor (assumed infinite), to promote social distancing. Unfortunately, between the $N$ students, there are $M$ friendship relations (obviously, bidirectional), and two friends will not agree with the division plan unless they are assigned to the same room or, at most, to adjacent rooms. Specifically, two friends $i$ and $j$ will agree with the division plan if and only if $|s(i) - s(j)| \leq 1$ (where $s(i)$ represents the index of the room to which the student numbered $i$ will be assigned, and $|x|$ represents the modulus of the integer $x$). To adhere as closely as possible to social distancing norms, students must be assigned to as many rooms as possible. Your task is to develop a system to determine the maximum number of rooms in which they can be assigned, so that all students agree with the division plan, and also to produce such a plan.

## Input data

The input file `sali.in` contains on the first line two natural numbers $N$ and $M$, as specified in the statement. On the following $M$ lines, there are two natural numbers $a$ and $b$ ($1 \leq a, b \leq N$), describing the friendship relations.

## Output data

The output file `sali.out` will contain on the first line a natural number $K$, the maximum number of rooms in which they can be assigned. On the second line, it will contain $N$ natural numbers in the interval $[1\ldots K]$. The $i$-th number will represent the index of the room assigned to the student numbered $i$.

## Constraints and clarifications

$1 \leq N \leq 1000$

$1 \leq M \leq 10000$

All pairs in the input file are distinct.

For each pair $(i, j)$, it is true that $i \neq j$.

For the displayed solution to be correct, each of the $K$ rooms must contain at least one student.

## Example

`sali.in` 
```
4 3
1 2
2 3
3 4
```

`sali.out`
```
4
1 2 3 4
```

`sali.in`
```
6 6
1 2
2 3
3 1
4 5
5 6
6 4
```

`sali.out`
```
4
1 2 2 1 2 3
```