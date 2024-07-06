```markdown
# Task

You are given an array $v$ of $n$ elements.
You are required to perform $q$ operations, where operation $i$ represents the reversal of the subarray $[l_i, r_i]$.
# Input data

The first line contains two integers $n$ and $q$, representing the length of the array $v$ and the number of operations, respectively.
The second line contains $n$ numbers, representing the elements of the array $v$.
Each of the following $q$ lines will contain 2 integers $l_i$ and $r_i$, representing the indices of the subarray that will be reversed in operation $i$.

# Output data

A single line should contain the elements of the array $v$ after applying the $q$ operations in the order they were read.

# Constraints and clarifications

* $1 \leq n \leq 300\ 000$
* $1 \leq q \leq 200\ 000$
* $1 \leq v_i \leq 10^9$
* $1 \leq l_i \leq r_i \leq n$
* It is recommended to use the following line of code at the beginning of the `main` function to reduce the input reading time: `cin.tie(0)->sync_with_stdio(0);`.

|#|Points|Constraints|
|-|-|-|
|0|0|Examples|
|1|20|$1 \leq n, q \leq 5\ 000$|
|2|20|$1 \leq n, q \leq 100\ 000$|
|3|60|Without additional constraints|

# Example 1

`stdin`
```
7 2
1 5 2 1 2 4 7
3 4
4 7
```

`stdout`
```
1 5 1 7 4 2 2 
```

## Explanation

The array $v$ is initially $[1, 5, 2, 1, 2, 4, 7]$.
After the first operation, the array $v$ becomes $[1, 5, \textbf{1, 2}, 2, 4, 7]$.
After the second operation, the array $v$ becomes $[1, 5, 1, \textbf{7, 4, 2, 2}]$.

# Example 2

`stdin`
```
8 5
5 2 7 3 1 6 8 4
1 4
2 7
5 8 
1 8
2 3
```

`stdout`
```
5 7 2 4 1 6 8 3 
```
```