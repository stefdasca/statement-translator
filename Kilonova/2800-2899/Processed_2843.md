
> Write an essay of at least 400 words, in which you present the particularities of a dramatic text belonging to Tanaka or Constantin.

~[fig1.png|align=right]

Miclovan has an array of $N$ permutations $X^1, \\dots , X^N$ of numbers from $1$ to $M$. In other words, each $X^i$ is an array $X^i_1 , \\dots , X^i_M$ of length $M$ that contains all the numbers from $1$ to $M$ exactly once. Miclovan wants to permute the array of permutations $X^1 , \\dots , X^N$ so that the array of permutations $Y^1, \\dots , Y^N$ thus obtained is _single-crossing_. Formally, Miclovan wants to find a permutation $P_1, \\dots , P_N$ of the numbers from $1$ to $N$ so that if $Y^i = X^{P_i}$ then $Y^1 , \\dots , Y^N$ is single-crossing.

An array of permutations $Y^1 , \\dots , Y^N$ is _single-crossing_ if and only if however we choose $1 \\leq i < j < k \\leq N$ and two values $1 \\leq a, b \\leq M$ such that $a$ appears before $b$ in both $Y^i$ and $Y^k$, we have that $a$ appears before $b$ in $Y^j$ too. Formally, $a$ appears before $b$ in a permutation $Z$ if, noting with $i, j$ the positions in $Z$ for which $Z_i = a, Z_j = b$, we have that $i < j$.

Intuitively, an array of permutations $Y^1 , \\dots , Y^N$ is single-crossing if and only if for any two elements $a, b$, the relative order of $a$ and $b$ changes at most once as we proceed in order through $Y^1, Y^2, \\dots , Y^N$. In Figure $1$ this is visually observed by the fact that any two of the four colored "trajectories" (red, green, blue, grey) intersect at most once.

# Task

Solve $T$ tests. For each test, given $N , M$ and the permutations $X^1, \\dots , X^N$ of the numbers from $1$ to $M$, determine if there is at least one permutation $P$ of the numbers from $1$ to $N$ with the previously described property. If affirmative, find such a permutation $P$.

# Input data

The first line of the input contains $T$, representing the number of tests, followed by the descriptions of $T$ tests.

Each test is described as follows: the first line contains $N$ and $M$, and the next $N$ lines contain $M$ numbers representing the permutations $X^1 , \\dots , X^N$. On the $i$th of these lines are the numbers $X^i_1 , \\dots , X^i_M$, separated by spaces.

# Output data

The output will contain $T$ lines, representing the answers for the $T$ tests, in the order of input. The answer for a test is either $–1$, if no permutation $P$ of the described type exists, or a permutation $P$ in the form of $N$ numbers between $1$ and $N$ separated by spaces.

# Constraints and clarifications

* $1 \\leq T \\leq 5$
* $1 \\leq N \\cdot M \\leq 1 \\ 000 \\ 000$
* To make reading and displaying faster, we recommend using the line: `ios_base::sync_with_stdio(false); cin.tie(nullptr);`

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 11      | $N \\cdot M \\leq 2 \\ 000$ and $1 \\leq N \\leq 20$ |
| 2 | 17      | $N \\cdot M \\leq 4 \\ 000$     |
| 3 | 22      | $N \\cdot M \\leq 100 \\ 000$ and $1 \\leq N \\leq 300$     |
| 4 | 16      | $N \\cdot M \\leq 100 \\ 000$ and $1 \\leq M \\leq 300$     |
| 5 | 15      | $N \\leq 2 \\ 000$     |
| 6 | 19     | No further constraints.      |

**Attention!** In case for all the tests where a permutation $P$ exists you answer correctly and for some (or all) tests where there is no such answer, you display a valid permutation (an array of length $N$ in which each number from $1$ to $N$ appears exactly once) instead of $–1$, you will get $70\\%$ of the points.

# Examples

`stdin`
```
2
5 4
2 3 1 4
2 1 3 4
1 2 3 4
4 3 2 1
3 2 4 1
4 4
1 2 3 4
1 2 4 3
2 1 3 4
2 1 4 3
```

`stdout`
```
3 2 1 5 4
-1
```

## Explanation

$T = 2$ tests are solved.

The first test has $N = 5$ and $M = 4$. In this case, a possible solution is given by $P = [3, 2, 1, 5, 4]$, illustrated in Figure $1$. The solution is valid because the four colored 'trajectories' (red, green, blue, grey) intersect pairwise at most once.

The second test has $N = M = 4$, and no permutation $P$ satisfies the required conditions.

The answer:
* $3 \\ 2 \\ 1 \\  5 \\  4$
* $1 \\ 2 \\ 3 \\ 4$
would have received $70\\%$ of the points.

The answer:
* $-1$
* $-1$
would have received $0$ points.
