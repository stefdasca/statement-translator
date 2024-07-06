Every four years, students from Lund gather to organize the Lund Carnival. For several days, a park is filled with tents where all kinds of festive activities take place. The person responsible for organizing this event is the carnival director.

In total, there have been $N$ carnivals so far, each managed by a different director. The directors are numbered from $0$ to $N - 1$ in chronological order. Each director $i$ has expressed their opinion about how good their predecessors were by publishing a ranking of the directors $0, 1, \ldots, i - 1$ in order from the best to the worst.

The next Lund Carnival will take place in 2026. In the meantime, all past carnival directors have gathered for a group photo. However, it would be strange if directors $i$ and $j$ (where $i < j$) end up next to each other if $i$ is **strictly** in the second half of $j$'s ranking (i.e., if $i$'s position in $j$'s ranking is in the interval $(\lfloor \frac{j + 1}{2} \rfloor, \ldots, j - 1)$).

For example:

* If director $4$ gave the ranking `3 2 1 0`, then $4$ can stand next to $3$ or $2$, but not next to $1$ or $0$.
* If director $5$ gave the ranking `4 3 2 1 0`, then $5$ can stand next to $4, 3$, or $2$, but not next to $1$ or $0$. Note that it is acceptable for a director to be exactly in the middle of another's ranking.

The figure below illustrates example 1. Here, director $5$ stands next to directors $2$ and $3$, and director $4$ stands only next to director $2$.

~[carnival-sample1.png]

You are given the rankings that the directors have published. Your task is to arrange directors $0, 1, \ldots, N - 1$ in a line, such that if $i$ and $j$ are adjacent (where $i < j$), then $i$ **is not** strictly in the second half of $j$'s ranking.

# Input data

The first line contains a positive integer $N$, representing the number of directors.

The next $N - 1$ lines contain the rankings. The first of these lines contains the ranking of director $1$, the second line contains the ranking of director $2$, and so on up to director $N - 1$. Director $0$ is missing because director $0$ had no predecessors to rank.

The ranking of director $i$ is a list of $i$ integers $p_{i, 0}, p_{i, 1}, \ldots, p_{i, i - 1}$, where each integer from $0$ to $i - 1$ appears exactly once. $p_{i, 0}$ represents the best director according to director $i$, and $p_{i, i - 1}$ represents the worst director according to director $i$.

It can always be demonstrated that there is a solution.

# Output data

Print a list of integers, an ordering of the numbers $0, 1, \ldots, N - 1$, such that for every pair of adjacent numbers, none is strictly in the second half of the other's ranking. If there are multiple solutions, you can print any of them.

# Constraints and clarifications

* $1 \leq N \leq 1\ 000$
* $0 \leq p_{i, 0}, p_{i, 1}, \ldots, p_{i, i - 1} \leq i - 1$ for $i = 0, 1, \ldots, N - 1$

Your solution will be tested on multiple groups of tests, each group having a certain number of points associated with it. Each group of tests can contain multiple tests. To obtain the points for a group of tests, the solution must pass all the tests in that group.

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 11      | $p_{i, 0} > p_{i, 1} > \ldots > p_{i, i - 1}$ for each $i$ such that $1 \leq i \leq N - 1$ |
| 2 | 23      | $p_{i, 0} < p_{i, 1} < \ldots < p_{i, i - 1}$ for each $i$ such that $1 \leq i \leq N - 1$  |
| 3 | 29      | $N \leq 8$    |
| 4 | 37      | No additional constraints.  |

# Example 1

`stdin`
```
6
0
1 0
2 1 0
3 2 1 0
4 3 2 1 0
```

`stdout`
```
4 2 5 3 1 0
```

## Explanation

The first example respects the condition of test group 1. In this example, neither director $2$ nor director $3$ can stand next to director $0$, and neither director $4$ nor director $5$ can stand next to directors $0$ and $1$. The example output has been illustrated in the figure above.

# Example 2

`stdin`
```
5
0
0 1
0 1 2
0 1 2 3
```

`stdout`
```
2 0 4 1 3
```

## Explanation

The second example respects the condition of test group 2. In this example, director $2$ cannot stand next to director $1$, director $3$ cannot stand next to director $2$, and director $4$ cannot stand next to directors $3$ and $2$.

# Example 3

`stdin`
```
4
0
1 0
0 2 1
```

`stdout`
```
3 0 1 2
```

## Explanation

The third example respects the condition of test group 3. In this example, the only pairs of directors that cannot stand next to each other are $(1, 3)$ and $(0, 2)$. Therefore, there are no conflicts if they are arranged in the order `3 0 1 2`. Another possible answer is `0 1 2 3`.