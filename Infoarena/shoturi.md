## Task

Usually, if you combine two good things, you get something even better! In this problem, we will see certain things that do not follow this rule. Among the youth of today, there is a new game: they have on the table $N$ forbidden substances, numbered from $1$ to $N$, and in the middle, they have a glass with a capacity of $K$ shots, initially empty. Each substance is harmful to the body, so for each substance $i$ $(1 \leq i)$ we know the coefficient $hazard[i]$. The game proceeds as follows: the mixture in the glass initially has a potency of $1$; for each substance $i$ $(1 \leq N)$ we can choose a natural number of shots $x[i]$; if $x[i]$ is $0$, then the potency of the mixture does not change; otherwise, it multiplies by $x[i] * hazard[i]$. When the glass is filled, one of the players who is in turn drinks that mixture. To demonstrate that this game is dangerous, we want to find the sum of the potencies of all possible mixtures. In short, we want to find the sum for all possible configurations of $x$, such that $\dots$. Because the game can become very dangerous, and young computer scientists are dangerous, this sum is required modulo $269696969$.

## Input data

The input file `shoturi.in` will contain on the first line the numbers $N$ and $K$ as described in the statement. The second line will contain $N$ numbers separated by spaces representing the coefficient $hazard[i]$ of each substance.

## Output data

The output file `shoturi.out` will contain on the first line the required sum modulo $269696969$.

## Constraints

$1 \leq N, K \leq 5,000$

$1 \leq hazard[i] \leq 100,000,000$

For $10$ points, $N, K \leq 12$

For other $40$ points, $N, K \leq 300$

For other $30$ points, $N, K \leq 2,000$

## Example

`shoturi.in`
```
2 3
2 3
```

`shoturi.out`
```
39
```

`shoturi.in`
```
10 100
1 2 3 4 5 6 7 8 9 10
```

`shoturi.out`
```
261463837
```

`shoturi.in`
```
30 5000
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
```

`shoturi.out`
```
145836083
```

## Explanation

If we pour only from substance type $1$, then we will have $x = \{3, 0\}$, thus $f(\{3, 0\}) = x[1] * hazard[1] = 3 * 2 = 6$. If we pour only from substance type $2$, then we will have $x = \{0, 3\}$, thus $f(\{0, 3\}) = x[2] * hazard[2] = 3 * 3 = 9$. If we pour from both types of substances, then $x$ will have multiple solutions:

$x = \{1, 2\}$, thus $f(\{1, 2\}) = (x[1] * hazard[1]) * (x[2] * hazard[2]) = (1 * 2) * (2 * 3) = 12$.

$x = \{2, 1\}$, thus $f(\{2, 1\}) = (x[1] * hazard[1]) * (x[2] * hazard[2]) = (2 * 2) * (1 * 3) = 12$.

Thus the answer will be $f(\{0, 3\}) + f(\{3, 0\}) + f(\{1, 2\}) + f(\{2, 1\}) = 6 + 9 + 12 + 12 = 39$.

For the second and third examples, the committee could not remember how crazy the game was, but they found out the next day, so you will have to trust the external sources.

Note: the third example is spread over $3$ lines for formatting reasons.