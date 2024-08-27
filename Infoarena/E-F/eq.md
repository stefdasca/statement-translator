# Easy Query

Consider an array of $N$ natural numbers, $x_1$, $x_2$, $\dots$ $x_N$. The following operation is defined: for a pair $i,j$, $1 \leq i \leq j \leq N$, consider the subarray $x_i$, $x_{i+1}$, $\dots$ $x_j$ from which two arrays corresponding to the given subarray are constructed as follows:
$y_t = x_t - x_k + x_p$, $i \leq t \leq j$, $t \leq k \leq j$, $t \leq p \leq j$, where $y_t$ is maximum
$z_t = x_t - x_k + x_p$, $i \leq t \leq j$, $t \leq k \leq j$, $t \leq p \leq j$, where $z_t$ is minimum
The value $P = \max(y) + \min(z)$ is calculated, where $\max(y)$ is the maximum of the array $y$ constructed as above, and $\min(z)$ is the minimum of the array $z$.

## Task

Given the initial array, answer a set of multiple operations.

## Input data

The first line of the input file `eq.in` contains two numbers $N$ and $M$ representing the number of elements in the array $x$, and the number of operations for which the value of $P$ is to be determined, respectively.
The next line contains the elements of the array $x$ separated by a space character.
The following $M$ lines contain the subarrays defined by two integers $i$ and $j$ separated by space representing the starting position and the ending position of the subarray.

## Output data

The output file `eq.out` contains the values of $P$ for each given subarray, one per line, in the order of their appearance in the input file.

## Constraints and clarifications

$1 < N \leq 100001$

$1 < M \leq 130001$

$0 \leq x_i \leq 2^{24}$

## Example

`eq.in`
```
6 3
1 8 10 5 9 3
1 4
2 6
3 5
```

`eq.out`
```
7
16
16
```