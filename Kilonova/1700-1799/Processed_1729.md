
_sumk_ is a game of insight, with $N$ stages numbered from $1$ to $N$. A game is successfully completed if the player has gone through all the $N$ stages of the game in order, from $1$ to $N$, and has obtained exactly $K$ points in each stage. Each stage has $N$ levels, also numbered from $1$ to $N$. The player can earn $0$, $1$, $\\dots$, $K$ points on any level of the current stage.

If the player is at stage $i$ on level $j$ and the total number of points obtained so far at this stage is less than $K$, he will necessarily move to level $j + 1$ of stage $i$. If the player receives at least one point on level $j$ and thus his score at stage $i$ becomes **exactly** $K$, then the player **automatically moves** to level $j$ of stage $i + 1$ or successfully completes the game if $i = N$.

# Task

Knowing the number $N$ of the game's stages and the number $K$ of points that must be obtained at each stage, determine the number of possibilities modulo $578 \\ 537$ for the game to be successfully completed.

# Input data

The input file `sumk.in` contains on the first line two natural numbers $N$, $K$ as described above.

# Output data

The first line of the file `sumk.out` will contain a single natural number $P$ representing the total number of possibilities modulo $578 \\ 537$ for the game to be successfully completed.

# Constraints and clarifications

* $1 \\leq K \\leq N \\leq 500$
* Let $x$ be the final score in any given stage. Then if $x \\neq K$, the game ends in failure.
* For $20\\%$ of the tests, $K \\leq N \\leq 10$, and for $30\\%$ of the tests, $K \\leq N \\leq 100$

# Example 1

`sumk.in`
```
2 2
```

`sumk.out`
```
5
```

## Explanation

~[sumk.png]

There are $N = 2$ stages, with $N = 2$ levels each. The sum is $K = 2$ on each stage. The levels are represented by the columns of the matrices. There are $5$ possibilities for the game to end successfully.

# Example 2

`sumk.in`
```
3 2
```

`sumk.out`
```
28
```

## Explanation

~[sumk2.png]

There are $N = 3$ stages, with $N = 3$ levels each. The sum is $K = 2$ on each stage. Only a few of the $28$ possibilities are represented.
