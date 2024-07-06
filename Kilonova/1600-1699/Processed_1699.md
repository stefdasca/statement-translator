Bob Ross is very famous for his oil paintings of mountainous landscapes. Today he decided to paint a new masterpiece, but he will approach his creative process in a novel way.

Bob has $N$ points on an infinite canvas, with the $i$-th point having coordinates ($x_i, y_i$). The points have the property that $x_i$ < $x_{i+1}$. He will choose a number of points, and for each chosen point $i$, he will color the segments between pairs of points ($i - 1, i$) and ($i, i+1$).

By choosing a subset of the $N$ points, he will color the segments incident to these points in the following manner: each time he chooses a point, he will color the segments incident to that point (any point has two neighbors, except for the first and the last point, which have only one neighbor). If a segment is already colored, then it will not be colored a second time, and the amount of paint on the brush will not decrease.

Initially, Bob has a brush with an amount $V$ of paint. The amount of paint required to color a segment is equal to the **square of the length of that segment**, and after coloring, the amount of paint on the brush decreases by this value.

# Task

Bob thought of the following $K$ scenarios. If in scenario $i$ he had a brush with an amount $V_i$ of paint, what is the maximum number $P_i$, such that no matter how we choose $P_i$ points, we can color all the adjacent segments to those points?

# Input data

The first line of the input file `ross.in` will contain a single number $N$ representing the number of points on Bob's canvas. The next $N$ lines will contain $2$ numbers each, $x_i$, $y_i$ separated by a space, representing the coordinates of point $i$. The next line contains the number $K$ of Bob's scenarios. The next $K$ lines will contain one number $V_i$ each representing the amount of paint on the brush for scenario $i$.

# Output data

The output file `ross.out` will contain $K$ lines, line $i$ having a single number $P_i$ representing the answer for scenario $i$.

# Constraints and clarifications

* $1 \leq N \leq 2\ 000$
* $1 \leq K \leq 10^5$
* $1 \leq x_i, y_i \leq 10^6$
* $0 \leq V_i \leq 10^{15}$
* $x_i < x_{i + 1}$; $\forall i \in \{1, 2, \dots, N - 1\}$;
* For tests worth $17$ points: $N \leq 15$, $K \leq 10$
* For other tests worth $13$ points: $N \leq 20, K \leq 10^5$
* For other tests worth $11$ points: $N, K, V_i, x_i, y_i \leq 100$
* For other tests worth $24$ points: $N \leq 200$
* For other tests worth $35$ points: No additional constraints.

# Example 1

`ross.in`
```
6
2 2
4 4
5 1
7 6
8 5
10 2
2
44
55
```

`ross.out`
```
1
2
```

## Explanation

For $V = 44$, the answer is $1$. No matter how we choose one point, we can color the segments adjacent to it. However, there exist pairs of $2$ points, for which coloring requires more paint than $44$ (for example, choosing the points ($5, 1$) and ($10, 2$), we need a brush with an amount of paint greater than or equal to $52$).

For $V = 55$, the answer is $2$. For any $2$ chosen pairs of points, the amount of paint required is less than or equal to $55$. Choosing the points ($4, 4$), ($7, 6$), and ($10, 2$), the cost of coloring exceeds $55$, so the answer is $2$.

~[ross.png]