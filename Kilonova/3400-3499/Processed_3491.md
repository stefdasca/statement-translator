# Task

Given $N$, $K$, and an array $a$ of $N$ integers, determine how many contiguous subarrays of $a$ (i.e., formed by consecutive elements in the array) have the property that at least $K$ of the numbers in this subarray are *special*.

We define a number as *special* if it has at least one divisor, other than $1$, which contains only odd digits. For example, $28$ is special because $28 \\ \\vdots \\ 7$, $38$ is special because $38 \\ \\vdots \\ 19$, but $16$ is not special.

# Input data

The first line contains two integers, $n$ and $k$. The next line contains $n$ integers, representing the array $a$.

# Output data

The first line will contain a single integer, representing the required number.

# Constraints and clarifications

* $1 \\leq K \\leq N \\leq 100 \\ 000$
* $1 \\leq a_i \\leq 1 \\ 000 \\ 000$ (for $i$ from $1$ to $N$)
* For $20$ points, $N \\leq 100$
* For another $20$ points, $N \\leq 3 \\ 000$

# Example

`stdin`
```
5 2
9 46 93 15 2021
```

`stdout`
```
7
```

## Explanation

The subarrays formed with at least $K = 2$ *special* numbers are:

1. $9, 46, 93$ ($9$ is special because $9 \\ \\vdots \\ 3$, and $93$ is special because $93 \\ \\vdots \\ 31$);
2. $9, 46, 93, 15$ ($9$ is special because $9 \\ \\vdots \\ 3$, and $93$ is special because $93 \\ \\vdots \\ 31$);
3. $9, 46, 93, 15, 2 \\ 021$ ($9$ is special because $9 \\ \\vdots \\ 3$, and $93$ is special because $93 \\ \\vdots \\ 31$);
4. $46, 93, 15$ ($93$ is special because $93 \\ \\vdots \\ 31$, and $15$ is special because $15 \\ \\vdots \\ 5$);
5. $46, 93, 15, 2 \\ 021$ ($93$ is special because $93 \\ \\vdots \\ 31$, and $15$ is special because $15 \\ \\vdots \\ 5$);
6. $93, 15$ ($93$ is special because $93 \\ \\vdots \\ 31$, and $15$ is special because $15 \\ \\vdots \\ 5$);
7. $93, 15, 2 \\ 021$ ($93$ is special because $93 \\ \\vdots \\ 31$, and $15$ is special because $15 \\ \\vdots \\ 5$).