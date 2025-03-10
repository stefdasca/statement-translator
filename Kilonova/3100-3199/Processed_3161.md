Marcel has recently taken up a new hobby: creating zen gardens. He quickly developed his own style, which uses $2N$ stones as garden decorations. Half of the stones are green (covered with moss) and uniquely numbered from $1$ to $N$, while the other half are gray (no moss grows on them) and are also uniquely numbered from $1$ to $N$. In order to create a garden, Marcel will take the stones and place them in a certain order in a straight line, ensuring that the distance between any two consecutive stones is exactly $1$ inch.

When it comes to judging the aesthetic aspect of a garden, all gardens are considered beautiful. However, Marcel has a superstition about his gardens: if the distance between two stones that have the same number written on them is equal to a multiple of $M$ inches, then the garden is considered $M$-**unlucky**, bringing great misfortune and causing `Code::Blocks` errors to befall the creator of that garden. Marcel will never create such a garden. Normally, the rest of the gardens are considered $M$-**lucky**.

# Task

As part of his quest to gain wisdom, Marcel has decided to create all possible $M$-**lucky** gardens. In any case, being a cautious and organized individual, Marcel wishes to know how many $M$-**lucky** gardens containing $2N$ stones exist before embarking on his mission. Two gardens $A$ and $B$ are considered different if there exists an integer $i, \\ 1 \\leq i \\leq 2N$, such that:

* the color of the $i$-th stone in garden $A$ is different from the color of the $i$-th stone in garden $B$, or
* the number written on the $i$-th stone in garden $A$ is different from the number written on the $i$-th stone in garden $B$.

# Input data

The first and only line of the input will contain two integers $N$ and $M$, meaning that Marcel will create gardens with $2N$ stones that are $M$-**lucky**.

# Output data

On a single line, print the number of $M$-**lucky** gardens containing $2N$ stones, **modulo** $10^9 + 7$.

# Constraints and clarifications

* $1 \\leq M \\leq N \\leq 2\ 000$

| # | Score | Constraints   |
| - | ------- | ------------------- |
| 1 | 9      | $1 \\leq N, M \\leq 5$|
| 2 | 12     | $1 \\leq N, M \\leq 100$|
| 3 | 13     | $1 \\leq N, M \\leq 300$|
| 4 | 18     | $1 \\leq N, M \\leq 900$|
| 5 | 48     | No additional constraints.|

# Example 1

`stdin`
```
100 23
```

`stdout`
```
171243255
```

# Example 2

`stdin`
```
1 1
```

`stdout`
```
0
```

## Explanation

In the second example, two gardens can be created. However, neither garden is $1$-**lucky**, because for both gardens the distance between stones numbered with $1$ is $1$ inch, which is a multiple of $M = 1$ inches.