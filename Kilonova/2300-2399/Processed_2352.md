```markdown
Given is a set of segments. The segments are described by their two endpoints, and the endpoints by their Cartesian coordinates. A segment cannot be a single point. Two segments are considered adjacent if they have a common endpoint. 
Segments $S_i$ and $S_j$ are called **connected** if there is a sequence of segments, starting with $S_i$ and ending with $S_j$, in which two consecutive segments are adjacent.

~[poza_exemplu_segmente.png|align=center|width=50%]

In the adjacent figure, segments $S_2$ and $S_5$ are connected, because there is a sequence of consecutively adjacent segments, namely $S_2$, $S_3$, and $S_5$.

A subset of segments forms a **network**, if the respective segments are connected among them, without having connections with other segments that do not belong to the subset. A set of segments can have one or more networks. For the above figure, the networks are $\\{S_1, S_2, S_3, S_5\\}$, $\\{S_4\\}$ and $\\{S_6, S_7\\}$.

# Task

Given the number of segments and their coordinates, display the number of networks.

# Input data

The file `segmente.in` contains on the first line a natural number $n$, representing the number of segments. Each of the following $n$ lines contains the coordinates of the segment's endpoints, in the form $x_1$, $y_1$, $x_2$, $y_2$. The values are separated by a space and are integers.

# Output data

In the file `segmente.out`, the file `segmente.out` will contain, on the first line, a natural number representing the number of networks.

# Constraints and clarifications

- $1 \leq n \leq 700\ 000$
- $-100\ 000 \leq x_1, y_1, x_2, y_2 \leq 100\ 000$

# Example

`segmente.in`
```
7
1 7 4 8 
2 6 4 8 
4 8 7 4 
2 4 9 7 
5 2 7 4 
8 3 11 8 
8 3 13 1 
```

`segmente.out`
```
3
```

## Explanation

Example from the figure.
```