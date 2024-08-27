# Cans

Farfurel wants to organize a trip to the mountains. For the trip, he invites $N$ people. Knowing that conflicts will arise regarding the transportation of the cans, Farfurel wants to fairly distribute the $P$ cans purchased among the $N$ participants and at the same time obtain a maximum amount. A fair distribution means selecting a subset of cans such that the total weight can be divided equally among the $N$ participants and the weight carried by each participant is an integer.

## Input data

The first line contains $N$ and $P$, the number of people invited by Farfurel and the number of cans purchased. On the $i$-th line of the next $P$ lines, there is a natural number representing the weight of the $i$-th can.

## Output data

The first line will contain the required maximum sum. The second line will contain the number of cans needed to form this sum, and the third line will contain the cans used.

## Constraints and clarifications

$3 \leq N$

$P \leq 4\ 096$

If there are multiple solutions in terms of choosing the cans, any of them will be displayed. $40\%$ of the points of a test are awarded for correctly displaying the sum. The weight of a can will not exceed $500\ 000$.

## Example

`conserve.in`
```
6 7
178
25
123
34
56
79
100
```

`conserve.out`
```
570
6
1 3 4 5 6 7
```