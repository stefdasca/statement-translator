After a crushing defeat, Zăhărel gave up playing StarCraft and decided to solve a computer science problem instead. Thus, he has $N$ points in the plane, with natural number coordinates. He receives four natural numbers $A$, $B$, $C$, and $D$, and he knows that the slope of the line passing through two points $i$ and $j$ is defined as:
$$
m(i,j) = \frac{y_i - y_j}{x_i - x_j}
$$
He wants to find the number of pairs of points $i \ j (1 \leq i < j \leq N)$ with the property that
$$
\frac{A}{B} \leq m(i,j) \leq \frac{C}{D}
$$

# Task

Given $N$ points in the plane, determine how many pairs of points $i \ j (1 \leq i < j \leq N)$ have the property that
$$
\frac{A}{B} \leq m(i,j) \leq \frac{C}{D}
$$

# Input data

The input file `pante.in` contains on the first line the natural number $N$. The second line contains the natural numbers $A \ B \ C \ D$ separated by a single space. Each of the following $N$ lines contains the coordinates $x \ y$ of each point.

# Output data

The output file `pante.out` will contain a single line which will print the number of pairs with the required property.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* $0 \leq x_i, y_i \leq 2\ 000\ 000\ 000$
* $0 < A, B, C, D \leq 2\ 000\ 000\ 000$
* For $10\%$ of the tests $1 \leq N \leq 700$
* Any two points have different abscissas 

# Example

`pante.in`
```
3
1 2 1 1
0 0
1 1
2 0
```

`pante.out`
```
1
```

## Explanation

The pair of points $(1, 2)$ has the required property. The pair $(2, 3)$ has the slope $-1$, and the pair $(1, 3)$ has the slope $0$.