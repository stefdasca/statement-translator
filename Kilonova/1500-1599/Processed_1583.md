```markdown
Consider the positive natural numbers $N$ and $D$, followed by a sequence $S$ of $N$ positive natural numbers **sorted in ascending order**, indexed from $1$ to $N$.

Determine the number of quintuplets of indices $(i_1,i_2,i_3,i_4,i_5)$ that satisfy the relations:

* $a \cdot b \cdot c = D$
* $a \cdot x^2 + b \cdot y^2 = c^2$
* $a < b < c$
* $x \neq y$

where we denote $a = S[i_1]$, $b = S[i_2]$, $c = S[i_3]$, $x = S[i_4]$, $y = S[i_5]$.

**The result will be displayed modulo $10^9 + 7$.**

# Input data

The input file `cvintete.in` contains on the first line two positive natural numbers $N$ and $D$ with the meaning given in the statement. 
The next line contains $N$ positive natural numbers sorted in ascending order. 

# Output data

The output file `cvintete.out` will contain a single natural number which represents the result of the task, modulo $10^9 + 7$.

# Constraints and clarifications

|#|Score|Constraints|
|-|-|--------|
|1|16|$1 \leq N \leq 20  \quad 1 \leq S[i] \leq 20  \quad 1 \leq D \leq 250$|
|2|12|$1 \leq N \leq 1\,000  \quad 1 \leq S[i] \leq 1\,000  \quad 1 \leq D \leq 10^{5}$|
|3|25|$1 \leq N \leq 5\,000  \quad 1 \leq D \leq 10^{7} \quad S[i] = i$, for any $1 \leq i \leq N$|
|4|28|$1 \leq N \leq 10\,000  \quad 1 \leq S[i] \leq 5\,000 \quad 1 \leq D \leq 10^{7}$|
|5|19|$1 \leq N \leq 100\,000  \quad 1 \leq S[i] \leq 20\,000  \quad 1 \leq D \leq 10^{9}$|

* For all subtasks, the relation $S[i] \leq S[i + 1]$ is satisfied, for any $1 \leq i \leq N - 1$.

# Example 1

`cvintete.in`
```
4 6
1 2 3 3
```

`cvintete.out`
```
2
```

## Explanation

For the first example, the quintuplets that satisfy the task are $(1, 2, 3, 1, 2)$ and $(1, 2, 4, 1, 2)$.

# Example 2

`cvintete.in`
```
10 60
1 2 3 4 4 5 6 8 10 12
```

`cvintete.out`
```
4
```

## Explanation

For the second example, the quintuplets that satisfy the task are $(1, 6, 10, 8, 4)$, $(1, 6, 10, 8, 5)$, $(1, 7, 9, 2, 4)$ and $(1, 7, 9, 2, 5)$.
```

I have double-checked the statement and ensured there are no grammar or syntax errors based on the rules of the English language.