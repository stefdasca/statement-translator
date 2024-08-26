## Task

Businessman Gigi needs to reach city $J$ to finalize an important contract. Before reaching city $J$ to finish the contract, he needs to pass through city $I$, where he has other important business to attend to. Since he has a very tight schedule, Gigi wants to complete his entire journey in the shortest possible time. Therefore, he would like to know the minimum length of a route that starts from the city he is initially in (numbered $1$), passes through city $I$, and ends in city $J$, how many such distinct routes (with minimal travel time) exist, and a few of these routes.

## Input data

In the `path2.in` file, the first line contains 4 integers: $N$ $M$ $I$ $J$, representing the number of cities in the country where businessman Gigi is located, the number of bidirectional direct connections between cities, the number of the city where Gigi first needs to arrive, and the number of the city where Gigi will finish his journey. Each of the following $M$ lines contains a pair of cities between which there is a direct connection.

## Output data

On the first line of the `path2.out` file, you will print $T$, representing the minimum duration (in hours) of a route that passes through city $I$ and ends in city $J$. On the second line, you will print the number of distinct ways to reach city $J$ in time $T$ (passing through city $I$). On the following lines, you will print all distinct routes (of minimum length) to reach city $J$, passing through city $I$. If the number of such routes exceeds $100$, then you will print only $100$ of them (any $100$). A route will be printed as a sequence of cities through which Gigi passes: starting city ($1$), the next city, $\dots$, $I$, $\dots$, $J$, separated by spaces. Between any two consecutive cities, there must be a direct connection. Each route will be printed on a single line.

## Constraints and clarifications

$3 \leq N \leq 100$

$1 < I$

$I,J \leq N$

$I \neq J$

$2 \leq M$

$M \leq \frac{N*(N-1)}{2}$

The time required to travel a direct connection between $2$ cities is $1$ hour.

Therefore, a minimum-length route from city $1$ to city $J$, also passing through city $I$, is represented by a sequence of $T+1$ cities (where $T$ is the minimum time that must be calculated).

The number of distinct minimum-length routes will be at least $1$ and at most $2\ 000\ 000\ 000$.

Gigi is allowed to pass through city $J$ before reaching city $I$, but he cannot finalize the contract in city $J$ until he has passed through city $I$ (this means that the last city in his route must be city $J$).

## Example

`path2.in`

`7 8 7 4 1 2 1 3 2 4 3 4 4 5 4 6 5 7 6 7`

`path2.out`

`6`

`8`

`1 2 4 5 7 5 4`

`1 2 4 5 7 6 4`

`1 2 4 6 7 5 4`

`1 2 4 6 7 6 4`

`1 3 4 5 7 5 4`

`1 3 4 5 7 6 4`

`1 3 4 6 7 5 4`

`1 3 4 6 7 6 4