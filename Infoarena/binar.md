## Task

Miruna has a matrix with $N$ rows and $M$ columns which contains only elements of $1$ and $0$. She wants to sort the columns of the matrix lexicographically and is asking for your help.

## Input data

The input file `binar.in` will contain on the first line two natural numbers $N$ and $M$ representing the dimensions of the matrix. The next $N$ lines will contain $M$ characters each, not separated by space, from the set $\{0, 1\}$.

## Output data

In the output file `binar.out` you will display a permutation of numbers from $1$ to $M$, representing the lexicographical order of the columns. If multiple columns are identical, the corresponding indices will be displayed in ascending order.

## Constraints and clarifications

$1 \leq N, M \leq 2000$

Read each line as a string.

Avoid reading character by character!

## Example

`binar.in`

```
4 6
010111
010100
101111
110011
```

`binar.out`

```
3 1 5 6 2 4
```