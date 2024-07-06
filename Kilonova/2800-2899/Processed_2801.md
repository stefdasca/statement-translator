> “The Six of Pentacles represents help and generosity” just as the competitive programming committee generously offers you the opportunity to win 100 points with the following problem.

~[4dp.png|align=right]

You are given $N$ points with integer coordinates in the plane, each having a weight. A partitioning of the plane through the coordinate point $(x, y)$ is defined as splitting the plane into $4$ quadrants by drawing the vertical line at coordinate $x + 0.5$ and the horizontal line at coordinate $y + 0.5$. The weight of a quadrant is the sum of the weights of the points located in that quadrant. The _imbalance_ of a specific partition is defined as the maximum difference between the weights of any two quadrants.

# Task

For each integer $x$ between $1$ and $N - 1$, find the minimum imbalance for any partition through a point on the vertical line at coordinate $x$.

# Input data

The first line of the input contains the number $N$.

Each of the following $N$ lines contains $3$ integers $x_i, y_i$ and $w_i$, representing the coordinates of the $i$-th point in the plane, along with its weight.

# Output data

The output must contain on the first line $N - 1$ numbers, representing the minimum sought imbalances.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* $1 \leq x_i, y_i \leq N$ for $1 \leq i \leq N$
* $1 \leq w_i \leq 10^9$ for $1 \leq i \leq N$
* The points are not necessarily distinct.

| # | Score  | Constraints          |
| - | ------- | ------------------- |
| 1 | 7      | $1 \leq N \leq 200$ |
| 2 | 17      | $1 \leq N \leq 5\ 000$      |
| 3 | 53      | $1 \leq N \leq 100\ 000$     |
| 4 | 23     | No additional constraints.      |

# Examples

`stdin`
```
4
3 2 5
4 4 2
1 4 4
2 2 1
```

`stdout`
```
6
4
6
```

## Explanation

The first vertical line at coordinate $x = 1.5$ splits the $4$ points into $2$ half-planes. To the left of the vertical line is the point $(1, 4)$ and to the right are the other $3$ points. If we choose the horizontal line at coordinate $y = 3.5$, we obtain $4$ quadrants: the upper-left quadrant contains the point $(1, 4)$ with weight $4$, the upper-right quadrant contains the point $(4, 4)$ with weight $2$, the lower-right quadrant contains the points $(2, 2)$ and $(3, 2)$ with a total weight of $6$, and the lower-left quadrant contains no points and has weight $0$. The imbalance becomes $6 - 0 = 6$.

For $x = 2.5$, we select $y = 2.5$, thus splitting the plane into $4$ quadrants, each containing exactly one of the $4$ points. The imbalance is thus $5 - 1 = 4$.