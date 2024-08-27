# Superstring

The shortest common supersequence of 2 strings $S_1$ and $S_2$ is a string $S$ with a minimum number of characters that contains both $S_1$ and $S_2$ as subarrays (sequences of characters in consecutive positions in $S$). For example, the shortest common supersequence of the strings "alba" and "bacau" is "albacau". Given two strings consisting of lowercase English letters, find the length of their shortest common supersequence.

## Input data

The first line of the input file `superstring.in` contains the integer $T$, representing the number of tests to follow. Each test consists of 2 lines. The first of these lines contains the string $S_1$, and the second line contains the string $S_2$.

## Output data

For each of the $T$ tests, in the order given in the input file, print one line in the output file containing the length of the shortest common supersequence.

## Constraints

$1 \leq T \leq 11$

$1 \leq$ length of any string $\leq 1\,000\,000$

## Example

`superstring.in` 
```
2
alba
bacau
resita
mures
```

`superstring.out` 
```
7
8
```