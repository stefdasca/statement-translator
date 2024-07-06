In the land of the Lord, there are $N + 1$ cities. These were built in a straight line, starting from the one where the Lord's house is located. Between any $2$ consecutive cities, there is a road constructed. For each road, its length, expressed in meters, and the speed at which it can be travelled, expressed in meters per second, are known.

# Task

The Lord needs to travel from city $0$ to city $N$.
He knows that he can improve a road by increasing its speed from $V$ meters per second to $V + 1$ meters per second, at a cost of $1$ dollar. He can improve a road multiple times.
The Lord has a budget of $X$ dollars and would like to use it to reduce the time it takes to travel from city $0$ to city $N$.

# Input data

The input file `orase.in` contains the following structure:

* The first line contains the number $T$, representing the type of constraints that the test adheres to.
* The second line contains $2$ natural numbers $N$ and $X$.
* The third line contains $N$ natural numbers, the $i$-th number representing the distance between cities $i-1$ and $i$.
* The fourth line contains $N$ natural numbers, the $i$-th number representing the speed between cities $i-1$ and $i$.

# Output data

The output file `orase.out` will contain on the first line a natural number $R$ that represents the integer part of the minimum travel time from city $0$ to city $N$.

# Constraints and clarifications

* $1 \leq N \leq 5 \cdot 10^4$
* $1 \leq X \leq 10^7$
* The length of the road between any $2$ cities is a natural number in the interval $[1, 10^4]$
* The initial speed between any $2$ consecutive cities is a natural number in the interval $[1, 10^4]$

# Example 1

`orase.in`
```
1
3 5
5 3 7
2 1 4
```

`orase.out`
```
3
```

## Explanation

The minimum time is $3.65$, and the result is $\left\lfloor{3.65}\right\rfloor=3$.
The final speeds will be $4$, $3$, $5$.
$5 / 4 + 3 / 3 + 7 / 5 = 3.65$

# Example 2

`orase.in`
```
1
4 6
3 8 10 5
4 3 7 3
```

`orase.out`
```
4
```

## Explanation

The minimum time is $4.321$, and the result is $\left\lfloor{4.321}\right\rfloor=4$.
The final speeds will be $4$, $7$, $7$, $5$.
$3 / 4 + 8 / 7 + 10 / 7 + 5 / 5 = 4.32142857$

# Example 3
`orase.in`
```
1
5 6
2 5 3 2 4
5 1 2 1 3
```

`orase.out`
```
4
```

## Explanation

The minimum time is $4.65$, and the result is $\left\lfloor{4.65}\right\rfloor=4$.
The final speeds will be $5$, $4$, $3$, $3$, $3$.
$2 / 5 + 5 / 4 + 3 / 3 + 2 / 3 + 4 / 3 = 4.65$