
# Task

$n$ points are given in the plane $P_1, P_2, \dots, P_n$ and $k$ is a natural number. It is required to verify if it is possible to construct $k$ segments with both ends from the set $\\{P_1, P_2, \dots, P_n\\}$, in such a way that no triangle is formed with vertices in these points.

# Input data
The input file `puncte.in` contains on the first line the number $n$, and on the second line the number $k$.

# Output data
The output will be in the file `puncte.out` which will contain:
- a line containing the character `0`, if there is no solution, OR
- $k+1$ lines, with the first line containing the character `1`, and on the next $k$ lines there will be two numbers separated by a space (in the form $i\ j$ signifying that $P_i P_j$ represents a segment), in the case where there is a solution.

# Constraints and clarifications
- $1 \le n \le 300$
- $1 \le k \le 300$
- If there are multiple solutions, provide one of them.

# Example 1
`puncte.in`
```
4
5
```
`puncte.out`
```
0
```

# Example 2
`puncte.in`
```
4
2
```
`puncte.out`
```
1
1 4
1 2
```
