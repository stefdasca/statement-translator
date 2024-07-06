
*The Year 1905*

A South American country has proposed major investments in railway infrastructure. The Brazilian Badinho is the manager of a railway transport company on an important line. Along the line, there are $N$ stations, numbered from $1$ to $N$. Each station corresponds to a number $X_i$ which represents the number of kilometers from the start of the line to station $i$ ($X_1 = 0$). For simplicity, Badinho represents the line as a straight line, and the stations as points on that line, with station $i$ being at coordinate $X_i$.

A route represents a subset of at least 2 stations among the $N$, meaning that stops will be made at these stations. Any route operated by Badinho has 2 stations called endpoints, defined as the closest station, included in the route, to the start of the line, and the furthest station, included in the route, to the start of the line.

Badinho's company will receive a subsidy for opening a new route, which will be proportional to the length of the open route. More precisely, Badinho will receive $C$ reals (the national currency of Brazil) for each kilometer of the new route. The length of the route is defined as the distance between the endpoints.

Badinho can open two types of routes:
* Regio — stops are made at all stations between the two endpoints
* Express — some stations between the two endpoints may be traversed without stopping at them

To open a route, Badinho must build a depot at each endpoint of the respective route. The cost to build a depot at station $i$ is $D_i$ reals.

Knowing that Badinho must spend the entire amount he would receive from a subsidy, determine:
1. The number of ways to open a Regio route, $ \text{modulo }10^9 + 7$
2. The number of ways to open an Express route, $ \text{modulo }10^9 + 7$

# Input data
The file `transport.in` contains:
* The first line contains the task type $T$, which can have the value $1$ or $2$.
* The second line contains $N$ and $C$, separated by a space, representing the number of stations, and the amount received per kilometer as a subsidy.
* On the next $N$ lines, on line $i + 2$, there is a pair $X_i$ and $D_i$, separated by a space, representing the distance to station $i$ from the start of the line, and the cost to build a depot at station $i$.

# Output data
The file `transport.out` will contain:
* If $T = 1$, the number of ways to open a Regio route, $ \text{modulo }10^9 + 7$
* If $T = 2$, the number of ways to open an Express route, $ \text{modulo }10^9 + 7$

# Constraints and clarifications
* Two routes are considered distinct if they differ by at least one station.
* $2 \\leq N \\leq 200\ 000$, $1 \\leq C \\leq 10^9$
* $0 \\leq X_i, D_i \\leq 10^9 \ \forall \ 1 \\leq i \\leq N$
* $X_1 = 0$
* The sequence $X$ is strictly increasing: $X_i < X_j \ \forall \ 1 \\leq i < j \\leq N$
* All railway lines of the railway are already built, the only costs Badinho will incur are those of building depots.

## Subtask 1 (12 points)
* $T = 1$, $N \leq 1\ 000$
## Subtask 2 (26 points)
* $T = 1$, $N \leq 200\ 000$
## Subtask 3 (6 points)
* $T = 2$, $N \leq 15$
## Subtask 4 (15 points)
* $T = 2$, $N \leq 1\ 000$
## Subtask 5 (41 points)
* $T = 2$, $N \leq 200\ 000$

# Example 1
`transport.in`
```
1
5 1
0 2
1 1
3 10
4 15
6 4
```
`transport.out`
```
2
```
## Explanation
The possible routes under task 1 conditions are: $ \{1,2,3,4,5\}$, $ \{2,3,4,5\}$.
The route $ \{1,2,3,4,5\}$ includes stops at stations $1$, $2$, $3$, $4$, $5$. Stations $1$ and $5$ are the 2 endpoints. The amount received from the subsidy is: $1 \cdot (6-0) = 6$ reals ($6-0$ represents the distance between stations $1$ and $5$), and the cost of building the 2 depots is: $2+4 = 6$ reals.

# Example 2
`transport.in`
```
2
5 1
0 2
1 1
3 10
4 15
6 4
```
`transport.out`
```
12
```

# Explanation
The possible routes under task 2 conditions are: $ \{1,5\}$, $ \{1,2,5\}$, $ \{1,3,5\}$, $ \{1,4,5\}$, $ \{1,2,3,5\}$, $ \{1,2,4,5\}$, $ \{1,3,4,5\}$, $ \{1,2,3,4,5\}$, $ \{2,5\}$, $ \{2,3,5\}$, $ \{2,4,5\}$, $ \{2,3,4,5\}$.
The route $ \{1,2,5\}$ includes stops at stations $1$, $2$, $5$. Stations $1$ and $5$ are the 2 endpoints. The amount received from the subsidy is: $1 \cdot (6-0) = 6$ reals, and the cost of building the 2 depots is: $2+4 = 6$ reals.