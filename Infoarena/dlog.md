Dlog

This problem is sponsored by IXIA A prime natural number $P$ is given. We define $Z_P$ as the set of all possible remainders modulo $P$, i.e., $\{0, 1, 2, \dots P - 1\}$. All operations on numbers in $Z_P$ are performed modulo $P$. For example, in $Z_5$, $3 * 3 = 4$ $(9 \mod 5)$. We say that a natural number $G$, from the set $\{1, 2, \dots P - 1\}$, is a generator of $Z_P$ with multiplication if, by raising it to certain powers, we can obtain all the numbers from $Z_P \setminus \{0\}$. For example, $2$ is a generator of $Z_5$, because: $2^1 = 2$, $2^2 = 4$, $2^3 = 3$, $2^4 = 1$ (all operations are performed modulo $5$). On the other hand, $2$ is not a generator of $Z_7$, because the number $5$ cannot be obtained by the described operation. Given a prime number $P$, a number $G$, a generator of $Z_P$, and a number $Y$ belonging to the set $\{1, 2, 3, \dots P - 1\}$, find the minimum $X$ such that $G^X = Y$ $(\mod P)$.

## Task

The input file `dlog.in` will contain on the first line $T$, the number of queries in the input file. Each of the following $T$ lines will contain a query in the format $P, G, Y$, with the above meaning.

## Input data

The file `dlog.in` will contain the number of queries $T$ on the first line. Each of the next $T$ lines will contain one query in the format $P, G, Y`, with the above meaning.

## Output data

The file `dlog.out` will contain the answers to the $T$ queries, on separate lines.

## Constraints

$1 \leq T \leq 1000$

$2 \leq P \leq 2\ 000\ 000$

$1 \leq G, Y < P$

For each of the $T$ tests, the answer must be in the range $[0 .. P - 1]$

## Example

`dlog.in`

```
3
3 2 1
5 3 2
7 3 4
```

`dlog.out`

```
0
3
4
```

## Explanation

$2^0 \mod 3 = 1 \mod 3 = 1$

$3^3 \mod 5 = 27 \mod 5 = 2$

$3^4 \mod 7 = 81 \mod 7 = 4$