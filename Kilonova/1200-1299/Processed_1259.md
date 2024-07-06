# Task

Given a sequence of $N$ integer numbers $A_1, A_2, \ldots , A_N$. The following operation can be performed on this sequence: the sequence is divided into $3$ non-empty segments, the maximum value from each segment is calculated and then the sum of these values is computed. In other words, two indices $0 < i < j < N$ are chosen and the values are calculated as follows:

* $X = max \{ A_k | \ 1 \leq k \leq i \}$
* $Y = max \{ A_k | \ i+1 \leq k \leq j \}$
* $Z = max \{ A_k | \ j+1 \leq k \leq N \}$
* The sum $ S = X + Y + Z$

# Task

Calculate the minimum value of $S$ that can be obtained from such an operation and determine the two indices that separate the segments to obtain this value.

# Input data

The first line of the input file `secv.in` contains a natural number $N$ representing the number of elements of the input sequence, and the second line contains the integer numbers $A_1, A_2, \ldots, A_N$ separated by a space.

# Output data

The output file `secv.out` will contain:

- on the first line: the minimum value of the sum
- on the second line: two natural numbers $i, j$ separated by a space, representing the indices for which the minimum value for $S$ is obtained by applying the above-described operation

# Constraints and clarifications

* $3 \leq N \leq 30\ 000$
* $A_1, A_2, \ldots , A_N$ are integers in the interval $[-10\ 000, 10\ 000]$
* If there are multiple solutions, any of them can be displayed

# Example

`secv.in`
```
7
3 2 1 5 6 3 2
```

`secv.out`
```
10
2 3
```

# Explanation

First segment: $3\ 2$ – the maximum is $3$

Second segment: $1$ – the maximum is $1$

Third segment: $5\ 6\ 3\ 2$ – the maximum is $6$

Sum: $10$