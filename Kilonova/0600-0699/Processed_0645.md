LLM defines the operation of $reduction$ of a number $X$ as follows:

Let $X$ = $\overline{x_1 x_2 x_3 ... x_k}$.
We can choose the position of a digit, say $t$ provided $1 < t \leq k$ and eliminate it.
Thus $X$ becomes $\overline{x_1 x_2 ... x_{t-1} x_{t+1} x_{t+2} ... x_k}$.

Given the numbers $P$, $N$ and the array $a_1, a_2, ..., a_N$. LLM has two types of questions for you and asks you to provide the correct answer for both types of questions.

# Task

If $P = 1$, LLM asks you to display an array of $N$ numbers, the $i$-th number being $1$ if $a_i$ is a perfect square, $0$ otherwise.

If $P = 2$, LLM asks you to display an array of $N$ natural numbers, the $i$-th number representing the number of different ways to reduce the number $a_i$ to a perfect square.

# Input data

The first line of the input file `reducere.in` contains two natural numbers $P$ and $N$ separated by a space. The next line contains $N$ natural numbers separated by a space representing the array $a_i$.

# Output data

If $P = 1$, the first line of the output file `reducere.out` contains the array of $N$ natural numbers separated by a space. If $P = 2$, the first line of the output file `reducere.out` contains the array of $N$ natural numbers separated by a space.

# Constraints and clarifications
* $P = 1$ or $P = 2$.
* $1 \leq N \leq 100\ 000$
* $1 \leq a_i \leq 10^9$ for any $1 \leq i \leq N$.
* Two $reduction$ operations are considered different if the position of the removed digit is different.
* For 40 points $P = 1$.
* For 20 points $P = 2$ and $a_i < 100$.

# Example 1

`reducere.in`
```
1 5
64 10 100 36 63
```
`reducere.out`
```
1 0 1 1 0
```

# Example 2

`reducere.in`
```
2 5
102 81000 99 369 2256
```
`reducere.out`
```
0 3 1 1 2
```

# Explanations

In the first example, $64 = 8^2$, $100 = 10^2$, $36 = 6^2$.

In the second example:

Numbers obtained by reducing the number $102$ are $10$ and $12$, which are not perfect squares.

The perfect squares obtained by reducing the number $81000$ are $8100$, $8100$ and $8100$.

The perfect square obtained by reducing the number $99$ is $9$.

Numbers obtained by reducing the number $369$ are $36$ and $39$, $36$ being a perfect square.

Numbers obtained by reducing the number $2256$ are $256$ and $226$, and $225$, only $226$ is not a perfect square.