Superpoligon

Last year, Marcel was an expert in simple geometric figures. He even knew how to find the number of pairs of indistinguishable triangles that could be formed by choosing vertices from a given set of points. Recently, Marcel has gotten even more skilled and now challenges you to solve a generalization:

## Task

You are given $N$ distinct points, a number $K$ and a number $M$. For each $r$ from $3$ to $K$, find the number modulo $M$ of ordered pairs of indistinguishable polygons with $r$ points that can be formed by choosing vertices from a given set of points. Each polygon may self-intersect but cannot contain the same point twice. Two polygons are considered indistinguishable if there exists a translation such that the polygons overlap perfectly. For example, any polygon is indistinguishable from itself. Note: Overlapping is verified by checking if the vertices coincide, not if the lines coincide - a relevant fact in the case of collinear points: $(0, 0) - (0, 1) - (0, 3)$ is different from $(0, 0) - (0, 2) - (0, 3)$. Two polygons are identical if the points of one can be obtained by a circular permutation of the other. For example, $(0, 0) - (0, 1) - (0, 2)$ is the same polygon as $(0, 1) - (0, 2) - (0, 0)$, but different from $(0, 0) - (0, 2) - (0, 1)$.

## Input data

The input file `superpoligon.in` contains on the first line the natural numbers $N$, $K$, and $M$ $(10^8 \leq M \leq 10^9 + 7)$, and on the next $N$ lines, there are $2$ integers with absolute value less than $10^9$ representing the coordinates of the points.

## Output data

The output file `superpoligon.out` will contain $K - 2$ lines, with the remainder of the required number for $r = i + 2$ modulo $M$ on the $i$-th line.
Subtasks:
- Subtask $1$ - $10$ points (tests $1$ and $2$): $3 \leq K \leq N \leq 8$, $M = 10^9 + 7$
- Subtask $2$ - $30$ points (tests $3\ldots 8$): $3 \leq K \leq N \leq 100$, $M = 10^9 + 7$
- Subtask $3$ - $15$ points (tests $9\ldots 11$): $3 \leq K \leq N \leq 40$, $M = 10^9 + 7$
- Subtask $4$ - $15$ points (tests $12\ldots 14$): $3 \leq K \leq N \leq 40$
- Subtask $5$ - $15$ points (tests $15\ldots 17$): $3 \leq K \leq N \leq 1,000$, $M = 10^9 + 7$
- Subtask $6$ - $15$ points (tests $18\ldots 20$): $3 \leq K \leq N \leq 1,000$

## Example

`superpoligon.in`
```
8 8 1000000007
0 0
0 2
1 1
1 3
3 0
3 2
4 1
4 3
```
`superpoligon.out`
```
160
456
1344
3360
5760
5040
```

## Explanation

There are $160$ pairs of indistinguishable triangles, such as $\{ (0, 0), (0, 2), (1, 1) \}$ with $\{ (3, 0), (3, 2), (4, 1) \}$. Notice that $\{ (0, 0), (0, 2), (1, 1) \}$ and $\{ (3, 0), (3, 2), (4, 1) \}$ is considered a different pair from $\{ (0, 0), (1, 1), (0, 2) \}$ with $\{ (3, 0), (4, 1), (3, 2) \}$. Notice that $\{ (0, 0), (0, 2), (1, 1) \}$ and $\{ (3, 0), (3, 2), (4, 1) \}$ is considered an identical pair with $\{ (0, 2), (1, 1), (0, 0) \}$ and $\{ (3, 2), (4, 1), (3, 0) \}$. Also, $\{ (0, 0), (0, 2), (1, 1) \}$ and $\{ (3, 0), (3, 2), (4, 1) \}$ is considered a different pair from $\{ (3, 0), (3, 2), (4, 1) \}$ and $\{ (0, 0), (0, 2), (1, 1) \}$.