```markdown
# Task

Given $n$ and a **binary** matrix, named $c$, with $n$ rows and $n$ columns. Determine if there exist two **binary** sequences $a$ and $b$ of length $n$ such that $a_i \cdot b_j = c_{i,j}$ for every $1 \leq i, j \leq n$. If there do not exist two such sequences, print `1`.

# Input data

The input file `inmultire.in` contains the number $n$ on the first line. The next $n$ lines contain $n$ elements, representing the matrix $c$.

# Output data

Print `-1` in the file `inmultire.out` if there is no solution, otherwise print the sequence $a$ on the first line and the sequence $b$ on the second line. If there are multiple solutions, any of them can be printed.

* $2 \leq n \leq 1 \ 000$
* $0 \leq c_{i, j} \leq 1$
 
# Constraints and clarifications

|#|Score|Constraints|
|-|-|--------|
|1|10|$n = 1$|
|1|20|$n = 2$|
|3|70|No additional constraints|

# Example 1
`inmultire.in`
```
2
0 0
1 1
```
`inmultire.out`
```
0 1
1 1
```

## Explanation

In the first example, we have $a = [0, 1]$ and $b = [1, 1]$. $c_{1, 1} = a_1 \cdot b_1 = 0$, $c_{1, 2} = a_1 \cdot b_2 = 0$, $c_{2, 1} = a_2 \cdot b_1 = 1$ and $c_{2, 2} = a_2 \cdot b_2 = 1$. So, this solution is correct.

# Example 2
`inmultire.in`
```
5
1 0 0 1 1
1 0 0 1 1
1 0 0 1 1
0 0 0 0 0
1 0 0 1 1
```
`inmultire.out`
```
1 1 1 0 1
1 0 0 1 1
```

# Example 3
`inmultire.in`
```
2
1 0 
0 1
```
`inmultire.out`
```
-1
```

## Explanation

In the third example, it can be demonstrated that there is no solution. Therefore, we print `-1`.
```