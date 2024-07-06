## Graph Staircase of Order \( n \)

A **graph staircase of order \( n \)** is an undirected graph with \( 2n \) vertices, labeled from \( 1 \) to \( 2n \), and \( 3n-2 \) edges, defined as follows: \([2k - 1, 2k]\) for \( 1 \le k \le n \) and \([k, k + 2]\) for \( 1 \le k \le 2n - 2\).

# Task

Given the values \(n\) and \(b\), calculate the number of partial trees for a graph staircase of order \( n \) and display the result in base \( b \).

# Input data

The input file `grafscara.in` contains on the first line, separated by a space, the natural numbers \( n \) and \( b \) as described above.

# Output data

The output file `grafscara.out` will contain on the first line the required value.

# Constraints and clarifications

- \( 1 \le n \le 50\ 000 \)
- \( 2 \le b \le 10 \)
- It is guaranteed that the number of digits of the result does not exceed \( 100\ 000 \).

| #  | Points | Constraints |
|---|--------|--------------|
| 1  | 6      | \( 1 \le n \le 17 \), \( b = 10 \) |
| 2  | 9      | \( 1 \le n \le 17 \), \( b < 10 \) |
| 3  | 9      | \( 18 \le n \le 34 \), \( b = 10 \) |
| 4  | 11     | \( 18 \le n \le 34 \), \( b < 10 \) |
| 5  | 16     | \( 35 \le n \le 100 \), \( b = 10 \) |
| 6  | 18     | \( 35 \le n \le 100 \), \( b < 10 \) |
| 7  | 10     | \( 101 \le n \le 10\ 000 \), \( b = 10 \) |
| 8  | 13     | \( 101 \le n \le 10\ 000 \), \( b < 10 \) |
| 9  | 5      | \( 10\ 001 \le n \le 50\ 000 \), \( b = 10 \) |
| 10 | 3      | \( 10\ 001 \le n \le 50\ 000 \), \( b < 10 \) |

# Example 1
`grafscara.in`
```
3 10
```
`grafscara.out`
```
15
```
# Example 2
`grafscara.in`
```
10 2
```
`grafscara.out`
```
100100111100010100
```
# Example 3
`grafscara.in`
```
40 10
```
`grafscara.out`
```
21792711940069192045616
```
# Example 4
`grafscara.in`
```
50 8
```
`grafscara.out`
```
11164406761045535232603005157144
```

