Workers

The $N$ workers at the Brewery Factory are having a tough day today because they need to check the quality of the $M$ batches proposed for export. The Factory Director has posted a list with the moments at which each batch check should start, $A_i$, as well as the approximate duration that a worker spends doing the respective check, $B_i$. To be able to go home as early as possible, the workers want to perform these checks in a very organized manner: they will take the batches in chronological order according to the start time written on the list, with each batch being assigned to the free worker who has the $K$-th order number. Once a worker starts checking batch $i$, they will be occupied for $B_i$ seconds, being free again at the moment $A_i + B_i$.

## Task

Given $N$, $M$, $K$ and the $M$ pairs $A$ $B$, determine and display for each batch which worker will be assigned to it.

## Input data

The input file `muncitori.in` will contain on the first line the numbers $N$, $M$, and $K$, as described in the statement. The next $M$ lines will contain pairs $A_i$ $B_i$, the start moment and the duration for the checking of batch $i$.

## Output data

The output file `muncitori.out` will contain $M$ natural numbers, on separate lines, the $i$-th of them representing the worker who performs the check with order number $i$, considering the tasks in the order they are executed (ordered by the start time of the check).

## Constraints and clarifications

\[
1 \leq N \leq 100\ 000
\]
\[
1 \leq M \leq 100\ 000
\]
\[
1 \leq K \leq N
\]
\[
1 \leq A_i, B_i \leq 1\ 000\ 000
\]
It is guaranteed that for each of the $M$ checks, there will be at least $K$ available workers.
For 20% of tests $N, M \leq 1\ 000$
For another 20% of tests $K = 1$.
There are no two checks that start at the same time.

## Example

`muncitori.in`
```
4 3 1
4 6
5 2
7 3
```

`muncitori.out`
```
1
2
2
```