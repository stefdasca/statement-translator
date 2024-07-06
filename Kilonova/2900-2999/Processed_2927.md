```markdown
A prefix of a natural number $N$ is a number obtained by removing digits from the right end of $N$. For example, the prefixes of $123321$ are $123321$, $12332$, $1233$, $123$, $12$, $1$.

Similarly, a suffix of a natural number $N$ is a number obtained by removing digits from the left end of $N$. For example, the prefixes of $1023$ are $1023$, $023$, $23$, $3$.

# Task

Given $C$ and $N$.

If $C = 1$, find the sum of the prefixes of $N$.

If $C = 2$, find the sum of the suffixes of $N$.

# Input data

The first line of the input file `sterge.in` contains the numbers $C$, $N$ in this order.

# Output data

Print to the file `sterge.out` a number representing the answer to the task $C$.

# Constraints and clarifications

* $C = 1$ or $C = 2$
* $2 \leq N \leq 10^{17}$

|#|Points|Constraints|
|-|-|-----------|
|1|20|$C = 1$, $N$ has exactly two digits|
|2|30|$C = 1$, $N$ has more than two digits|
|3|20|$C = 2$, $N$ has exactly two digits|
|4|30|$C = 2$, $N$ has more than two digits|

# Example 1

`sterge.in`
```
1
123321
```
`sterge.out`
```
137022
```

## Explanation

In the first example, the sum of the prefixes of $N$ is $123321 + 12332 + 1233 + 123 + 12 + 1 = 137022$.

# Example 2

`sterge.in`
```
2
1023
```
`sterge.out`
```
1072
```

## Explanation

In the second example, the sum of the suffixes of $N$ is $1023 + 023 + 23 + 3 = 1072$.
```