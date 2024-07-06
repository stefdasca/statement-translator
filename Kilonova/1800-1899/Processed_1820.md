It is considered two natural numbers $K$ and $N$.

# Task

Determine the number $T$ of tuples formed of $K$ natural numbers $(X_1, X_2, X_3, \dots, X_K)$ with the properties:
* $1 \leq X_1 \leq X_2 \leq X_3 \leq \dots \leq X_K \leq N$
* the greatest common divisor of the numbers $X_1, X_2, X_3, \dots , X_K$ is $1$.

# Input data

The input file `tupleco.in` contains the first line to contain the natural numbers $K$ and $N$, separated by a space.

# Output data

The output file `tupleco.out` will contain the first line to contain the remainder of the division of number $T$ by $3\ 000\ 017$.

# Constraints and clarifications

* $2 \leq K \leq 10\ 000\ 000$.
* $1 \leq N \leq 10\ 000\ 000$.
* For tests worth $32$ points, $N \leq 1\ 000$

|#|Points|Constraints|
|-|-|--------|
|1|11|$K = 2$|
|2|44|$3 \leq K \leq 1\ 000$|
|3|30|$1\ 001 \leq K \leq 1\ 000\ 000$|
|4|15|$1\ 000\ 001 \leq K \leq 10\ 000\ 000$|

# Example 1

`tupleco.in`
```
2 6
```

`tupleco.out`
```
12
```

## Explanation

For the first example, we have $K = 2$ and $N = 6$.

There are 12 pairs of natural numbers that respect the conditions from the task: $(1,1)$,  $(1,2)$,  $(1,3)$, $(1,4)$, $(1,5)$, $(1,6)$, $(2,3)$, $(2,5)$, $(3,4)$, $(3,5)$, $(4,5)$ and  $(5,6)$.

# Example 2

`tupleco.in`
```
4 3
```

`tupleco.out`
```
13
```

## Explanation

For the second example, we have $K = 4$ and $N = 3$.

There are $13$ tuples formed of $4$ natural numbers each that respect the conditions from the task: $(1,1,1,1)$, $(1,1,1,2)$, $(1,1,1,3)$, $(1,1,2,2)$, $(1,1,2,3)$, $(1,1,3,3)$, $(1,2,2,2)$, $(1,2,2,3)$, $(1,2,3,3)$, $(1,3,3,3)$, $(2,2,2,3)$, $(2,2,3,3)$ and $(2,3,3,3)$.

# Example 3

`tupleco.in`
```
2022 2023
```

`tupleco.out`
```
981889
```

## Explanation

For the third example, we have $K = 2022$ and $N = 2023$.

The remainder of dividing the number $T$ by $3\ 000\ 017$ is $981\ 889$.