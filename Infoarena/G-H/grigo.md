# Grigo

Grigo, a famous mioritic character, recently studied the theory of permutations in college. A permutation is a sequence of $N$ natural numbers from $1$ to $N$ such that each number appears exactly once in the sequence. For a permutation $P$ with $N$ elements, we say that position $i$ is visible if and only if $i=1$ or $P_j < P_i$ for any $j < i$. Buru provides Grigo with a list of $M$ distinct natural numbers $i_1, i_2 \dots i_M$, and Grigo needs to find the number of distinct permutations with $N$ elements such that only the positions $i_1, i_2 \dots i_M$ are visible. Help Grigo find the remainder of this number when divided by $1 000 003$.

## Input data

The input file `grigo.in` will contain on the first line the numbers $N$ and $M$, separated by a single space, with the significance described in the statement. The second line will contain $M$ distinct natural numbers $i_1, i_2 \dots i_M$, which represent the positions that need to be visible.

## Output data

The output file `grigo.out` will contain a single natural number representing the answer sought by Grigo.

## Constraints and clarifications

$1 \leq M \leq N \leq 100 \000$

$1 \leq i_j \leq N$, for any $j$ between $1$ and $M$

## Example

`grigo.in`
```
4 2
1 2
```

`grigo.out`
```
6
```

## Explanation

The $6$ valid permutations are:
```
1 4 2 3
1 4 3 2
2 4 1 3
2 4 3 1
3 4 1 2
3 4 2 1
```
The permutation `1 2 3 4` is not valid because positions 3 and 4 are also visible.