Turnuri5

At school, Bulănel faces the following problem: he is given a sheet containing $N$ x $M$ points arranged in $N$ rows and $M$ columns. The rows are numbered from bottom to top, from $0$ to $N-1$, and the columns are numbered from left to right, from $0$ to $M-1$. On such a sheet, $T$ towers are marked. The towers have the shape of rectangles with corners at existing points, with the base on line $0$. Each tower $i$ has a height $h_i$ and spans an interval from $l_i$ to $r_i$ on the columns. All towers are disjoint, meaning they do not share any points. Bulănel intends to draw rectangles on the given sheet, but these must be valid. Valid rectangles must have an area strictly greater than $0$, have corners at existing points, have sides parallel to the sheet edges, and not share any points with any of the towers. For example, if Bulănel receives a sheet with $N=5$ rows and $M=6$ columns and a single tower with height $h_1=2$ that spans from $l_1=2$ to $r_1=3$, then he can draw rectangles such as: the rectangle with the top left corner at row $4$, column $0$ and the bottom right corner at row $3$, column $1$. the rectangle with the top left corner at row $3$, column $0$ and the bottom right corner at row $0$, column $1$. In total, he can draw $33$ such rectangles that meet the required properties. He cannot draw, for example: the rectangle with the top left corner at row $4$, column $0$ and the bottom right corner at row $1$, column $4$. the rectangle with the top left corner at row $4$, column $0$ and the bottom right corner at row $2$, column $2$. the rectangle with the top left corner at row $4$, column $0$ and the bottom right corner at row $2$, column $4$. Bulănel asks you to help him count how many valid rectangles he can draw on the given sheet. Since this number can be very large, it is required to display it modulo $10^9 + 7$.

## Task

The input file `turnuri5.in` contains on the first line three natural numbers $N$, $M$ and $T$ which represent, $N$ - the number of rows, $M$ - the number of columns, and $T$ - the number of towers. On the next $T$ lines are the towers. On line $i$ there are three natural numbers $h_i$, $l_i$, and $r_i$ which represent $h_i$ - the height of the tower, $l_i$ - the left end of the tower interval on the columns, $r_i$ - the right end of the tower interval on the columns.

## Output data

The output file `turnuri5.out` must contain one line. That line contains a natural number $D$ which represents the number of valid rectangles he can draw modulo $10^9 + 7$.

## Constraints and clarifications

$2 \leq N, M \leq 10^9$

$0 \leq T \leq 100,000$

$0 \leq h_i \leq N - 1$

$0 \leq l_i < r_i \leq M - 1$

Two rectangles are different if the top left corner or the bottom right corner differ.

For tests worth $5$ points, it is guaranteed $N, M, T \leq 10$

For tests worth $10$ points, it is guaranteed $N, M \leq 50, T \leq 10$

For tests worth $20$ points, it is guaranteed $N, M \leq 100$

For tests worth $30$ points, it is guaranteed $N, M \leq 1,000$

For tests worth $50$ points, it is guaranteed $N, T \leq 1,000, M \leq 10^9$

The problem will be evaluated on tests worth $90$ points.

## The examples will represent tests worth $10$ points "from the office".

## Example

`turnuri5.in`
```
5 6 1 2 2 3
```

`turnuri5.out`
```
33
```

`turnuri5.in`
```
10 12 3 5 1 4 1 7 9 8 10 11
```

`turnuri5.out`
```
507
```