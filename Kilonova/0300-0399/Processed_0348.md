
Coami, stressed about college, decided to play some *Metin*2.

The objective of *Metin*2 is to break *Metin Stones*. A *Metin Stone* is a convex polygon with $4$ vertices. Because Coami is a competitive player, he wants to MinMax his farming strategy, so he wants to know the area of the range in which he can hit all the stones at the same time.

Strictly speaking, you are given $N$ convex quadrilaterals, and you need to compute the total area of the shape inside ALL of the given quadrilaterals.

# Task

The first line of the input contains an integer $N$ ($1 \leq N \leq 10^5$), the number of *Metin Stones*.

Each *Metin Stone* is described on $4$ lines, each line containing a pair of integers $(x, y)$, $(-4 \cdot 10^5 \leq x, y \leq 4 \cdot 10^5)$, where $(x, y)$ is a vertex of the *Metin Stone*. The points are given in trigonometrical order.

For tests worth $10$ points, the following condition holds $1 \leq N \leq 10^2$.

For tests worth other $30$ points, the following condition holds $1 \leq N \leq 10^3$.

# Output

Output on one line the requested number with a precision of $10^{-6}$.

# Examples

`stdin`
```
2
-5 0
-5 -6
5 -4
5 1
-4 1
-5 -8
5 -6
2 0
```
`stdout`
```
40.072108018
```

`stdin`
```
5
-1 5
-3 -2
4 2
3 6
-5 8
-4 -2
2 0
2 7
-2 8
-1 0
2 0
3 4
-5 5
-4 1
4 1
1 8
-3 4
-1 -1
4 0
3 7
```
`stdout`
```
13.719694617
```
```
