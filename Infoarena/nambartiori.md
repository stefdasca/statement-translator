# Nambartiori

K0kalaru47 realized that the only way to make a lot of money in life is to learn mathematics. After studying the secrets of mathematics thoroughly, he concluded that "Nambăr Tiori" is his favorite chapter. He likes it so much that every day he arranges his money in piles such that if he writes down the number of money in each pile, the resulting sequence would be a geometric progression of natural numbers. A geometric progression of length $k$ with ratio $r$ is a sequence of numbers $p(1), p(2), \dots, p(k)$ for which the relationship holds: $p(i) = p(1) * r^{i - 1}$, $2 \leq i \leq k$. Unfortunately, being a true k0kalar, he does not keep track of money, and after arranging them in a geometric progression he forgot their number. All he remembers about the geometric progression is that it is the $N$-th geometric progression of length $k$ with a ratio greater than $1$ and less than or equal to $2$ in lexicographic order.

## Task

Knowing that he has arranged his money in $T$ geometric progressions, help him find them.

## Input data

The input file `nambartiori.in` contains on the first line a natural number $T$, representing the number of tests. The following $T$ lines will contain two numbers $n$ and $k$, having the meaning from the statement.

## Output data

The output file `nambartiori.out` will contain $T$ lines, on each line $i$ containing the answer to question $i$.

## Constraints and clarifications

$T \leq 10$

$n \leq 1000000000$

$2 \leq k \leq 10$

### Subtasks
Subtask 1 (10 points, test 1): $k = 2$

Subtask 2 (20 points, tests 2-3): $n \leq 100$

Subtask 3 (30 points, tests 4-6): $n \leq 10000$

Subtask 4 (40 points, tests 7-10):

## Initial constraints

## Example

```nambartiori.in
10
1 4
2 4
3 4
4 4
5 4
6 4
7 4
8 4
9 4
10 4
```

```nambartiori.out
1 2 4 8
2 4 8 16
3 6 12 24
4 8 16 32
5 10 20 40
6 12 24 48
7 14 28 56
8 12 18 27
8 16 32 64
9 18 36 72
```

```nambartiori.in
5
5763 2
34568 7
9345 3
845689 6
1065354 4
```

```nambartiori.out
107 199
33922 67844 135688 271376 542752 1085504 2171008
3105 6210 12420
810280 1620560 3241120 6482240 12964480 25928960
783083 1566166 3132332 6264664
```

## Explanation

The first 10 geometric progressions of length $4$ with the given ratio are: 
```
1 2 4 8
2 4 8 16
3 6 12 24
4 8 16 32
5 10 20 40
6 12 24 48
7 14 28 56
8 12 18 27
8 16 32 64
9 18 36 72
```