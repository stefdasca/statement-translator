## Task

Consider the binary string $A = "011011100\dots"$, formed by concatenating the binary representations of natural numbers from $0$ to infinity. The starting position is numbered $1$. You are given a binary string $B$ of length $N$. Display the smallest position $p$ such that the string $B$ is found as a subsequence in the string $A[1..p]$. We say that the string $T$ of length $K$ is a subsequence of $S$ if all characters in the string $T$ appear in the same order in the string $S$ at not necessarily consecutive positions. More precisely, $T$ is a subsequence of $S$ if there exist indices $1 \leq i_{1} < i_{2} < \dots < i_{K} \leq |S|$ such that $T_{1} = S_{i_{1}}, T_{2} = S_{i_{2}}, \dots, T_{K} = S_{i_{K}}$.

## Input data

The input file `subbit.in` contains the binary string $B$ on the first line.

## Output data

The output file `subbit.out` must contain the required number on the first line.

## Constraints and clarifications

$1 \leq |B| \leq 5\ 000\ 000$

## Example

`subbit.in`
```
00100101
```

`subbit.out`
```
12
```

## Explanation

The first $22$ characters of the string $A$ are $"\ 0\ 11\ 0\ 1\ 1\ 1\ 00101\ 1101111000"$.