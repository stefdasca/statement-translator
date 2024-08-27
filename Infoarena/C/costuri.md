## Costs

We define the cost of a natural number as the product of its digits. Given a series of natural numbers, answer multiple queries in the form $P$ $C$ with the meaning: what is the $P$-th number with the cost $C$ among the given ones? Numbers with the same cost are numbered in the same order as in the initial series.

## Input data

The first line of the file `costuri.in` contains a number $N$ which represents the number of values in the given series. The second line contains the $N$ values separated by a space. The third line contains a number $Q$, which represents the number of queries. Each of the next $Q$ lines contain a pair $P$ $C$, which represents a query.

## Output data

The file `costuri.out` must contain $Q$ lines. Each line contains a number from the given series or the value $-1$ (if there are not at least $P$ numbers with the cost $C$ in the series).

## Constraints and clarifications

$1 \leq N \leq 100000$

the elements of the given series are natural numbers with at most $9$ digits

$1 \leq Q \leq 100000$

the values $P$ and $C$ are natural numbers with at most $9$ digits

the elements of the input series are not necessarily distinct and a value is counted as many times as it appears

we consider that the number $0$ has the product of its digits equal to $0$.

## Example

`costuri.in`
```
3
11 8 1
3
2 1
3 1
1 3
```

`costuri.out`
```
1
-1
-1
```

## Explanation

In the series we have numbers with the cost $1$ and with the cost $8$. The second number with the cost $1$, in the order of appearance in the series, is $1$.