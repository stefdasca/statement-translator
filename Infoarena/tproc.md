# Tproc

A multiprocessor system consists of $K$ processors. On this system, an application consisting of $N$ independent processes, numbered from $1$ to $N$, needs to be executed. Each process must be entirely executed on one of the $K$ processors. Because some processes use data from completely different memory locations, if certain pairs of processes (called incompatible processes) are executed on the same processor, cache thrashing will occur, which will significantly reduce the system's performance. For each of these $P$ pairs of incompatible processes $(i, j)$, the performance penalty on $i, j$ is known, caused if the two processes are executed on the same processor. The total performance penalty is equal to the sum of performance penalties for each pair of incompatible processes executed on the same processor. Determine the minimum possible total performance penalty for executing the $N$ processes on the $K$ processors of the system. In solving the problem, you can use the following particularity of the application composed of the $N$ processes: The processes are organized into $M$ groups, based on the type of processing they need to perform. The groups are numbered from $1$ to $M$. Each group contains at most $8$ processes. A process can be part of multiple groups. If $2$ processes $i$ and $j$ are incompatible, then there will be at least one group $X$ to which both process $i$ and process $j$ belong. The $M$ groups are organized into a tree structure. Specifically, there are $M-1$ pairs of groups with the property that between the two groups $X$ and $Y$ in a pair there are reciprocal references, and the graph formed by the groups as nodes and the pairs of groups as edges forms a tree (connected graph without cycles). All the groups to which a process $i$ belongs form a subtree of the group tree (this is due to the fact that, within the application, it must be possible to reach any group that process $i$ is part of, from any other group that process $i$ is part of, via the references between groups). This last property is equivalent to the following: if a process $i$ is part of groups $X$ and $Y$, then it will be part of all the groups along the unique path between $X$ and $Y$.

## Input data

The first line of the input file `tproc.in` contains the integers $M$, $N$, and $K$, separated by a space. The next $M-1$ lines contain $2$ integers $X$ and $Y$, separated by a space, representing $2$ groups between which there is a reference. The next $M$ lines describe the composition of each group. The $X$-th of these $M$ lines represents the description of the group numbered $X$. The first number on the line represents the number $T$ of processes that are part of group $X$. The next $T$ numbers represent the numbers of the $T$ processes. The $T+1$ numbers on the line are separated by a space. The next line contains the integer number $P$ for pairs of incompatible processes. The next $P$ lines contain $3$ integers, $i$, $j$, and $pe_{i, j}$, separated by a space, representing the numbers of the $2$ incompatible processes within the pair and the performance penalty associated with executing the $2$ processes on the same processor.

## Output data

In the output file `tproc.out` you will print the minimum possible total penalty for executing the $N$ processes on the $K$ processors of the system.

## Constraints

$1 \leq M \leq 500$

$1 \leq N \leq 500$

$1 \leq K \leq 8$

Each group will contain between $0$ and $8$ processes (inclusive).

A process can be part of any number of groups (at least one).

$0 \leq P \leq 3000$

$0 \leq pe_{i, j} \leq 1000$

## Example

`tproc.in` 
```
6 9 3
1 3
6 3
4 3
5 3
2 1
7 1
2 3
4 5 7 9
5 1 2 3 5 9
8 1 2 3 4 6 7 8 9
5 2 4 6 7 8
5 2 4 6 7 8
6 1 4 6 7 8 9
22
1 2 703
1 3 485
1 4 384
1 5 216
1 7 670
1 9 410
2 3 789
2 4 977
2 6 210
2 7 856
2 9 610
3 4 780
3 9 453
4 6 149
4 8 528
4 9 85
5 9 949
6 7 754
6 8 457
7 8 204
7 9 827
8 9 700
```

`tproc.out`
```
937
```

`tproc.in`
```
2 10 2
1 2
6 1 2 3 4 5 6
6 1 2 7 8 9 10
12
1 3 1
3 4 1
4 2 1
3 5 1
5 6 1
6 1 1
1 7 1
7 8 1
8 1 1
2 7 1
2 8 1
2 9 1
```

`tproc.out`
```
1
```

## Explanation

In the first example, an optimal solution for allocating the $9$ processes on the $3$ processors is the following (the $i$-th number in the sequence indicates on which processor the process $i$ is executed): $2 2 3 1 3 1 3 2 1$. In the second example, an optimal solution for allocating the $10$ processes on the $2$ processors is the following: $1 1 2 1 1 2 2 2 2 2$.