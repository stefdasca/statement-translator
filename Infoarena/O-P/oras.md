# City

Since it is the season when the country's roads are intensively worked on, the mayor of an unspecified city has asked for your help in marking all the streets in his city with one-way directions. There are $N$ intersections in the city numbered from $1$ to $N$, and any two intersections in this city are connected by a street.

## Task

Determine a one-way direction for each street such that for any two numbers $x$ and $y$ $(1 \leq x,y \leq N)$, there exists a path that traverses at most two streets to get from intersection $x$ to intersection $y$.

## Input Data

The file `oras.in` will contain a single integer on the first line representing the value of $N$.

## Output Data

The file `oras.out` will contain exactly $N$ lines. Each line will contain exactly $N$ characters. The $j$-th character of the $i$-th line will be '$1$', if the direction of the street between $i$ and $j$ is from $i$ to $j$, otherwise this character will be '$0$'. The $i$-th character of the $i$-th line will always be '$0$'.

## Constraints and clarifications

$3 \leq N \leq 200$

If there is no solution, you will print $-1$.

If there are multiple solutions, you can print any of them.

## Example

`oras.in`

```
3
```

`oras.out`

```
010
001
100
```

## Explanation

A solution for $N=3$ is obtained by orienting the streets as follows: $1 \to 2$, $2 \to 3$, $3 \to 1$. We reach from $1$ to $2$ using street $1 \to 2$, from $1$ to $3$ by using streets $1 \to 2$, $2 \to 3$, from $2$ to $1$ by using streets $2 \to 3$, $3 \to 1$, from $2$ to $3$ by using street $2 \to 3$, from $3$ to $1$ by using street $3 \to 1$, from $3$ to $2$ by using streets $3 \to 1$, $1 \to 2$.