## Task

Dubota learned about Fibonacci numbers at school. These numbers are defined as follows: the first terms of the series are $0$, $F \_0 = F \_1 = 1$, and the $n$-th term, $2 \leq n$, is obtained by adding the terms $n-1$ and $n-2$ of the series $F \_n = F \_n-1 + F \_n-2$. Now Dubota is curious about the terms of the series formed by adding the last $k$ terms and having the first $k$ terms equal to $1$. $D \_0 = D \_1 = \dots = D \_k-1 = 1$, $D \_n = D \_n-1 + D \_n-2 + \dots + D \_n-k$, $k \leq n$. Given $k$, Dubota asks you to tell him the term with index $n$ of the series formed by the rule presented above.

## Input data

The input file `recurenta.in` will contain two numbers separated by space, $n$ and $k$ as described in the statement.

## Output data

The output file `recurenta.out` will contain a single number, the term with index $n$ of the series.

## Constraints and clarifications

$k \leq n \leq 10000$

$2 \leq k \leq 1000$

## Example

`recurenta.in`

```
6 3
```

`recurenta.out`

```
17
```

## Explanation

$D \_0 = D \_1 = D \_2 = 1$, $D \_3 = 3$, $D \_4 = 5$, $D \_5 = 9$, $D \_6 = 17$.