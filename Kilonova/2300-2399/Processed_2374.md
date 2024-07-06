Upon a sequence composed only of the digits $1, 2$ and $3$, a transformation $T$ is applied by simultaneously performing the following three operations:
1. A maximal sequence of $n$ consecutive $1$s is transformed into $n1$.
   For example:
   * $1$ is transformed into $11$
   * $11$ is transformed into $21$
   * $111$ is transformed into $31$
2. A maximal sequence of $n$ consecutive $2$s is transformed into $n2$.
   For example:
   * $2$ is transformed into $12$
   * $22$ is transformed into $22$
   * $222$ is transformed into $32$
3. A $3$ is transformed into $13$.
   For example:
   * $3$ is transformed into $13$
   * $33$ is transformed into $13 \\ 134$
   * $333$ is transformed into $1 \\ 313 \\ 134$

For example:
$T(3 \\ 113) = 132 \\ 113$
$T(3) = 13$
$T(1 \\ 331) = 11 \\ 131 \\ 311$

Let's consider the sequence $S$ defined recursively as follows: $S_1 = 3$ and $S_k = T(S_{k-1}), k > 1$.

# Task
Given $N$ a natural number, determine the length of the sequence $S_N$. Because the length can be very large, the result must be displayed modulo $37 \ 781$.

# Input data
The input file `sir.in` contains on the first line the natural number $N$.

# Output data
The output file `sir.out` will contain a single line where you will write the length of $S_N$ modulo $37 \ 781$.

# Constraints and clarifications
* $S_i$ will be composed only of $1, 2$ and $3$ for any $i > 0$.
* $1 \leq N < 260$

# Example 1

`sir.in`
```
1
```

`sir.out`
```
1
```

# Example 2

`sir.in`
```
6
```

`sir.out`
```
10
```

# Example 3

`sir.in`
```
71
```

`sir.out`
```
13391
```

## Explanation

The first terms of the sequence $S$ are: $3$, $13$, $1 \\ 113$, $3 \\ 113$, $132 \\ 113$, $1 \\ 113 \\ 122 \\ 113$, $311 \\ 311 \\ 222 \\ 113$, etc.
