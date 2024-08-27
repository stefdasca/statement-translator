## Football

In American football, a team can score points through the following methods:
Field Goal - $3$ points
TouchDown - $6$ points
Safety - $2$ points
Try for Extra - $1$ point
Given the score obtained by a team, calculate in how many ways the respective score could have been achieved.

## Input data

The input file `football.in` contains on the first line a natural number $T$.

It is followed by $T$ lines, each containing a natural number $S$, representing the scores for which the answer must be provided.

## Output data

The output file `football.out` contains $T$ lines. Line $i$ will contain "Case $i$: $result$" (without quotes) where $result$ will be an integer representing the answer for the $i$-th value from the input file.

## Constraints

$1 \leq T \leq 50$

$1 \leq S \leq 25$

## Example

`football.in`
```
1
4
```
`football.out`
```
Case 1: 7
```

## Explanation

$4 = 1 + 1 + 1 + 1$

$4 = 1 + 1 + 2$

$4 = 1 + 2 + 1$

$4 = 2 + 1 + 1$

$4 = 1 + 3$

$4 = 3 + 1$

$4 = 2 + 2$