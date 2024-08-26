## Sabotage

Company A1-809 owns a network consisting of $N$ computers numbered from $1$ to $N$ connected by $M$ cables such that any two computers can communicate with each other either directly through a cable or via other computers they are connected to. Between any two computers, there is at most one cable. You work for company C-109, which is in competition with A1-809, and you have the mission to sabotage their network. What you need to do is try to cut some of the $M$ cables that connect the computers, so that at least two computers are no longer connected. In order not to be caught by the guard Mr. Fane, the operation time must be minimal. Knowing for each cable the time needed to cut it, determine which cables need to be cut to disconnect any two computers in the A1-809 network as quickly as possible.

## Input data

The input file `sabotaj.in` contains on the first line two natural numbers $N$ and $M$ representing the number of computers and the number of cables in the network, respectively. The next $M$ lines contain three natural numbers each: $x$, $y$, and $t$ indicating that there is a cable connecting computer $x$ to computer $y$ and cutting it requires $t$ seconds.

## Output data

The output file `sabotaj.out` will contain on the first line two numbers: $t_{min}$ and $k$ representing the minimum number of seconds required for the operation and the number of cables that need to be cut, in this order and separated by a space. The next $k$ lines will each contain one number, so on the $(i+1)$-th line of the output file will be the index of the $i$-th cut edge. The edges are considered numbered from $1$ to $M$ in the order from the input file and will be displayed in increasing order of the index. If there are multiple solutions all having the same minimal total time, you will display any of them.

## Constraints

$2 \leq N \leq 200$

$1 \leq M \leq 3500$

$1 \leq$ time required to cut a cable $\leq 1024$

## Example

`sabotaj.in`

```
5 7
3 4 2
1 5 2
5 2 8
1 3 7
2 3 1
4 1 9
5 4 5
```

`sabotaj.out`

```
7 2
5
7
```