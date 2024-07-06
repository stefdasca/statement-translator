# Task

Write a program that determines the maximum number of successive jumps Spiderman can make, starting from any building, as well as the positions of the buildings that form the maximum path.

# Input data

The file `spider.in` contains, on the first line, two natural numbers, $m$ and $n$, separated by a space. Each of the next $m$ rows contains $n$ natural numbers, separated by a space, representing the heights of the buildings.

# Output data

The output file `spider.out` will contain, on the first line, a single natural number $k$, representing the maximum number of jumps. The next $k$ lines contain two natural numbers each, separated by a space, representing the coordinates of the buildings that form the maximum path, in the order of traversal. If there are multiple solutions, the file will contain the path that starts from the position $(i, j)$ with the smallest $i$, and if there are multiple solutions with the same smallest $i$, the file will contain the solution with the smallest $i$ and $j$ values.

# Constraints and clarifications

* $1 \leq m, n \leq 1\ 000$;
* The heights of the buildings are natural numbers in the range $[1, 10\ 000\ 000]$.
* In any $2 \times 2$ square area of neighboring buildings, there are **at most** 2 buildings of the same height.

# Example

`spider.in`
```
5 5
35 38 42 40 50
34 38 30 75 50
70 78 88 86 30
39 90 88 23 25
35 80 89 90 34
```

`spider.out`
```
8
5 4
5 3
4 3
3 3
3 4
2 4
2 5
1 5
1 4
```

## Explanation

Spiderman starts from the 90-meter building located at position $(5, 4)$, makes 8 jumps, and reaches the position $(1, 4)$, from where he can no longer jump.