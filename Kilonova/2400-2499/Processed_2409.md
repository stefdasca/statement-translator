Given an array $x_1, x_2, \dots x_k$ of natural numbers, you can apply two types of operations:

$1.$ Choose two numbers $(i, j)$ with $1 \leq i \leq j \leq k$ and set each value from $i$ to $j$ to $0$.
$2.$ Choose two numbers $(i, j)$ with $1 \leq i \leq j \leq k$ and add $1$ to each value from $i$ to $j$.

For example, if we start with the array $x = [1, 3, 0, 2, 3]$. We could, for instance, apply the following sequence of operations:

1. Apply operation $1$ for $(2, 3)$. $x = [1, 0, 0, 2, 3]$. 
2. Apply operation $2$ for $(1, 3)$. $x = [2, 1, 1, 2, 3]$.
3. Apply operation $2$ for $(4, 5)$. $x = [2, 1, 1, 3, 4]$.
4. Apply operation $1$ for $(1, 3)$. $x = [0, 0, 0, 3, 4]$. 

# Task

Given $n$ and an array $a_1, a_2, \dots a_n$ of natural numbers. Also given are $Q$ queries of the form $l, r, v$. What is the minimum number of operations needed so that $v = a_l = a_{l+1} = a_{l+2} = \dots = a_r$. **After each query, the array $a$ resets to its initial state.**

# Input data

The first line of the input file `egale.in` contains two integers, $n$ and $Q$. The second line contains the array $a_1, a_2, \dots a_n$ of natural numbers. The following $Q$ lines each contain a triplet $l, r, v$.

# Output data

For each $i$ from $1$ to $Q$, the $i$-th line of the output file `egale.out` should contain a single integer, the answer to the $i$-th query. 

# Constraints and clarifications

* $1 \leq n, Q \leq 100\ 000$
* $0 \leq a_i \leq 200$ for each $i$ from $1$ to $n$
* $1 \leq l \leq r \leq n$ and $0 \leq v \leq 200$ for every query.

|#|Points|Constraints|
|-|-|--------|
|1|10|$v = 0$ for every query and $n, Q \leq 1\ 000$|
|2|15|$v = 0$ for every query|
|3|19|$1 \leq n, Q \leq 1\ 000$|
|4|12|$a_i \leq 1$|
|5|25|$a_i \leq 10$|
|6|19|No other constraints|

# Example 1

`egale.in`
```
11 5
1 2 1 2 1 0 5 2 3 1 6
1 4 1
1 4 2
1 11 0
1 11 4
6 9 5
```

`egale.out`
```
2
2
1
5
6
```

## Explanation

For the first query, we need to find the minimum number of operations to make all elements in the array $[1, 2, 1, 2]$ equal to $1$. The only way to do this in $2$ operations is to apply operation $1$ to the entire array, then apply operation $2$ to the entire array.

# Example 2

`egale.in`
```
10 10
3 2 9 4 10 9 1 0 8 6
3 3 7
4 5 9
5 8 9
1 6 3
5 5 7
3 10 2
3 4 1
7 8 5
3 8 10
4 7 1
```
`egale.out`
```
8
10
10
4
8
3
2
5
11
2
```

# Example 3

`egale.in`
```
5 4
0 1 0 0 1 
1 1 0
1 2 0
1 3 0
3 4 0
```
`egale.out`
```
0
1
1
0
```

## Explanation

This example verifies that $v = 0$ for every query. 

For the first query, already all elements are $0$, so no operations are needed.

For the second query, we can apply operation $1$ to the interval $(1, 2)$.