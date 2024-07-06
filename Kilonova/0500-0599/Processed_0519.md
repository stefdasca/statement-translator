*Boss, if N is 30,000, clearly you try $N^2$ optimized!* (Friedrich Nietzsche)

Given a connected graph without loops with `N` nodes and `M` edges. Each edge must be labeled with a number from `1` to `M` such that no two edges share the same label and, for every node with a degree greater than `1`, the greatest common divisor of the labels of the incident edges is `1`.

# Input data
The file `nogcd.in` contains on the first line the natural numbers `N` and `M` separated by a space, and on the following `M` lines, there are two numbers `x` and `y` separated by a space, between `1` and `N`, which means there is an edge between the nodes `x` and `y`.

# Output data
The file `nogcd.out` will contain `M` lines, each line containing three natural numbers `x y v` separated by a space, representing the endpoints of the edge `(x, y)` and the value of the label of this edge.

# Constraints and clarifications
* `1 \ \leq N \ \leq 100\ 000`
* `1 \ \leq M \ \leq 220\ 000`

# Example
`nogcd.in`
```
5 6
1 2
2 3
1 3
4 1
3 4
3 5
```
`nogcd.out`
```
1 2 2
1 4 1
1 3 3
3 2 5
3 4 4
3 5 6
```

Explanation
---

The graph has `5` nodes and `6` edges.
For node `1` the labels are `2`, `1` and `3`; `gcd(2,1,3)=1`.
For node `2` the labels are `2` and `5`; `gcd(2,5)=1`.
For node `3` the labels are `3, 4, 5` and `6`; `gcd(3,4,5,6)=1`.
For node `4` the labels are `1` and `4`; `gcd(1,4)=1`.
Node `5` has a degree of `1`, so gcd is not calculated.