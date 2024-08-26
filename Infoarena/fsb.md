## Task
You are given a sequence of $0$s and $1$s. Determine the number of subarrays that have an equal number of $0$s and $1$s.

## Input data
The input file `fsb.in` contains on the first line $N$, the length of the sequence. The second line contains a sequence of $N$ characters, representing the sequence.

## Output data
The output file `fsb.out` contains a single integer, representing the number of required subarrays.

## Constraints
$1 \leq N \leq 200\ 000$

A subarray of a sequence $a_1, a_2, \dots, a_N$ is the sequence $a_i, a_{i+1}, \dots, a_{i+k}$, with the property that $1 \leq i \leq i + k \leq N$

Two subarrays $a_i, a_{i+1}, \dots, a_{i+k}$ and $a_j, a_{j+1}, \dots, a_{j+l}$ are considered distinct if $i \neq j$ or $k \neq l$.

## Example
`fsb.in`
```
6
110001
```

`fsb.out`
```
4
```

## Explanation
The required subarrays are: $1100$, $10$, $01$, $110001$