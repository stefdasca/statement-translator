Zzid

Given a perfectly rectangular wall with height $H$ and width $W$, made of bricks with height $1$ and variable width, glued together.

## Task

Cut this wall vertically in such a way that the number of bricks that need to be cut is minimized. If there are multiple such places where the wall can be cut, we want the difference in widths of the two resulting pieces to be as small as possible.

## Input data

The input file `zzid.in` contains on the first line the numbers $H$ and $W$. Each of the following $H$ lines will describe a row of the wall in the following manner: a number $N_i$, representing the number of bricks in row $i$, followed by $N_i$ numbers representing the width of the bricks in row $i$ in the order in which they appear. The sum of the widths of the bricks in each row is equal to $W$. All numbers in the input file are natural numbers.

## Output data

The output file `zzid.out` contains a single line with two natural numbers separated by a space: the minimum number of bricks that need to be cut in order to cut the wall into two pieces, and the minimum difference between the widths of the two resulting pieces of the wall.

## Constraints and clarifications

$2 \leq W \leq 10^9$

$2 \leq H \leq 10^5$

Maximum number of bricks is $10^6$

For $30\%$ of the tests, $H$ and $W \leq 1000$

For another $20 \%$ of the tests, $H \leq 1000$

The wall cannot be rotated

## Example

`zzid.in`

```
3 10
1 10
2 5 5
3 2 3 5
```

`zzid.out`

```
1 0
```

## Explanation

The wall can be cut exactly in the middle, and only the brick in the first row needs to be cut.