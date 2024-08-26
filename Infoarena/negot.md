# Negot

Radusqrt, the sultan of the distant land of iGorj, conducted a thorough analysis of the economic situation in his realm. Following this analysis, he noticed that some silk producers started monopolizing the entire market. Consequently, Radusqrt implemented a strict rule that no producer can do business with more than $K$ shops. Moreover, no shop is allowed to do business with more than one producer. In the land, there are $N$ producers and $M$ shops. Each producer $i$ has a good business relationship with $T_i$ shops. The esteemed Radusqrt wishes for the economy to be as prosperous as possible, so he will personally decide which shops each producer will do business with. Our sultan will choose optimally, so that the sum of the number of shops each producer does business with is as large as possible, thus ensuring the greatest possible number of subjects contribute to the smooth running of the economy. Help Radusqrt determine this sum!

## Input data

The input file `negot.in` will contain on the first line 3 numbers $N$, $M$, and $K$ (the number of producers, the number of shops, and the maximum number of shops a producer can do business with); each of the following $N$ lines will contain a number $T_i$ (representing the number of shops producer $i$ has good relations with) and $T_i$ numbers, each representing the order number of the shop.

## Output data

The output file `negot.out` will contain a single number $S$ on the first line representing the sum mentioned in the statement.

## Constraints and clarifications

$1 \leq N \leq 1000$

$1 \leq M \leq 40000$

$1 \leq K \leq 30$

For 10 points $1 \leq N, M \leq 5 ; K=2$

For another 10 points $1 \leq N, M \leq 10 ; K=3$

For another 20 points $1 \leq N, M \leq 1000 ; K=1$

For another 30 points $1 \leq N, M \leq 1000 ; 1 \leq K \leq 15$

It is guaranteed that a producer has good relations with at most 200 shops!

## Example

`negot.in`

```
3 5 2
2 1 5
3 1 2 3
1 5
```
`negot.out`

```
4
```

## Explanation

The division will be as follows: producer1 will supply shops 1 and 5, producer2 will supply shops 2 and 3, and producer3 will stay home and not supply any shop.