> “Be it rain or storm
> A shawarma is just great”

All of Orăștia knows that Naic has the best shawarma shop in town. With so many orders, he no longer competes with Siclam and GurgerBrill, but with KFC and McDonald's. Since the problems at today’s contest are too easy, you decided to go to your brother Naic to get a shawarma, but of course, there are 150 orders ahead of you from the firefighters and IGO. Since he doesn’t look at you angrily while you wait for your order, as those from Siclam and GurgerBrill do, he lets you play on OEIS 5 (Orăștie Entertainment Interactive System 5). Naic's favorite game on the play station 5 is the following:

You are given a tree with $N$ nodes where each edge can have a value of $0$ or $1$.

A path in the tree from one node to any other node is called $K$-alternating if at most $K$ consecutive edges have the same value.

There is a possibility to perform operations of the type “change the value of an edge from $0$ to $1$ or from $1$ to $0$”.

Find the length of the longest $K$-alternating path that can be obtained if at most $M$ edges can be changed.

# Task

Write a program that solves the game on the console since today's problems were so easy.

# Input data

The first line contains $N, K$ and $M$. The next $N − 1$ lines contain three integers $x, y$ and $c$ indicating that there is an edge between node $x$ and node $y$ with value $c$.

# Output data

The only line of the output file will print the maximum length of a $K$-alternating path.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* $2 \leq K < N$
* $0 \leq M < N$

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 7      | $1 \leq N \leq 300$ |
| 2 | 13      | $1 \leq N \leq 5\ 000$     |
| 3 | 25      | $1 \leq N \leq 70\ 000$     |
| 4 | 17      | $M = 0$     |
| 5 | 38     | No additional constraints.      |

# Example

`stdin`
```
9 2 1
1 2 0
2 3 1
3 4 1
4 5 1
1 6 1
1 7 0
7 8 0
8 9 1
```

`stdout`
```
6
```

## Explanation

If we change the edge $1-7$, we obtain the path $9-8-7-1-2-3-4$, with a length of 6 edges, on which there are at most two equal consecutive values. See the figure below.

~[arb1.png|align=center]