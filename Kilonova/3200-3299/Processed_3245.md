
# Task

Two arrays, $A$ and $B$, each of length $N$, are given. The score of a subarray $1 \leq st \leq dr \leq N$ is $ \displaystyle (A_{st} + A_{st+1} + A_{st+2} + \dots + A_{dr}) - max(B_{st}, B_{st+1}, B_{st+2}, ..., B_{dr})$.

Find the maximum score of a subarray.

# Input data

The first line of the input file `2siruri.in` contains a natural number, $N$.
The second line contains $N$ natural numbers, the $i$-th of which is $A_i$.
The third line contains $N$ natural numbers, the $i$-th of which is $B_i$.

# Output data

The first line of the output file `2siruri.out` will contain a single integer, the maximum score of a subarray.

# Constraints and clarifications

* $1 \leq N \leq 500 \ 000$
* $0 \leq A_i, B_i \leq 1 \ 000 \ 000 \ 000$

|# | Score | Constraints |
| - | - | ------------|
|1|0|Examples.|
|2|10|$1 \leq N \leq 300$|
|3|20|$1 \leq N \leq 3 \ 000$|
|4|70|No additional constraints.|

# Example

`2siruri.in`
```
5
7 2 1 4 3
4 7 9 1 2
```

`2siruri.out`
```
8
```
