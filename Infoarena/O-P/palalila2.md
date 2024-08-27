# Palalila2

Given a string $S$ consisting of uppercase and lowercase letters of the English alphabet. A subsequence of $S$ is a string formed by some characters (not necessarily consecutive) of it, in the order in which they appear. We call a zig-zag subsequence $S'$ = $(s_1, s_2, \dots, s_n)$ of $S$ one for which $s_1 < s_2$, $s_2 > s_3$, $s_3 < s_4$, $s_4 > s_5, \dots$ where `<` and `>` are understood lexicographically (We know that '$A < B < \dots < Z < a < \dots < z$'). Determine the maximum length of a zig-zag subsequence of $S$.

## Input Data

The input file `palalila2.in` will contain a single line which will contain the string $S$.

## Output Data

The output file `palalila2.out` will print on the first line the determined length for the longest zig-zag subsequence of $S$.

## Constraints

$1 \leq\text{length of string } S \leq 500000$

For 50% of the tests

$1 \leq\text{length of string } S \leq 4000$

## Example

`palalila2.in`

`nostressATfmi`

`palalila2.out`

`7`

## Explanation

A possible zig-zag subsequence of length 7 is `osesAmi