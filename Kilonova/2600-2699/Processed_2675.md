
# Task

You are given an array $a$ of $n$ numbers $a_1,a_2,\ldots,a_n$.

Find the *minimum lexicographic* sequence $b_1,b_2,\ldots,b_n$ that satisfies the following conditions:
- The array $b$ can be obtained by rearranging the elements of $a$.
- $b_i \neq b_{i+1}$ for any $i$, $1 \leq i < n$.

If there is no array $b$ that satisfies these properties, print `-1`.

$^1$ The sequence $x_1,x_2,\ldots,x_n$ is smaller lexicographically than the sequence $y_1,y_2,\ldots,y_n$ if there is a position $p$ ($1 \leq p \leq n$) such that:
- $x_i=y_i$, for any $1 \leq i < p$.
- $x_p < y_p$.

# Input data

The first line of the input file `permus.in` contains $n$ - the length of the array $a$.

The second line contains $n$ numbers $a_1,a_2,\ldots,a_n$ - the elements of the array $a$.

# Output data

If there is an array $b$ that satisfies the conditions from the statement, print the elements of the array $b$. Otherwise, print `-1`.

# Constraints and clarifications
- $1 \leq n \leq 2 \cdot 10^5$
- $1 \leq a_i \leq n$

|#|Points|Constraints                                                             |
|-|-------|-----------------------------------------------------------------------|
|1| 10    | There is a maximum of two distinct elements in the array $a$            |
|2| 15    | All elements in the array $a$ have a frequency less than or equal to $2$ |
|4| 45    | $n \leq 2000$                                                          |
|5| 30    | No additional constraints                                              |

# Example 1

`permus.in`

```
7
3 2 1 1 3 3 2
```

`permus.out`
```
1 2 3 1 3 2 3
```

## Explanation 

$[1,2,3,1,3,2,3]$ is the minimum lexicographic sequence that meets the conditions from the statement.

# Example 2

`permus.in`

```
4
1 2 1 1
```

`permus.out`
```
-1
```

## Explanation 

It can be demonstrated that there is no array $b$ that meets the conditions from the statement.
