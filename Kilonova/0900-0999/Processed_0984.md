In the ancient city of Ica, it is said that there was a palace with wealth beyond imagination. Inside, there is a corridor with $N$ boxes of candies from all corners of the world. Travelers passing through can take as many candies as they want, provided they pay for them in gold by weight.

The boxes of candies are numbered from $0$ to $N - 1$, from left to right. In box $i$, there are $a_i$ pieces of candy left, where $a_i$ is a non-negative integer.

As the guardian of the palace, you want to rearrange the boxes so that the boxes with many candies are closer to the entrance.

You are given the array $a_0, a_1, \ldots, a_{N - 1}$, as well as the numbers $F$ and $T$. In a single operation, you are allowed to swap two **adjacent** elements among $a_0, a_1, \ldots, a_{N - 1}$. What is the minimum number of operations required for the sum of the first $F$ elements of the array to be at least $T$?

# Input data

The first line contains three integers, $N$, $F$, and $T$.

The second line contains $N$ integers, $a_0, a_1, \ldots, a_{N - 1}$.

# Output data

If it is impossible to achieve your goal using the described operation, print `NO`.

Otherwise, print a single integer, the minimum number of operations required.

# Constraints and clarifications

* $1 \leq N \leq 100$
* $1 \leq F \leq N$
* $0 \leq T \leq 10^{11}$
* $0 \leq a_i \leq 10^9$ for $i = 0, 1, ..., N - 1$.

**Note:** The numbers in the input may not fit in a $32$-bit data type, so be careful if you use `C++`.

Your solution will be tested on multiple test groups, each group having a number of points associated with it. Each group of tests may contain multiple tests. To obtain the score of a test group, the solution must pass all tests in the respective group.

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 6       | $N \leq 2$ and $a_i \leq 100$ for $i = 0, 1, \ldots, N - 1$ and $T \leq 10^9$|
| 2 | 19      | $a_i \leq 1$ for $i = 0, 1, \ldots, N - 1$      |
| 3 | 16      | $N \leq 20$    |
| 4 | 30      | $a_i \leq 100$ for $i = 0, 1, \ldots, N - 1$    |
| 5 | 29      | No additional constraints.      |

# Example 1

`stdin`
```
6 2 27
10 4 20 6 3 3
```

`stdout`
```
1
```

## Explanation

In the first example test, the first two elements must sum at least $27$. This can be achieved with a single swap of two adjacent elements: $4$ and $20$. After this swap, the array becomes `10 20 4 6 3 3`, and indeed the first two elements sum $10 + 20 = 30 \geq 27$.

# Example 2

`stdin`
```
6 5 5000000000
1000000000 1000000000 0 1000000000 1000000000 1000000000
```

`stdout`
```
3
```

## Explanation

In the second example test, the element $0$ must be moved to the end of the array; this requires three swaps.

# Example 3

`stdin`
```
3 2 100
20 30 60
```

`stdout`
```
NO
```

## Explanation

In the third example test, it is impossible to make the first two elements sum at least $100$; the best result we can obtain is $60 + 30 = 90$.

# Example 4

`stdin`
```
1 1 100
100
```

`stdout`
```
0
```