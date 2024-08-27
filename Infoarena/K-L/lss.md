## Task

The story is long, but long story short: We are given a number $K$. Consider the following infinite array with elements: $1, 2, 3, \dots, K, 1, 2, 3, \dots, K, 1, 2, 3, \dots$ . Our task is to delete $P$ given elements. Each time we delete an element $X$ at position $Poz$, we must pay $X$ valuable units. Also, all elements after $Poz$ ($Poz + 1$, $Poz + 2$, $\dots$) will decrease by $1$. However, if their cost is already $1$, they will change to $K$. You need to find an order in which to delete the $P$ given numbers such that you consume the fewest valuable units.

## Input data

The input file `lss.in` will contain on the first line $2$ numbers $K$ and $P$. The next line will contain $P$ numbers representing the positions that need to be deleted.

## Output data

The output file `lss.out` will contain on the first line a single natural number representing the minimum number of valuable units that you can consume.

## Constraints

$1 \leq K \leq 1\,000\,000\,000$

$1 \leq P \leq 100\,000$

The given positions are natural numbers in the range $[1, 1\,000\,000\,000]$

When an element is deleted, it does not disappear from the array; its value becomes $0$ and it does not change thereafter.

## Example

`lss.in`

```
3 4
3 4 5 6
```

`lss.out`

```
6
```