## Ejoc

Dalila and Denisa are extremely bored, so they decide to play the following game. They start with a set containing two numbers. In each turn, one of them chooses two different numbers from the set whose absolute difference is not already in the set and inserts that absolute difference back into the set. Dalila and Denisa take turns alternately. The girl who can no longer make a move loses. Write a program to determine which girl wins, given that both play optimally. Dalila makes the first move.

## Task

The input file `ejoc.in` will contain on the first line the number $T$ of games to be played. Each of the following $T$ lines contains two numbers $A$ and $B$, the two numbers initially in the set.

## Input data

The output file `ejoc.out` will contain $T$ lines. The $i$-th line will contain the name of the girl who wins the $i$-th game: "Dalila" or "Denisa" (without quotes).

## Constraints and clarifications

$1 \leq T \leq 30$

$1 \leq A, B \leq 10^{18}$

For tests worth 20 points:

$1 \leq A, B \leq 10^{2}$

$A$ is different from $B$

## Example

```
ejoc.in
2
1 2
2 3
```

```
ejoc.out
Denisa
Dalila
```

## Explanation

In the first game, Dalila cannot make any move, so she loses. In the second game, Dalila inserts $1$ into the set ($|2 - 3| = 1$), and then Denisa can no longer make any move, so she loses.