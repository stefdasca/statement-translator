## Task

The following operations are given: 
1. Create a $1 \times 1$ square
2. Extend an already existing square by one unit. 

For example, if we apply the extension operation on a square of dimensions $A \times A$, after applying, the square will have dimensions $(A + 1) \times (A + 1)$.

Given $N$ and $M$, natural numbers, display the minimum number of operations to construct a rectangle of dimensions $N \times M$.

## Input data

The input file `dreptunghi.in` contains two natural numbers $N$ and $M$, having the meaning described above.

## Output data

The output file `dreptunghi.out` contains on a single line the minimum number of operations to construct a rectangle of dimensions $N \times M$.

## Constraints

$1 \leq N$ \\
$1 \leq M$ \\
$M \leq 10^9$

## Example

`dreptunghi.in`

```
7 4
```

`dreptunghi.out`

```
10
```

## Explanation

1. Create a $1 \times 1$ square. Extend the square to dimensions $4 \times 4$. So far, we have $4$ operations.
2. Create a $1 \times 1$ square to the right of the already created one. Extend the square to dimensions $3 \times 3$. In total, we have $7$ operations.
3. Create $3$ squares of dimensions $1 \times 1$ above the last created $3 \times 3$ square. In total, we have $10$ operations.