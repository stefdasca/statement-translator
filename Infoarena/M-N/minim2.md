# Minim2

Lavinia just started cycling and is determined to get into the record book, so she has chosen a route consisting of $N$ segments on which she wants to break the record. To break the record on the route, the sum of Lavinia's times on each segment must be less than the current record. Unfortunately, she is not well-prepared enough, so she seeks your help. You have the ability to multiply the length of any segment once by a number less than one $A$ and then any number of times thereafter by another number less than one $B$, $A \leq B$. What is the minimum number of adjustments that need to be made so that Lavinia breaks the record?

## Input data

The first line of the input file `minim2.in` will contain an integer $N$, representing the number of segments. The next line will contain $N$ natural numbers representing the lengths of the segments. The 3rd line will contain 3 real numbers, $A$, $B$, and the current record.

## Output data

The first line of the output file `minim2.out` will contain the minimum number of adjustments that need to be made so that Lavinia breaks the record.

## Constraints and clarifications

$1 \leq N \leq 100000$

$1 \leq D[i] \leq 1000000000$

$0 \leq A \leq B \leq 1$

For all the tests, the total number of adjustments will not exceed $500000000$.

For $40\%$ of tests, no more than $200000$ adjustments will be performed.

The record is considered broken if the absolute difference between Lavinia's time and the record is less than $10^{-6}$ or if Lavinia's time is less than the record.

No segment will be shortened more than $10{000}$ times.

## Example

`minim2.in`

```
4
5 10 100 18
0.5 0.75 52.4
```

`minim2.out`

```
4
```

## Explanation

First, act on segment $3$, $100 \cdot 0.5 = 50$.

The 2nd time, act again on segment $3$, $50 \cdot 0.75 = 37.5$, the sum being $70.5$.

The 3rd time, act again on segment $3$, $37.5 \cdot 0.75 = 28.125$.

The 4th time, act on segment $4$, $18 \cdot 0.5 = 9$.

And thus the sum is $5 + 10 + 28.125 + 9 = 52.125$.