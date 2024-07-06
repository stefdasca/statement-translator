Our friend, Pit, is in ancient Greece, in the most famous public market. We consider that the market is a rectangle in the plane, with dimensions $X$ and $Y$. If we represent the market on a Cartesian coordinate system \(xOy\), it has the four vertices at the coordinate points \((0,0)\), \((X,0)\), \((X,Y)\), and \((0,Y)\). At each point \((a,b)\), with \(a \in \{1, \dots, X\}\) and \(b \in \{1, \dots, Y\}\), there is a stall selling protractors. Our friend is a businessman and wants to rent a rectangular plot of land, with sides parallel to the sides of the market, and with vertices at natural number coordinates. The vertices of the plot are inside the market or on its sides. In this plot, Pit wants to include as many special stalls as possible, which have the following properties:
- The distance from the origin to the stall is a natural number;
- There is no other stall on the segment between the origin and the stall.

# Task

Given the values of $X$, $Y$, and the coordinates \((S_{X_i}, S_{Y_i})\) and \((D_{X_i}, D_{Y_i})\) for $Q$ plots, where \(1 \leq i \leq Q\), determine, for each plot, the number of special stalls it contains.

# Input data

The first row of the file `agora.in` contains three natural numbers separated by a space, $X$, $Y$, and $Q$, with the significance given in the statement.
The following $Q$ rows contain 4 non-zero natural numbers \(S_{x_i}\), \(S_{y_i}\), \(D_{x_i}\), \(D_{y_i}\), separated by a space, with the significance given in the statement.

# Output data

Each of the first $Q$ rows of the file `agora.out` contains a natural number, the number on line $i$ representing the number of special stalls contained by plot $i$.

# Constraints and clarifications

* \(2 \leq X \leq 7\ 000\)
* \(2 \leq Y \leq 7\ 000\)
* \(1 \leq Q \leq 100\ 000\)
* A stall is part of a plot even if it is on its sides.
* \((S_{X_i}, S_{Y_i})\) and \((D_{X_i}, D_{Y_i})\) will not be outside the rectangle associated with the market, but can be on its sides.
* For tests worth 10 points: \(X, Y \leq 100\) and \(Q \leq 100\).
* For other tests worth 20 points: \(X, Y \leq 2\ 000\) and \(Q \leq 1\ 000\).
* For other tests worth 10 points: \(X, Y \leq 2\ 000\) and \(Q \leq 100\ 000\).

# Example

`agora.in`
```
5 5 2
1 5 3 4
3 4 4 3
```

`agora.out`
```
1
2
```

## Explanation

The first plot contains the special stall at point \((3,4)\).
The second plot contains the special stalls \((3,4)\) and \((4,3)\).