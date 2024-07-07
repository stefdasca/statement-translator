
# Task

A sequence $s_1, s_2, \ldots, s_k$ of natural numbers is called $xy$*-dominant* for given values $x$ and $y$ if:
1. There exist at least $x$ distinct numbers in the sequence $s$.
2. It is possible to choose $x$ distinct numbers from the sequence such that the sum of the frequencies of the chosen numbers is greater than or equal to $y$.

For example, for $x=2$ and $y=4$:
- The sequence $[1,2,1,2,3]$ is $xy$*-dominant* (we can choose the numbers $1$ and $2$, which appear in the sequence a total of $2+2=4$ times).
- The sequence $[1,1,1,1]$ is not $xy$*-dominant* (there are not two distinct values in the sequence).
- The sequence $[1,2,1,3]$ is not $xy$*-dominant* (there are not two distinct values in the sequence that appear a total of at least $4$ times).

Given $n, x, y$ and a sequence of natural numbers $a_1, a_2, \ldots, a_n$. 

Find the number of $xy$*-dominant* subarrays of the sequence $a$.

# Input data

The first line of the file `dominant.in` contains the numbers $n$, $x$ and $y$. 

The second line contains the sequence $a_1, a_2, \ldots, a_n$.

# Output data

The first line of the file `dominant.out` contains the number of $xy$*-dominant* subarrays of the sequence $a$.

# Constraints and clarifications

* $1 \leq n \leq 3 \cdot 10^5$
* $1 \leq x \leq $ number of distinct values in the sequence $a$
* $1 \leq y, a_i \leq n$
* To obtain points for a certain subtask, at least one submitted source will need to pass all tests from that subtask.
|#|Score|Constraints|
|-|-|--------|
|0|0|Examples|
|1|25|$1 \leq n \leq 300$|
|2|22|$1 \leq n \leq 3\ 000$|
|3|16|$y = 1$|
|4|19|$x = 1$|
|5|18|No other constraints|

# Example 1

`dominant.in`
```
4 3 1
1 2 3 4
```

`dominant.out`
```
3
```

## Explanation

The $xy$*-dominant* subarrays are $[1,2,3]$, $[2,3,4]$ and $[1,2,3,4]$.

# Example 2

`dominant.in`
```
10 2 4
1 1 1 2 1 2 2 2 1 2
```

`dominant.out`
```
28
```

## Explanation

In total, there are $28$ $xy$*-dominant* subarrays, among which are $[1,1,1,2]$, $[2,1,2,2]$ and $[1,1,1,2,1,2,2,2,1,2]$.

# Example 3
`dominant.in`
```
14 3 8
5 3 5 1 4 5 1 4 2 2 4 5 4 4
```

`dominant.out`
```
15
```

## Explanation

In total, there are $15$ $xy$*-dominant* subarrays, such as $[5,3,5,1,4,5,1,4,2,2,4]$.
