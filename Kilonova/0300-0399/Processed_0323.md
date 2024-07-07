
# Task
You are given an array $v$ of $n$ integers. Display the result of the expression $ \\displaystyle \\sum_{i=1}^{n-2} \\sum_{j=i+1}^{n-1} \\sum_{k=j+1}^{n} v_i \\cdot v_j \\cdot v_k $.

# Input data
The first line contains the natural number $n$, and the second line contains the numbers in the array $v$, separated by exactly one space.

# Output data
Print the result of the expression from the task.

# Constraints and clarifications
- $3 \\leq n \\leq 100\\ 000$
- $-30 \\leq v_i \\leq 30, \\ i = \\overline{1..n}$
- Test 0 is worth 0 points and it is the example from the statement, while test 1 is worth 20 points and has $n \\leq 100$.

# Example
`stdin`
```
4
0 1 2 3
```
`stdout`
```
6
```

## Explanation
$0 \\cdot 1 \\cdot 2 + 0 \\cdot 1 \\cdot 3 + 0 \\cdot 2 \\cdot 3 + 1 \\cdot 2 \\cdot 3 = 6$
```
