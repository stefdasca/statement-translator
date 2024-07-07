
$N$ friends, numbered from $1$ to $N$, are drinking non-alcoholic beer at a round table.

For each friend $i$, the cost of their favorite beer $C_i$ is known. From time to time, a friend $k$ buys a beer for a sequence of friends sitting in consecutive positions at the table, including himself, in a clockwise direction.

He is willing to spend $x$ money and wants to treat the maximum possible number of friends.

# Task

Determine the number of beers each friend $k$ will buy within the budget $x$ that he has. If $x$ is greater than the cost of beers for all friends at the table, a maximum of $N$ beers will be purchased.

# Input data

The first line of the input file `br.in` contains two natural numbers $N$ and $T$ separated by a space representing the number of friends and respectively the number of friends who want to treat their friends.

The second line of the input file contains $N$ natural numbers $C_1, C_2, \ldots C_N$, separated by a space, representing the costs of the favorite beers of each friend. The beer for friend $i$ has the cost $C_i$.

Each of the following $T$ lines contains two numbers separated by a space:

* $k_1 \ x_1$
* $k_2 \ x_2$
* $\dots$
* $k_T \ x_T$

indicating the index of a friend who treats and respectively the amount of money he has.

# Output data

The output file `br.out` will contain $T$ lines, each with a single number $D_i$ representing the number of beers friend $k_i$ will buy with the amount of money $x_i$ under the conditions of the problem.

# Constraints and clarifications

* $1 \leq N \leq 15\ 000$
* $1 \leq T \leq 10\ 000$
* $1 \leq C_i \leq 100$
* $1 \leq k_i \leq N$
* $1 \leq x_i \leq 3\ 000\ 000$
* A correct program that fits within the time limit for $T \leq 4\ 000$ will score at least $30$ points
* A correct program that fits within the time limit for $N \leq 2\ 000$ will score at least $60$ points
* The friends drink only their favorite beer

# Example

`br.in`
```
5 4
10 5 15 22 13
1 32
4 50
1 9
4 200
```

`br.out`
```
3
4
0
5
```

# Explanation

Friend $1$ buys a beer for himself and for friends $2, 3$. The cost of the $3$ beers is $30$.

Friend $4$ buys $4$ beers: one for himself and for friends $5, 1, 2$. The cost of the $4$ beers is $50$.

With $9$ money, friend $1$ cannot even buy his own beer.

Friend $4$ buys $5$ beers. The cost of the $5$ beers is below the cost limit $200$.
```
