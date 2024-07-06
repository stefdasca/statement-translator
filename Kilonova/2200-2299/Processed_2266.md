In a country seeking its path to prosperity and civilization, there are $N$ cities, numbered from $1$ to $N$, interconnected by $N - 1$ bidirectional highways. Between any two cities, there is at most one highway. Each highway connects two distinct cities. It is possible to travel between any two cities by using highways only.

Unfortunately, there are no highways. There is also no money for building highways. Therefore, the state's policy is to grant the highways to the $K$ "kings of asphalt". These will build highways at their expense, having the right to impose tolls on the highway, expressed in euros. Each highway thus built will replace one of the roads.

# Task

Write a program that calculates the number of ways modulo $30 \ 011$ in which the roads can be granted, such that for any vehicle traveling between any two cities of the country only on roads and highways, the total toll does not exceed $S$ euros.

# Input data

The input file `autostrazi.in` contains on the first line three integers $N$, $S$ and $K$ separated by a single space, with the meaning from the statement. On the next line, it contains $K$ natural numbers, $R_1, R_2, \ldots, R_k$, not necessarily distinct, separated by a single space, representing the tolls imposed by the kings of asphalt. On the next $N - 1$ lines, there are two distinct natural numbers $x$ and $y$ separated by a single space representing a road that connects city $x$ to city $y$.

# Output data

The output file `autostrazi.out` must contain a single natural number $M$, representing the number of possibilities modulo $30 \ 011$ in which the highway network can be built, such that the sum of the tolls paid during a journey between any two cities does not exceed $S$ euros.

# Constraints and clarifications

* $1 \leq x, y \leq N \leq 100$
* $1 \leq K \leq 20$
* $1 \leq S \leq 100$
* $1 \leq R_1, R_2, \dots , R_k \leq 100$
* The i-th king of asphalt imposes the same toll $R_i$ for each highway built by him and can build zero, one or at most $N - 1$ highways.
* A road is granted entirely to a single contractor or may not be granted at all. In this case, there is no toll.
* It is allowed that no road is granted.

# Example

`autostrazi.in`
```
4 2 2
2 1
1 2
2 3
4 2
```

`autostrazi.out`
```
11
```

## Explanation

The tolls: $2$ and $1$. The roads: $(2 \ 1), (2 \ 3), (2 \ 4)$
Toll variants: $(0 \ 0 \ 0), (1 \ 0 \ 0), (0 \ 1 \ 0), (0 \ 0 \ 1), (1 \ 1 \ 0), (0 \ 1 \ 1), (1 \ 0 \ 1), (1 \ 1 \ 1), (2 \ 0 \ 0), (0 \ 2 \ 0), (0 \ 0 \ 2)$