## Task

A Romanian software company has bought $N$ computers, which will be connected in a network. A connection can be established between any 2 distinct computers and is bidirectional (if the 2 computers are labeled with $i$ and $j$, then data can be transmitted from $i$ to $j$ as well as from $j$ to $i$). Determine a way to interconnect the $N$ computers so that any 2 computers can transmit data to each other (directly or indirectly, using other intermediary computers). There is one additional requirement: the formed network must contain exactly $K$ critical pairs. A pair $(i,j)$ is critical if there is a connection which, if removed, would prevent data from being transmitted from $i$ to $j$ (and vice versa).

## Input data

The input file `perechi2.in` contains 2 integers, separated by a space: $N$, the number of computers, and $K$, the number of critical pairs.

## Output data

In the output file `perechi2.out` you will print the connections that form the network, one connection per line. For each connection, print 2 integers, separated by a space: $i$ and $j$, representing the 2 computers directly connected by the respective connection. If it is not possible to form a network having $K$ critical pairs, print only the number $-1$ in the output file.

## Constraints

$1 \leq N \leq 100$

$0 \leq K \leq N*(N-1)/2$

There can be at most one connection between 2 computers.

## Example

`perechi2.in`
```
7 12
```

`perechi2.out`
```
1 2
1 3
2 3
3 4
4 5
4 6
4 7
5 6
5 7
6 7
```
