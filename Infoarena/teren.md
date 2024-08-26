## Task

Zaharel wants to build a vacation house somewhere in the mountains. First, he needs to choose the place where he will build his house. He owns a rectangular plot of land that is $N$ meters long and $M$ meters wide. For each piece of $1×1$ meter of land, it is known whether it is good or not for construction. The house that Zaharel wants to build will be rectangular and will have its sides parallel to the sides of the land plot. Zaharel does not want to have too many broken pieces of land, and he also wants the house to be as large as possible. Therefore, he needs to determine a rectangular portion of land of maximum area that does not contain more than $X$ broken pieces of $1×1$ meters.

## Input data

The input file `teren.in` will contain on the first line the natural numbers $N$, $M$, $X$. The next $N$ lines will contain $M$ values separated by spaces, describing the state of each $1×1$ piece of land. A value of $0$ means that construction is possible on that piece, while a value of $1$ means that construction is not possible on that piece.

## Output data

The output file `teren.out` will contain a single natural number representing the maximum possible area of the house.

## Constraints and clarifications

$1 \leq N$

$M \leq 300$

$0 \leq X \leq N \times M$

## Example

`teren.in`

```
3 5 1
0 0 0 0 1
0 1 0 0 0
0 0 0 1 0
```

`teren.out`

```
9
```

## Explanation

The bolded area represents one possible solution:

```
0 0 0 0 1
0 1 0 0 0
0 0 0 1 0
```