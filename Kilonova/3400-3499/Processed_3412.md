# Task

Hero Mishu needs to recover the legendary *sword with a scope* from the Peluzasud castle to defeat the evil witch Mirinda. Peluzasud is structured on $9$ levels, each level represented by a matrix of size $N \times M$. Besides the legendary weapon, there are also $N \times M$ monsters of varying strengths, expressed as natural numbers, in the castle. The arrangement of these monsters in the castle follows $3$ rules:

1. A monster with strength $x$ will always be on the level equal to the number of digits of $x$.
2. There will not be $2$ monsters in the same cell $(i, j, k)$.
3. There will not be a monster above another monster. In other words, if the cell $(i, j, x)$ is occupied by a monster, then for any $y \neq x$, the cell $(i, j, y)$ will remain unoccupied.

Since there are $N \times M$ enemies that cannot be stacked on top of each other, it is observed that the monsters can similarly be represented in the form of an $N \times M$ matrix, where the value of the element $(i, j)$ determines both the strength of the monster and the level on which it is located.

# Task

After Mishu receives this matrix from the wise DCIT, he wants to know:

1. The sum of the strengths of the monsters on level $k$.
2. The answers to $Q$ queries of the form: â€œWhat is the sum of the strengths of the monsters on level $k$ in the submatrix with the top-left corner at $(a, b)$ and the bottom-right corner at $(c, d)$?â€.

Help Mishu save the world!

# Input data

The first line of the file `peluzasud.in` will contain a natural number $c$, representing the task that needs to be solved.

The second line will contain $2$ natural numbers, $N$ and $M$, representing the dimensions of the matrix.

On the next $N$ lines, there will be $M$ numbers, the elements of the matrix.

If $c = 1$, the last line will contain a number $k$, the level that Mishu is interested in.

If $c = 2$, on line $N + 2$ there will be a natural number $Q$, representing the number of queries for which Mishu wants answers, and on the following $Q$ lines there will be $5$ numbers each, $a, b, c, d, k$, his queries.

# Output data

If $c = 1$, the file `peluzasud.out` will contain a single number, the requested sum.

If $c = 2$, the file will contain $Q$ numbers, one on each line, representing the answers to the queries.

# Constraints and clarifications

* $1 \le N, M \leq 10^3$;
* $1 \le Q \le 2 \cdot 10^5$;
* $c \in \{1, 2\}$;
* $1 \le k \le 9$;
* The elements of the matrix will be natural numbers in the range $[1, 10^9-1]$.

| # | Score | Constraints |
|:-:|:--:|:-----------------------------:|
| 1 | 20 |            $c = 1$            |
| 2 | 20 |         $c = 2; Q = 1$        |
| 3 | 30 |     $c = 2; 1 \le N, M \leq 500$ |
| 4 | 30 | $c = 2; 1 \le N, M \leq 1 \ 000$ |

# Example 1

`peluzasud.in`
```
1
5 6
7 18 2 124 3344 48
88 19 5 7 443 25
1129 63 393 9 5684 199
37 42 9981 2 13 1001
743 1000 808 1 63 6
3
```

`peluzasud.out`
```
2710
```

## Explanation
Numbers on level $3$ (having $3$ digits) are $124, 443, 393, 199, 808, 743$.
$124 + 443 + 393 + 199 + 808 + 743 = 2710$.

# Example 2

`peluzasud.in`
```
2
5 6
7 18 2 124 3344 48
88 19 5 7 443 25
1129 63 393 9 5684 199
37 42 9981 2 13 1001
743 1000 808 1 63 6
5
2 2 5 6 3
1 1 3 4 2
5 6 5 6 1
3 4 4 6 4
2 2 4 4 1
```

`peluzasud.out`
```
1843
188
6
6685
23
```

## Explanation

For the first query, the numbers with $3$ digits in the submatrix $(2, 2)$, $(5, 6)$ are $443, 393, 199$, and $808$.
$443 + 393 + 199 + 808 = 1843$.

For the second query, the numbers with $2$ digits in the submatrix $(1, 1)$, $(3, 4)$ are $18, 88, 19$, and $63$.
$18 + 88 + 19 + 63 = 188$.