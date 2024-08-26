# Namlei

There are $N + 1$ cities arranged in a line, numbered in the interval $[0 \dots N]$, each having $K$ strategic objectives numbered in the interval $[0 \dots K - 1]$. Thus, any objective can be identified by a pair $(i, j)$, where $i$ represents the city number of the respective objective, and $j$ is the order number of the objective. Given these notations, edges can exist only between an objective $(i, x)$ and an objective $(i + 1, y)$ (i.e., between consecutive cities). Between two objectives $(i, x)$ and $(i + 1, y)$, there is at least one edge (possibly more). The operations that can be performed are as follows:
$U$: All edges between cities $i$ and $i + 1$ are removed. New edges are introduced to preserve the previous condition.
$Q$: The number of distinct paths consisting of exactly $j - i$ edges between objectives $(i, x)$ and $(j, y)$ is calculated and displayed.

## Input data and Output data

The first line of the file `namlei.in` contains the numbers $N$ and $K$, separated by a space. The second line of the file contains the numbers $X$ and $Y$, separated by a space. On each of the following $N$ lines, there is a triplet of numbers $(cnt, j, k)$. This triplet on the $i$-th line ($i$ between $0$ and $N - 1$) means that between cities $i$ and $i + 1$ there are (besides the $K * K$ mandatory edges) $cnt$ edges among which the first is $(i, j) - (i + 1, k)$. If the $(w - 1)$-th edge is $(i, j) - (i + 1, k)$, the $w$-th edge $(i, j') - (i + 1, k')$ is calculated using the following formula:
$$ j' = (j * X + k * w * Y) \% K $$
$$ k' = (j * w * X + k * Y) \% K $$
The $cnt$ edges are numbered $0 \dots cnt - 1$. Until the end of the file, each pair of two lines represents a $U$ or $Q$ operation. On the first of the lines is the type of operation, and on the second, the parameters determining this operation.

In the case of a $U$ operation: The second line contains the numbers $i, cnt, j, k$ separated by a space. This quadruplet means that (after removing the edges that existed already) there are between cities $i$ and $i + 1$ (besides the $K * K$ mandatory edges) $cnt$ edges among which the first is $(i, j) - (i + 1, k)$. If the $(w - 1)$-th edge is $(i, j) - (i + 1, k)$, the $w$-th edge $(i, j') - (i + 1, k')$ is calculated using the following formula:
$$ j' = (j * X + k * w * Y + 1) \% K $$
$$ k' = (j * w * X + k * Y + 1) \% K $$
The $w$ edges are numbered $0 \dots cnt - 1$. ATTENTION! Due to considerations intimately tied to the nature of the problem, these formulas differ by a $+1$ from the previous formulas.

In the case of a $Q$ operation: The second line contains the numbers $i, x, j, y$ separated by a space. In this case, the number of distinct paths of exactly $j - i$ edges between objectives $(i, x)$ and $(j, y)$ must be displayed. $i$ is strictly less than $j$. All results will be displayed modulo $997$. The answers will be displayed in the file `namlei.out` in the order the questions are asked, each answer on a separate line.

## Constraints and clarifications

$$ 1 \leq N \leq 30000 $$
$$ 3 \leq K \leq 8 $$
$$ 1 \leq cnt \leq 120 $$
There are at most 1000 operations of each type.
$X$ and $Y$ are strictly positive natural numbers representable as 32-bit variables.

## Example

`namlei.in`
```
4 3
17 19
3 1 0
3 2 2
4 0 2
4 2 2
Q 1 2 3 0
U 1 4 1 0
Q 0 2 3 0
```

`namlei.out`
```
21
4
```