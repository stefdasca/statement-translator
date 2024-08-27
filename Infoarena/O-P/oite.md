# Sheep

The Big Bad Wolf is organizing this year's bridge championship. The participants will be the $C$ sheep of shepherd Eduard. For the first round, the wolf needs 4 participants whose wool quantity sums up to $L$ (their wool will be used to craft a coat for the organizer).

## Task

Help the Big Bad Wolf determine how many distinct ways there are to organize the first round of the bridge championship. Two methods of organization are considered distinct if there is at least one sheep that appears in one arrangement and not in the other.

## Input data

The input file `oite.in` contains on the first line two integers $C$ and $L$. The second line contains $C$ numbers $A_i$ representing the wool quantities of each sheep.

## Output data

The output file `oite.out` contains a single line that contains the required number of possibilities.

## Constraints and clarifications

$4 \leq C \leq 1\ 024$

$0 \leq L \leq 2\ 000\ 000\ 000$

$0 \leq A_i \leq 500\ 000\ 000$

For 80% of the tests $L \leq 1\ 000\ 000$

For 50% of the tests $C \leq 550$

The 4 participants must be distinct sheep

## Example

`oite.in`

```
10 38
13 1 12 10 8 10 1 12 9 1
```

`oite.out`

```
3
```

## Explanation

The three possibilities are:

`1 2 3 8`

`1 3 7 8`

`1 3 8 10`
