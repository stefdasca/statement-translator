```markdown
# Statement
T. Zahlentheoretische, **Mr. T**, being a "netetist"$^1$, is short and to the point, thus asking you to solve the following problem.

# Task
Three numbers $n, m, p$ and an array $v$ with $n$ elements are given, where $0 \leq v_i \leq p$. **Mr. T** asks you to process $q$ operations of the form:
`1 k`: Count how many arrays $w$ of $n$ elements, where $0 \leq w_i \leq p$, are *strictly* lexicographically smaller than $v$ and have the sum of elements $s$, where $s \equiv k$ (mod m). Since the number of such arrays is very large, compute it modulo $998244353$.
`2 x y`: **Even worse! Mr. T** will change the value of the element $v_x$ to $y$.

# Input data
The input file `domnult.in` contains on the first line three natural numbers $n, m, p$. The second line contains $n$ natural numbers, $v_1, v_2, ..., v_n$, representing the elements of array $v$. The third line contains a natural number $q$ representing the number of operations. The next $q$ lines contain the description for each operation.

# Output data
The output file `domnult.out` contains a line with the answers for each type $1$ operation.

# Constraints and clarifications
* $1 \leq n \leq 10^5$
* $1 \leq m \leq 32$
* $1 \leq p \leq 10^9$
* $1 \leq q \leq 10^4$
* A "netetist"$^1$ is a person who works at the company *Do Not Disturb Time*.
* For tests worth $20p$, only one type $1$ operation is processed.

# Example
`domnult.in`
```
3 3 9
1 0 9
3
1 2
2 1 0
1 0
```

`domnult.out`
```
36
3
```
```