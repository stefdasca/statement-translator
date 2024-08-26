## Task

Everyone knows TractoMarm, the one who counts nodes in trees faster than others can count the fingers on their hands. A few days ago, TractoMarm decided to "play" with Bercea's $N$ safes, where the unit of measurement of value is a million euros. The $N$ safes are arranged in the form of a tree (an acyclic connected graph), with the safe numbered 1 as the root. Each safe is associated with a key that can open the safe. Unfortunately (or fortunately), there may be two or more safes that can be opened with the same key. Knowing this, TractoMarm wants to find out, for each safe $x$, which key opens the most safes in the sub-tree of $x$.

## Input data

The input file `egal.in` contains on the first line $N$, the number of Bercea's safes. The next $N - 1$ lines contain two numbers $x$ and $y$ each, indicating that there is a connection between safe $x$ and safe $y$. On the last line, there are $N$ numbers, the $i$-th of which indicates the index of the key that opens safe $i$.

## Output data

In the output file `egal.out`, you will print $N$ lines. The line numbering $i$ will contain the index of the key that has the highest frequency in the sub-tree of $i$ and how many times it appears.

## Constraints and clarifications

$1 \leq N \leq 100000$

If there are multiple keys with the maximum number of occurrences, print the one with the minimum index.

The index of a key fits in a signed 32-bit integer.

Attention! TractoMarm reminds you that the available stack memory is a maximum of $8$ MB!

## Example

`egal.in`
```
7
1 2
1 3
3 4
3 5
5 6
5 7
1 3 2 2 2 1 1
```

`egal.out`
```
1 3
3 1
2 3
2 1
1 2
1 1
1 1
```