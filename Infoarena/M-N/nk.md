## Task

You are given an array of $N$ distinct natural numbers and a natural number $K$. Determine how many of the $N$ numbers can be written as the product of exactly $K$ distinct numbers from the array.

## Input data

The input file `nk.in` contains the number of tests $T$ on the first line, on the second line two natural numbers $N$ and $K$, and on the third line $N$ numbers representing the numbers in the array.

## Output data

The output file `nk.out` will contain a single number, representing the number of numbers that can be written as the product of exactly $K$ distinct numbers from the array of the $N$ numbers.

## Constraints

$1 \leq T \leq 10$

$1 \leq N \leq 1{,}000$

$1 \leq K \leq N$

$0 \leq X \leq 10^9$, where $X$ is an element of the array.

## Example

`nk.in`

```
2
4 2
2 3 6 18
2 2
1 2
```

`nk.out`

```
1
1
```

## Explanation

For the first example, we have: $6 = 2 \cdot 3$ and $18 = 3 \cdot 6$.

For the second example, we have: $2 = 1 \cdot 2$.