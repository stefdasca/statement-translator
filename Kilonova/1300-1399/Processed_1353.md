~[img.png|align=right]

Consider a board of dimension $n$, in the form of an equilateral triangle, whose sides are named $A$, $B$ and $C$ and have a length equal to $n$. On sides $A$ and $B$, $n-1$ points are marked that divide the sides into $n$ equal segments. From each marked point on side $A$, a segment parallel to side $B$ is drawn, and from each marked point on side $B$, a segment parallel to side $A$ is drawn. The other end of each drawn segment is on side $C$. In this way, the triangular board contains $\frac{n \cdot (n + 1)}{2}$ elementary boards (that are not crossed by any segment). Thus, on a triangular board of size $n=4$, as in the figure, we have 6 elementary boards in the shape of a rhombus and 4 in the shape of a triangle (those with one side on side $C$ of the triangular board).

We want to divide the triangle into elementary boards with a minimal total cost. If $n=1$, the cost of the division is $0$. For $n \geq 2$ the only permitted operation is a cut from one end to the other along a segment of maximum length, obtaining a triangle of size $n-1$ and a strip. The strip will be divided into elementary boards by cuts along the segments of length 1 that separate the elementary boards that compose it. The obtained triangle will be divided further into elementary boards by repeatedly using the operation described above. The total cost of dividing the triangle of dimension $n$ into elementary boards is equal to the cost of the cut along the segment of maximum length, plus the costs of dividing the obtained strip and the triangle of dimension $n-1$ into elementary boards.

On each elementary board, a number is written. The cost of a cut (whether it’s in a triangle or a strip) is equal to the sum of the values from the elementary boards that have a common side with the segment on which the cut is made, multiplied by the segment’s length. For a triangle of dimension $n \geq 2$, there are exactly 2 possibilities to perform an operation (corresponding to the 2 segments of maximum length, one parallel to side $A$, and the other parallel to side $B$).

A cut in the $NV-SE$ direction (parallel to side $B$) in the triangle from the figure has a cost of $(8+10+3+6+6+12) \cdot 3 = 135$. The cost of dividing the obtained strip into elementary boards is equal to $(10+6) \cdot 1+(6+12) \cdot 1 + (12+5) \cdot 1 = 51$.

# Task

Determine the minimal total cost necessary to divide the triangular board into elementary boards.

# Input data

The file `triunghi.in` contains on the first line a non-zero natural number $n$, representing the dimension of the board. The second line contains $\frac{n \cdot (n + 1)}{2}$ natural numbers, representing the values of the elementary boards in the order from top to bottom and then from left to right, according to the figure above.

# Output data

The file `triunghi.out` contains on the first line the required minimal total cost.

# Constraints and clarifications 

* $1 \leq n \leq 1000$
* $0 \leq$ number on an elementary board $\leq 2000000000$
* It is guaranteed that the result will fit within $32$ bits.
* For $50\%$ of the tests, we will have $n \leq 400$.

# Example

`triunghi.in`
```
4
10 8 6 4 3 12 3 1 6 5
```

`triunghi.out`
```
235
```

## Explanation

To ensure the minimal total cost, a cut can be made in the $NE-SV$ direction with a cost of $3\cdot(10+6+8+3+4+1)=96$, adding the cost of cutting the strip into elementary boards $3+4+4+8+8+10=37$. The remaining triangular board will be cut in the $NE-SV$ direction. The cost of the cut is $2\cdot(3+6+6+12)=54$, the strip cutting cost into elementary boards is $1+3+3+6=13$. The remaining triangular board can be cut in the $NV-SE$ direction. The cost of the cut is $6+12=18$, the strip cutting cost into elementary boards is $12+5=17$, the total minimal cost is $235$.