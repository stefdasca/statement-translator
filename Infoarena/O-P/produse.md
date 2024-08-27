## Task

Given a sequence of $N$ natural numbers, how many subsets of indices of the sequence have the property that the product of the elements at those indices is less than or equal to $D$? The empty set is not considered in calculating the answer.

## Input data

The input file `produse.in` will contain the values $N$ and $D$ on its first line. The next line will contain $N$ natural numbers, representing the values in the sequence.

## Output data

The output file `produse.out` will contain a single line which will contain the answer to the problem modulo $10^9 + 7$.

## Constraints and clarifications

$1 \leq N$, $D \leq 200\ 000$

Each number in the sequence will be less than or equal to $D$ and greater than or equal to $1$.

For tests worth 15 points $N \leq 20$

For other tests worth 30 points the $N$ numbers are generated uniformly at random from the interval $[1, D]$

## Example

`produse.in`
```
6 50
2 2 2 3 4 10
```

`produse.out`
```
39
```