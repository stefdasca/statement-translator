
# Task

You are given an array $a$ consisting of $n$ natural numbers. How many subarrays of this array are also subarrays of the Fibonacci sequence?

A subarray of an array $a_1, a_2, \ldots, a_n$ with endpoints in $a_l$ and $a_r$ ($1 \le l \le r \le n$) contains the elements $[a_l, a_{l+1}, a_{l+2}, \ldots, a_{r-1}, a_r]$.

# Input data

The input file `fibus.in` contains:
The first line contains $n$ - the length of the array $a$.

The second line contains $n$ numbers $a_1, a_2, \ldots, a_n$ - the elements of the array $a$.

# Output data

The output file `fibus.out` will contain the number of subarrays of the array $a$ that are also subarrays of the Fibonacci sequence.

# Constraints and clarifications
- $1 \le n \le 3 \cdot 10^5$
- $1 \le a_i \le 10^9$
|#|Score|Constraints                            |
|-|-------|--------------------------------------|
|1| 15    | $a_1=a_2=\ldots=a_n$                 |
|2| 30    | $n \le 100$                          |
|4| 20    | $n \le 1000$                         |
|5| 35    | No additional constraints            |

# Example 1

`fibus.in`

```
7
1 1 1 2 3 4 1
```

`fibus.out`
```
13
```

## Explanation

The $13$ subarrays that are also subarrays of the Fibonacci sequence are: $[a_1]$, $[a_2]$, $[a_3]$, $[a_4]$, $[a_5]$, $[a_7]$, $[a_1, a_2]$, $[a_2, a_3]$, $[a_3, a_4]$, $[a_4, a_5]$, $[a_2, a_3, a_4]$, $[a_3, a_4, a_5]$ and $[a_2, a_3, a_4, a_5]$.

# Example 2

`fibus.in`

```
2
1 3
```

`fibus.out`
```
2
```

## Explanation

The $2$ subarrays that are also subarrays of the Fibonacci sequence are $[a_1]$ and $[a_2]$.
