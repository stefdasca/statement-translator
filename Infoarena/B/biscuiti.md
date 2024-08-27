# Biscuits

The fence of the biscuit factory is quite worn out. The management decides to fix this and contacts two amateur workers. Upon arrival, the workers determine that the fence is made up of $N$ planks (which they number 1, 2, 3 $\dots$ $N$ from left to right) of different lengths. They decide that the first task that needs to be done is to dismantle the $N$ planks. Thus, they decide that each of the following $N$ days, they will dismantle the plank with the smallest length. As they progress with the work, they notice a rather bizarre thing. If on day $T$ they dismantle the plank at position $X$, the length of all planks to the left of plank $X$ increases by $T$ units.

## Task

Find the difference between the sum of the lengths of the dismantled planks and the sum of the initial lengths of the planks.

## Input data

The first line of the file `biscuiti.in` contains the number $N$. The next $N$ lines contain the initial length of the plank $i-1$.

## Output data

The first line of the file `biscuiti.out` should contain the required number $K$.

## Constraints and clarifications

$1 \leq N \leq 100.000$

$1 \leq X_i \leq 1.000$, $X_i$ is the initial length of the plank $i$

If they have to choose between multiple planks of equal lengths, the workers will choose the left-most one.

The initial day is day 1.

Plank $i$ ($i \geq 2$) has planks 1, 2, 3 $\dots$ $i-1$ to its left.

## Example

`biscuiti.in`
```
7
9
10
6
6
4
9
8
```
`biscuiti.out`
```
36
```