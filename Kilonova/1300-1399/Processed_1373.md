```markdown
Let $N$ be segments in the `XOY` coordinate plane. The segments are either horizontal (parallel to the `OX` axis) or vertical (parallel to the `OY` axis) and have endpoints at integer coordinates. Also, no two horizontal segments lie on the same line and no two vertical segments lie on the same line. An operation can be simultaneously applied to all segments, extending both endpoints by an integer value $D$. For any segment, if the length is $L$, then after extension its size is $L + 2 \cdot D$.

# Task

Determine the minimum value $D$ by which the segments must be extended so that after extension the segments enclose at least one rectangle.

# Input data

The first line of the file `segmente.in` contains a natural number $N$ representing the number of segments. Each of the next $N$ lines contains four integers $x_1 y_1 x_2 y_2$. The first two represent one endpoint of the segment, and the last two the other endpoint.

# Output data

The first line of the file `segmente.out` will contain a natural number $D$ representing the minimum size required to extend all segments to form at least one rectangle.

# Constraints and clarifications

* $4 \leq N \leq 1\ 000$
* The endpoints of the segments are integers in the range $[-500\ 000\ 000, 500\ 000\ 000]$
* Any segment has an initial length of at least $1$
* For the input data, there is initially no rectangle already formed; also, there will be at least $2$ vertical segments and at least two horizontal segments
* It is guaranteed that there is a solution with $1 \leq D \leq 1\ 000\ 000\ 000$
* For $50\%$ of tests, $N \leq 200$

# Example

`segmente.in`
```
5
1 2 1 3
3 2 4 2
2 3 2 5
5 2 5 7
5 6 7 6
```

`segmente.out`
```
3
```

## Explanation

~[7f4d9a47014125917f8d149ba6d88eb8.png]

The initial segments are the thick ones, the dotted line segments are the extensions by $3$ units at both ends of all segments, and the shaded area marks the rectangle that was formed after the extension with $D = 3$.
```

Note: Double-checked grammar and syntax, all appear correct.