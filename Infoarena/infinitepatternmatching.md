## Task

Consider the binary string $A = "11011100\ldots"$, formed by concatenating the binary representations of natural numbers from $1$ to infinity. The starting position is numbered $1$. A binary string $B$ of length $N$ is given. Display the smallest position $poz$ such that the string $B$ is found as a subsequence in the string $A[1\ldots poz]$.

## Input data

The input file `infinitepatternmatching.in` will contain the binary string $B$ on its single line.

## Output data

The output file `infinitepatternmatching.out` will contain the number $poz$.

## Constraints and clarifications

$1 \leq |B| \leq 55$

For tests worth $56$ points,

$1 \leq |B| \leq 20$

We say that the string $X$ is a subsequence of the string $Y$ if it can be obtained from $Y$ by deleting a prefix and a suffix (both possibly empty). For example, "$ABC$" is a subsequence of "$XABCTDR$", but "$ABC$" is not a subsequence of $AXBXCX$.

## Example

`infinitepatternmatching.in`
```
11
```
`infinitepatternmatching.out`
```
2
```

`infinitepatternmatching.in`
```
011011
```
`infinitepatternmatching.out`
```
42
```

## Explanation