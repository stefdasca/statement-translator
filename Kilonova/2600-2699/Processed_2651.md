~[fig1.png|align=right]

Fascinated by Chinese culture and the Great Wall of China, Andra decided to build her own miniature wall, with height $N$ and width $M$, using the red and yellow pieces she owns.

She has an unlimited number of pieces with a width of one unit and all possible heights. The red pieces (hóng) have an odd height $(1, 3, 5, \dots)$, while the yellow pieces (huáng) have an even height $(2, 4, 6, \dots)$. **The pieces cannot be rotated and can only be placed vertically**.

Because the yellow color is considered the most prestigious in Chinese culture, Andra wants the sum of the lengths of all yellow pieces that make up the wall to equal a number $K$, specially chosen to bring luck. Furthermore, she wonders **in how many ways** she can build the wall so that this condition is met.

Since this task “seems Chinese” to her (even though she speaks Chinese!), she decided to ask for your help, hearing that you feel lucky in the year of the dragon.

# Task

Given $N, M$, and $K$, determine the number of ways to build the wall under the given conditions.

# Input data

The single line of the input file `zid.in` contains the values $N$, $M$, and $K$, as described above.

# Output data

The single line of the output file `zid.out` will contain the number of ways to build the **wall** modulo $10^9 + 7$.

# Constraints and clarifications

* $1 \leq N, M \leq 5 \ 000$
* $0 \leq K \leq N$
* Two ways of building the wall are considered identical if they are made of the same types of pieces placed in the same way. For example, there are two ways to build a fully yellow wall of $4 \times 1$.

| # | Points | Constraints         |
|---|--------|---------------------|
| 1 | 10     | $N \leq 6$, $M = 1$ |
| 2 | 16     | $N \leq 500$, $M = 1$ |
| 3 | 5      | $N \leq 2 \ 500$, $M = 1$, $K = N$ |
| 4 | 6      | $N \leq 2 \ 500$, $M = 1$, $K = 0$|
| 5 | 14     | $N \leq 2 \ 500$, $M = 1$ |
| 6 | 4      | $N \leq 500$, $M = 2$ |
| 7 | 2      | $N \leq 500$, $M = 3$ |
| 8 | 5      | $N \leq 2 \ 500$, $M = 4$ |
| 9 | 17     | $N \leq 2 \ 500$, $M \leq 10$ |
| 10 | 14    | $N \leq 2 \ 500$, $M \leq 2 \ 500$ |
| 11 | 7     | Without additional restrictions |

# Example 1

`zid.in`
```
5 1 2
```

`zid.out`
```
6
```

## Explanation

All $6$ configurations of walls with height $5$, width $1$, and $K = 2$ possible are illustrated in the first figure.

~[fig2.png|align=center]

# Example 2

`zid.in`
```
2 2 2
```

`zid.out`
```
2
```

## Explanation

All $2$ configurations are illustrated in the second figure.

~[fog3.png|align=center]