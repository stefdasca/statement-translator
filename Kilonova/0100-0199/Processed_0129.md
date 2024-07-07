Let us consider a tree with `N` vertices, numbered from `1` to `N`.

# Task
Write a program that adds, if possible, a minimum number of edges so that each vertex (whether terminal or not) belongs to exactly one cycle.

# Input data
The input file `arbore.in` contains on the first line `T`, the number of scenarios. For each scenario contains on the first line `N` - the number of vertices in the tree, and on the following `N-1` lines $x_{i} \\;y_{i}$ - the endpoints of edge `i`.

# Output data
The output file `arbore.out` will contain for each scenario on the first line the value `−1` if the problem does not admit a solution, or the number of edges added if the problem admits a solution. If the problem admits a solution, on each of the following lines the endpoints of an added edge will be written, separated by a space, in the form $a_{i} \\;b_{i}$:

# Constraints and clarifications
* $3 \\leq S_N \\leq 100\ 000$, where $S_N$ is the sum of the `N` values for all scenarios
* `3 \\leq N \\leq 100\ 000`
* $x_i, y_i$ are integers in the range `[1, N]`
* The problem has been modified

# Example

`arbore.in`
```
2
4
1 2
2 3
2 4
7
1 2
1 3
3 5
3 4
5 6
5 7	
```

`arbore.out`
```
-1
2
6 7
4 2
