# Ghober-distances

You are quite silly to be honest Friedrich Nietzsche After GhoberBoss authorized the ghober-contest, he presented this ghober-problem as ghober-revenge: You have a connected graph with $N$ nodes and $M$ weighted edges. The cost of a path is equal to the maximum cost of an edge on that path. We define the function $f(x, y)$ as the minimum cost of a path from $x$ to $y$. You are given $Q$ queries of the form: $K \ a$ $\ \ 1 \ a$ $\ \ 2 \ \dots \ a \ k$. For each query, the sum of $f(a_{i}, a_{j})$ for each pair $(i, j)$ where $1 \leq i < j \leq k$ is required.

## Input data

The first line of the input file `ghoberdist.in` contains the numbers $N$ and $M$. The next $M$ lines contain 3 numbers $x \ y \ z$ which means there is an edge between nodes $x$ and $y$ with cost $z$. The next line contains $Q$, and the next $Q$ lines contain the queries in the format $K \ a$ $\ \ 1 \ a$ $\ \ 2 \ \dots \ a \ k$.

## Output data

The output file `ghoberdist.out` will contain $Q$ lines, each with a number, representing the answer for each query.

## Constraints and clarifications

Let $S$ be the sum of all $K$ values from the input.
- The cost of each edge is less than or equal to $1 \ 000 \ 000$
- The answer fits in a 64-bit signed data type
- For any subtask, unless otherwise specified, $K \geq 2$, and implicitly $2 * Q \leq S$

## Scoring

## Constraints

1. $1 \leq N, M, S \leq 1 \ 000$
2. $1 \leq N \leq 100 \ 000, 1 \leq S, M \leq 200 \ 000, K = 2$
3. $1 \leq N \leq 100 \ 000, M = N-1, 1 \leq S \leq 200 \ 000, The graph is a chain$
4. $1 \leq N \leq 100 \ 000, 1 \leq S, M \leq 200 \ 000 , 1 \leq Q \leq 200$
5. $1 \leq N, S \leq 500 \ 000, 1 \leq M \leq 1 \ 000 \ 000$

## Example

`ghoberdist.in`
```
7 10 
1 4 6 
1 5 10 
1 6 10 
1 7 11 
2 5 8 
2 7 9 
3 4 5 
3 5 11 
4 7 9 
5 6 9 
3 4 2 
3 5 7 5 
3 1 4 7 
```

`ghoberdist.out`
```
53 
80 
6 
```