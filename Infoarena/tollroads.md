TollRoads

$N$ cities are connected by $M$ bidirectional highways, each highway $(a, b)$ having an attached toll cost $c$. A revision of the toll system is desired, but there are several aspects that need to be considered and investigated, since some of the $N$ cities are major commercial or tourist centers.

## Task

The goal is to find the answers to a series of $Q$ questions of the form: $(X, T)$ - how many of the other $N-1$ cities have access to city $X$, with a total toll cost of at most $T$ to each city?

## Input data

The input file `tollroads.in` contains the numbers $N$, $M$, and $Q$ on the first line, representing the number of cities, the number of highways, and the number of queries. Each of the next $M$ lines contains three numbers $a$, $b$, $c$, separated by spaces, representing two cities connected by a highway and the cost of the highway. The next $Q$ lines each contain two numbers $X$ and $T$, separated by space, representing the query data, according to the statement.

## Output data

The output file `tollroads.out` will contain, on each of the first $Q$ lines, a single number representing the answers to the queries, in the order they were asked.

## Constraints and clarifications

$1 \leq N \leq 10^5$ 

$1 \leq M \leq 10^5$

$1 \leq a, b \leq N$

$1 \leq c \leq 10^5$

$1 \leq T \leq 10^5$

$1 \leq Q \leq 10^2$

between any two cities, there can be more than one highway

## Example

`tollroads.in`
```
7 8 5
1 2 1
2 3 2
2 4 4
3 5 1
4 5 1
5 6 2
1 6 5
6 7 1
1 6
1 5
1 4
2 3
4 4
```

`tollroads.out`
```
6
5
2
4
6
```

## Explanation

Cities 2,3,4,5,6,7 have access to city 1 with a maximum toll of 6

Cities 2,3,4,5,6 have access to city 1 with a maximum toll of 5

Cities 2,3,5 have access to city 1 with a maximum toll of 4

Cities 1,3,5 have access to city 2 with a maximum toll of 3

Cities 2,3,5,6,7 have access to city 4 with a maximum toll of 4