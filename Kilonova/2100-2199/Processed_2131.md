> "If you think it’s simple, then you have misunderstood the problem" (Bjarne Stroustrup)

Jeffrey wants to expand his online store also in Romania. To ensure the obsession for customer satisfaction, he sets up an efficient, automatic delivery strategy to complete orders as quickly as possible.

Romania consists of $N$ cities connected to each other, with a unique route existing between any two cities. A route is a sequence of roads that connect two cities, so that no road is repeated. In total, there are $N - 1$ bidirectional roads connecting the cities.

Each road has an associated cost. Jeffrey's team has created a list of $M$ pairs of cities between which there will be very frequent deliveries. We define the cost of a pair of cities $(x, y)$ as the sum of the costs of the roads in the route from city $x$ to city $y$. We also define the **total cost** as the sum of all the costs of the given $M$ pairs of cities.

Jeffrey can apply the following type of operation: select a road with a strictly positive cost and **decrease its cost by $1$**. For reasons of "frugality", this operation can be applied at most $K$ times, where $K$ is a natural number.

# Task

Find the minimum total cost that can be obtained after applying the above operation at most $K$ times.

# Input data

The first line of the input file contains a natural number $N$, representing the number of cities.

The following $N - 1$ lines each contain $3$ numbers $x$, $y$ and $w$, representing that there is a bidirectional road between cities $x$ and $y$, with a cost equal to $w$. The cities are numbered from $0$ to $N - 1$.

The next line contains the numbers $M$ and $K$, representing the number of pairs of cities, respectively the number of operations that can be applied, followed by $M$ lines each containing two numbers $x$ and $y$ representing the $M$ pairs of cities.

# Output data

The first line of the output file will contain a single number, representing the minimum total cost that can be obtained, **modulo $666 \ 013$**.

# Constraints and clarifications

* $1 \leq N \leq 200 \ 000$
* $0 \leq K \leq 200 \ 000$
* $1 \leq M \leq N$
* $1 \leq w \leq 20$
* $0 \leq x, y < N$, $x \neq y$
* The operation of decreasing the cost of a road **can be applied multiple times for the same road**, as long as the cost of the road does not become a negative number.
* For tests worth $20$ points, it is guaranteed that $1 \leq N,K \leq 1 \ 000$.
* For other tests worth $30$ points, it is guaranteed that $K = 0$.
* For the remaining tests worth $50$ points, there are no additional constraints.

# Example

`amazon.in`
```
5
1 0 4
0 2 3
1 3 4
1 4 4
3 5
2 4
1 4
3 4
```

`amazon.out`
```
10
```

## Explanation

We can choose to apply the operation of decreasing the cost of the road from city $1$ to city $4$ by $4$ times. Thus, the cost of the road will become $0$.

We can also apply the operation once more for the road from city $1$ to $3$, reducing its cost to $3$. The cost of the route between cities $2$ and $4$ will be the sum of the costs of the roads $2 \rightarrow 0$, $0 \rightarrow 1$ and $1 \rightarrow 4$, i.e., $3 + 4 + 0 = 7$. The cost of the route between cities $1$ and $4$ will be the cost of the road $1 \rightarrow 4$, i.e., $0$. The cost of the route between cities $3$ and $4$ will be the sum of the costs of the roads $3 \rightarrow 1$ and $1 \rightarrow 4$, i.e., $3 + 0 = 3$.

Thus, the total cost is $7 + 0 + 3 = 10$.