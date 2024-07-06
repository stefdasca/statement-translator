```markdown
# Task

Maximilian learned dynamic programming at school and set himself the noble goal of joining the National Informatics Team and, if possible, even the elite team.

Not long ago he learned the algorithm that calculates, for a sequence with $n$ elements, a strictly decreasing subsequence of maximum length.

Since this is an easy problem, he modified the problem statement, and now he doesn't know how to solve it. The problem reads as follows: knowing that the $n$ elements of the sequence can have values from the set $\\{x, x + 1, \\dots , y\\}$, determine the number of distinct sequences that admit a maximum number of strictly decreasing subsequences of maximum length.

Knowing the values $n$, $x$ and $y$ with the meanings as described above, help Maximilian calculate the number of distinct sequences modulo $1 \ 114 \ 111$ that contain a maximum number of strictly decreasing subsequences of maximum length.

# Input data

The input file `maxmaxmax.in` contains on the first line the $3$ natural numbers $n$, $x$ and $y$ separated by space.

# Output data

The output file `maxmaxmax.out` will contain on the first line a single natural number that represents the number of distinct sequences modulo $1 \ 114 \ 111$.

# Constraints and clarifications

* $1 \leq n, x, y \leq 10^9$;

# Example 1

`maxmaxmax.in`
```
4 3 5
```

`maxmaxmax.out`
```
20
```

## Explanation

There are $5$ sequences with a maximum of $4$ solutions, that admit a strictly decreasing subsequence of maximum length $2$: 

$(4 \ 4 \ 3 \ 3) \ (4 \ 5 \ 3 \ 3) \ (5 \ 5 \ 3 \ 3) \ (5 \ 5 \ 3 \ 4) \ (5 \ 5 \ 4 \ 4)$

There are another $15$ sequences with a maximum of $4$ solutions, that admit a strictly decreasing subsequence of maximum length $1$: 

$(3 \ 3 \ 3 \ 3) \ (3 \ 3 \ 3 \ 4) \ (3 \ 3 \ 3 \ 5) \ (3 \ 3 \ 4 \ 4) \ (3 \ 3 \ 4 \ 5) \ (3 \ 3 \ 5 \ 5) \ (3 \ 4 \ 4 \ 4) \ (3 \ 4 \ 4 \ 5) \ (3 \ 4 \ 5 \ 5) \ (3 \ 5 \ 5 \ 5) \ (4 \ 4 \ 4 \ 4) \ (4 \ 4 \ 4 \ 5) \ (4 \ 4 \ 5 \ 5) \ (4 \ 5 \ 5 \ 5) \ (5 \ 5 \ 5 \ 5)$

In total $15 + 5 = 20$ solutions. All other sequences allow a smaller number of solutions of maximum length.
```