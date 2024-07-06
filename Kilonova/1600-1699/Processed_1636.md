```markdown
After learning numbers at school, Maria and Mihai started playing with them. Maria chose the number $3$ and said that she likes all numbers that can be written as a sum of one or more distinct powers of $3$. For example: $1 = 3 ^ 0, 91 = 3 ^ 4 + 3 ^ 2 + 3 ^ 0, 27 = 3 ^ 3$, are numbers that Maria likes. The number $6 = 3 ^ 2 + 3 ^ 2$ is not liked by Maria ($3 ^ 2$ appears twice). Mihai, who always likes to compete with Maria, chose the number $5$ and said that he likes numbers that can be written as a sum of one or more distinct powers of $5$ (the same rule as for the numbers Maria likes, but using the number $5$). While playing on the computer, they found a file `puteri35.in` that contained a non-zero natural number $n$. Immediately, the children thought to write each of them in a file (which they agreed to name `puteri35.out`), the first $n$ numbers that they like. Here again, the discussion arose: in what order will they write them. In the end, they agreed to write all $2 \cdot n$ numbers in ascending order.

# Task

Given a non-zero natural number $n$, obtain in ascending order all $2 \cdot n$ numbers, the first $n$ numbers that Maria likes and the first $n$ numbers that Mihai likes.

# Input data

The input file `puteri35.in` contains on the first line a natural number $n$.

# Output data

The output file `puteri35.out` contains $2 \cdot n$ numbers, each on a new line, in ascending order, the first $n$ numbers that Maria likes and the first $n$ numbers that Mihai likes.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000 \ 000$

# Example

`puteri35.in`
```
3
```

`puteri35.out`
```
1
1
3
4
5
6
```

## Explanation

The solution $1 \ 3 \ 4 \ 1 \ 5 \ 6$ is not correct because the numbers are not in ascending order.
```