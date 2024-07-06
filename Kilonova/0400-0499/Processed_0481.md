```markdown
# Task

You are given an array $a_1, a_2, \dots, a_n$.

You will receive $q$ queries of the type $x, y$. For each query, you need to display $\\sum_{i=x,i-=y}^{i \\ge 1} a_i$. More precisely, display $a_x + a_{x-y} + a_{x-2y} + \dots + a_{x-ky}$ with $k$ maximum such that $x-ky \ge 1$ for each query.

# Input data

The input contains $n$ followed, on the second line, by the $n$ values of the array. The third line contains $q$ and the following $q$ lines contain 2 numbers $x$ and $y$ with the meaning from the statement.

# Output data

The output will contain $q$ lines. On the $i$th line, print the answer for the $i$th query, in the order they were read.

# Constraints and clarifications

- $1 \le n, q \le 10^5$;
- $1 \le x, y \le n$, for each $q$;
- $-10^9 \le a_i \le 10^9$;
- For 20 points, $1 \le n, q \le 10^3$;
- For another 20 points, $1 \le y \le 10$, for each $q$.

# Example

`stdin`
```
8
3 2 -1 4 8 1 6 6
4
3 2
8 3
4 3
6 1
```

`stdout`
```
2
16
7
17
```

## Explanation

For the first query, it requires $a_3 + a_1$.
For the second query, it requires $a_8 + a_5 + a_2$.
For the third query, it requires $a_4 + a_1$.
For the fourth query, it requires $a_6 + a_5 + a_4 + a_3 + a_2 + a_1$.
```