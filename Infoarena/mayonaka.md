# Mayonaka

Eudanip has not solved his implementation problems that have been haunting him for so many years. To hide from the public shame caused by this fact, he settled in Australia, where he works at a kangaroo research center. The kangaroo specialists are trying to study how the weight of kangaroos changes over time. For this purpose, they have divided a certain path often traveled by kangaroos into $N$ cells. Each of the $N$ cells contains a scale that will sum up the mass of all the kangaroos stepping on that cell. A kangaroo can be concisely described by a tuple $x$, $y$, $jump$, $weight$. It will start its journey on cell $x$ and will step on cells $x + k * jump$ for all non-negative $k$ for which $x + k * jump \leq y$. Given $N$ and a list of $M$ kangaroos, Eudanip needs to find the sum recorded on each scale after all the journeys are completed. He knows how to do this but has decided to propose the problem to you in a contest, perhaps to earn a source of 100 points from you.

## Input data

The input file `mayonaka.in` will contain on its first line the numbers $N$ and $M$, having the meaning as described. The next $M$ lines will each contain 4 numbers $x$, $y$, $jump$, $weight$ having the meaning as described.

## Output data

The output file `mayonaka.out` will contain $N$ numbers, representing the sums recorded by each scale.

## Constraints and clarifications

$1 \leq N, M \leq 100\,000$

$1 \leq x[i] \leq y[i] \leq N$

$1 \leq jump[i] \leq N - 1$

$1 \leq weight[i] \leq 10\,000$

For tests worth 30 points, $N, M \leq 5\,000$

For tests worth 70 points, $N, M \leq 70\,000$

## Example

`mayonaka.in`
```
10 5
1 10 1 1
1 10 2 5
2 5 2 9
3 7 2 6
2 10 1 10
```

`mayonaka.out`
```
16 18 6 11 13 21 6 8 6 1
```