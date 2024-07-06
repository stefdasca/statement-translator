~[paianjen.png|align=right]

A spider has woven a web, in which the nodes are arranged in a grid with $m$ rows (numbered from $0$ to $m-1$) and $n$ columns (numbered from $0$ to $n-1$) as shown in the figure. Initially, any two neighboring nodes (horizontally or vertically) were connected by web segments of length $1$. Over time, some portions of the web have deteriorated, becoming unsafe. On the web, at any given moment, there are the spider and a fly, in nodes with known coordinates.

# Task

Determine the length of the shortest path the spider must follow, using only the safe portions of the web, to reach the fly. Additionally, provide such a path.

# Input data

The input file `paianjen.in` contains:
- the first line contains two natural numbers $m$, $n$, separated by a space, representing the number of rows and the number of columns of the web, respectively;
- the second line contains two natural numbers $l_p$, $c_p$, separated by a space, representing the row and the column of the node where the spider is initially located;
- the third line contains two natural numbers $l_m$, $c_m$ separated by a space, representing the row and the column where the fly is initially located;
- the fourth line contains a natural number $k$, representing the number of deteriorated portions of the web;
- each of the next $k$ lines contains four natural values $l_1$, $c_1$, $l_2$, $c_2$, separated by spaces, representing the coordinates of the ends of the $k$ deteriorated portions of the web (the row and then the column for each end).

# Output data

The output file `paianjen.out` will contain:
- the first line contains a natural number min representing the length of the minimum path traveled by the spider, expressed in number of segments of length $1$;
- on the following min+1 lines, the nodes through which the spider passes are written, one node per line. For each node, the row and the column where it is located are written, separated by a space.

# Constraints and clarifications

* $1 \leq m, n \leq 140$;
* $1 \leq k \leq 2 \cdot (m \cdot n - m - n + 1)$;
* The length of the minimum path is at most $15\ 000$;
* For the test data, there is always a solution. If the problem has multiple solutions, only one will be displayed.
* The unsafe portions are specified in the input file in any order. Any two unsafe horizontal portions can intersect at most at one end. Likewise, any two unsafe vertical portions can intersect at most at one end.
* $30\ \%$ of the score is awarded for determining the length of the minimum path, and $100\ \%$ for solving both tasks.

# Example

`paianjen.in`
```
9 7
2 3
7 4
8
2 4 2 5
2 3 3 3
3 0 3 1
3 3 3 5
4 4 5 4
6 4 6 5
6 5 7 5
7 2 7 3
```

`paianjen.out`
```
8
2 3
2 2
3 2
4 2
5 2
6 2
6 3
7 3
7 4
```

## Explanation

The problem corresponds to the figure above. The optimal path is drawn with a thick line, and the unsafe portions are dotted.