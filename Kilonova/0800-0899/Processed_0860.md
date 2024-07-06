﻿Considering a sequence of binary values, we name a *dominant subarray* a set of elements located at consecutive positions in the sequence that has the property that the number of values equal to $1$ is strictly greater than the number of values of $0$. For example, in the sequence $1,0,0,0,1,1,0,1,1,1,0,0$ a dominant subarray is $0,1,1$ and another one, of greater length, is $0,1,1,0,1,1,1$. The maximal dominant subarray is the dominant subarray of maximum length. In the example sequence, the maximal dominant subarray is $1,0,0,0,1,1,0,1,1,1,0$ (i.e., the entire string, except the last zero).

# Task

Given a sequence of binary values, determine the length of a maximal dominant subarray as well as the number of such subarrays.

# Input data

The input file `dominant.in` contains on the first line a natural number $V$, and on the second line the sequence of binary values, without spaces.

# Output data

The output file `dominant.out` will contain:

* Option $1$: if $V = 1$, then the first line of the output file will contain a single natural number representing the length of a maximal dominant subarray.
* Option $2$: if $V = 2$, then the first line of the output file will contain a single natural number representing the number of maximal dominant subarrays.

# Constraints and clarifications

* $V \in \{1,2\}$
* The length of the sequence of binary values is at most $300\ 000$.
* For all tests, the binary sequence will contain at least one value of $1$.
* For $55\%$ of the score, $V = 1$.

# Example 1

`dominant.in`
```
1
100011011100
```

`dominant.out`
```
11
```

## Explanation

The maximal dominant subarray is $10001101110$ and has the length of $11$.

# Example 2

`dominant.in`
```
2
100011011100
```

`dominant.out`
```
1
```

## Explanation

The maximal dominant subarray is $10001101110$ and has the length of $11$. There is only one maximal dominant subarray.

# Example 3

`dominant.in`
```
1
0000110000111
```

`dominant.out`
```
9
```

## Explanation

The maximal dominant subarray has a length of $9$; it is $110000111$.

# Example 4

`dominant.in`
```
2
10000111000
```

`dominant.out`
```
3
```

## Explanation

The maximal dominant subarray has a length of $5$. There are three maximal dominant subarrays: $00111, 01110$ and $11100$.