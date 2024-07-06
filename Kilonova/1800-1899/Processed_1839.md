```markdown
`<Link />` wants to get his hands on a new `C chart`, which can only be found on `The Isle of <meta>`, inside `The Temple of <element>`. To enter the Temple, he must first solve a puzzle.

`<Link />` must first enter a $T$-dimensional plane, so each point in space is described by a vector of length $T: [x_1, x_2, x_3, \dots, x_T]$. In this plane, there are $N$ stationary statues numbered from $1$ to $N$ and $Q$ movable statues numbered from $1$ to $Q$. `<Link />` can make the following move **up to $K$** times: he can choose any **movable** statue and an axis and move that statue exactly one unit in any direction. That is, the coordinates of such a statue will become either $[x_1, x_2, \dots, x_i−1, \dots, x_T]$ or $[x_1, x_2, \dots, x_i+1, \dots, x_T]$.

To unlock the entrance to `The Temple of <element>`, he must move the **movable** statues in such a way that the sum of Manhattan distances between each **movable** statue and each **stationary** statue is minimized.

The Manhattan distance between two $T$-dimensional points $[x_1, x_2, \dots, x_T]$ and $[y_1, y_2, \dots, y_T]$ is defined as:

$$
dist([x_1, x_2, \dots, x_T], [y_1, y_2, \dots, y_T]) = \displaystyle \sum_{i = 1}^{T} |x_i - y_i|
$$

Let $s$ be a vector with coordinates for each **stationary** statue and $m$ be a vector with coordinates for each **movable** statue after performing at most $K$ optimal moves. Calculate:

$$
\displaystyle \sum_{i = 1}^{N} \sum_{j = 1}^{Q} dist(s_i, m_j)
$$

# Input data

The first line of the input will contain integers $N, T, K$ which represent the number of stationary statues, the dimension, and the maximum number of moves `<Link />` can make.

The following $N$ lines each contain $T$ integers separated by spaces. The $i$-th line of these represents the coordinates of the $i$-th **stationary** statue.

The next line contains a single integer $Q$ representing the number of **movable** statues.

The last $Q$ lines each contain $T$ integers separated by spaces, representing the coordinates of each movable statue, in a similar way to the **stationary** statues.

# Output data

Print a single integer representing the minimum sum of Manhattan distances from each **stationary** statue to each **movable** statue after making at most $K$ moves.

# Constraints and clarifications

* $1 \leq N, Q \leq 100\ 000$
* $1 \leq T \leq 10$
* $1 \leq K \leq 10^{15}$
* All coordinates are integers from $0$ to $10^9$ inclusive.
* It's guaranteed that the answer fits within a 64-bit signed integer.

| # | Points | Constraints     |
| - | ------- | ------------------- |
| 1 | 7      | $T = Q = 1$         |
| 2 | 10     | $N, Q, K \leq 100$  |
| 3 | 12     | $N, Q \leq 50$      |
| 4 | 28     | $T = 1$             |
| 5 | 17     | $Q = 1$             |
| 6 | 26     | No additional constraints |

# Example 1

`stdin`
```
3 2 7
8 1
2 0
0 3
2
10 2
2 6
```

`stdout`
```
29
```

# Example 2

`stdin`
```
6 4 200
12 1 19 10
45 3 42 44
42 32 40 41
39 12 32 47
35 18 40 20
38 14 25 1
3
34 10 7 9
29 32 21 50
16 36 18 38
```

`stdout`
```
708
```
```