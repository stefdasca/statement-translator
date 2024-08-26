## Inv

A sequence $S$ of length $n$ with integer numbers is given. We call an inversion a pair of indices $(i, j)$ such that $1 \leq i < j \leq n$ and $S[i] > S[j]$.

## Task

Determine how many inversions are in the given sequence.

## Input data

The input file `inv.in` contains on the first line the natural number $n$.  
The next line contains $n$ integer numbers, representing the elements of the sequence $S$ in order.

## Output data

The output file `inv.out` will contain a single number, representing the remainder of the number of inversions in the sequence when divided by $9917$.

## Constraints

$2 \leq n \leq 100\,000$

## Example

`inv.in`
```
5
3 4 1 2 5
```

`inv.out`
```
4
```