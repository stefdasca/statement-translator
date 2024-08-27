Paving

Gigel, the mayor in his town, decided to renovate the main street, which has dimensions $N*M$ and is composed of $1*1$ pieces. Most of the pieces are damaged, but there are $K$ pieces that are considered good. Wanting to pay as little money as possible, Gigel bought $2*2$ blocks from a merchant at the price of a $1*1$ block. To pave the street, he needs to place as many of these blocks as possible on the damaged pieces, without paving over any good pieces, as this would cause unevenness, and without overlapping the $2*2$ blocks. He realized that it would have been better to buy $1*1$ blocks, as they would cover the entire street without any hassle, but now he has no choice and needs your help!

## Task

Determine the maximum number of $2*2$ blocks that the mayor can place to repair the street.

## Input data

The first line of the file `pavare.in` will contain three integers separated by spaces: $N$, $M$, and $K$. The next $K$ lines will contain pairs of integers representing the row and column of each good piece.

## Output data

The first line of the file `pavare.out` will contain a natural number representing the maximum number of $2*2$ blocks that can be placed on the street.

## Constraints

$1 \leq N \leq 150$

$1 \leq M \leq 15$

$1 \leq K \leq N*M$

Rows are numbered from $1$ to $N$, and columns from $1$ to $M$.

## Example

`pavare.in`

```
4 6 3
1 1
2 6
3 3
```

`pavare.out`

```
4
```

## Explanation

This is a possible placement of the blocks:

~[image.png]