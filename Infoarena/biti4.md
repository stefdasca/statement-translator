# Biti4

Let the set of all bit strings of length $N$ with at most $K$ pairs of consecutive positions where the digits $0$ and $1$ are adjacent. We will consider canonical strings to be the strings in the set that are lexicographically smaller than their reverse.

## Task

Considering all canonical strings in lexicographic order, for given $N$, $K$, and $I$, determine the $I$-th canonical string.

## Input data

The input file `biti4.in` contains on the first line three integers $N$, $K$, and $I$ with the meaning specified in the statement.

## Output data

The output file `biti4.out` will contain on the first line a single binary string representing the requested canonical string.

## Constraints

$0 \leq K < N \leq 60$

$1 \leq I \leq 10^{18}$

A string $s = s_1 s_2 \dots s_n$ is lexicographically smaller than another string $t = t_1 t_2 \dots t_n$ if there is a position $p$ such that $s_p < t_p$ and $s_1 = t_1$, $s_2 = t_2$, $\dots$, $s_{p-1} = t_{p-1}$. There will always be a solution.

## Example

`biti4.in`
```
4 2 7
```

`biti4.out`
```
1001
```

## Explanation

The 9 canonical strings are: $0000$, $0001$, $0010$, $0011$, $0110$, $0111$, $1001$, $1011$, $1111$.