In mathematics, the factorial of a non-negative integer $K$ is denoted by $K!$ and is equal to the product of all positive integers less than or equal to $K$.

For example:
- $1! = 1$;
- $2! = 1 \cdot 2 = 2$;
- $3! = 1 \cdot 2 \cdot 3 = 6$;
- $K! = 1 \cdot 2 \cdot 3 \cdot \ldots \cdot K$.

\
Any natural number $N$ can be decomposed with the help of factorial numbers as follows:
$N = 1! f_1 + 2! f_2 + 3! f_3 + \ldots + m! f_m$,
where coefficients $f_i$, with $1 \leq i \leq m$ are natural numbers and additionally $f_m \neq 0$.

For example:
- $20 = 1! \cdot 20$;
- $20 = 1! \cdot 6 + 2! \cdot 4 + 3! \cdot 1$;
- $20 = 1! \cdot 0 + 2! \cdot 1 + 3! \cdot 3$.

Among all these possible decompositions, there is a **unique** decomposition, called the decomposition in *factorial base* which additionally respects the conditions $0 \leq f_i \leq i$, with $1 \leq i < m$ and $0 < f_m \leq m$.

For example:
- $6 = 1! \cdot 0 + 2! \cdot 0 + 3! \cdot 1$;
- $17 = 1! \cdot 1 + 2! \cdot 2 + 3! \cdot 2$;
- $119 = 1! \cdot 1 + 2! \cdot 2 + 3! \cdot 3 + 4! \cdot 4$.

# Task
Write a program that solves the following tasks:
1. Determine the decomposition in *factorial base* of a given natural number $X$.
2. Given an arbitrary decomposition of a natural number $Y$, determine its decomposition in *factorial base*.

# Input data
The input file is `bazaf.in`.

It contains on the first line a natural number $V$ which can have values $1$ or $2$ with the following significance:
- if $V$ is $1$, the second line of the input file contains a natural number $X$ as described above;
- if $V$ is $2$, the second line of the input file contains a decomposition of a number $Y$ in the form of a sequence of natural values where the first term is $m$, followed by $m$ values $f_i$, which respect the conditions $f_i \geq 0$, with $1 \leq i < m$ and $f_m \neq 0$, separated by spaces, as described above.

# Output data
The output file is `bazaf.out`.

If $V$ is $1$, the output file will contain the decomposition in *factorial base* of the number $X$, and if $V$ is $2$, the output file will contain the decomposition in *factorial base* of the number $Y$. The decomposition in *factorial base* involves writing a single line in the output file in the form of a sequence of natural values where the first term is $m$, followed by $m$ values $f_i$, which respect the conditions $0 \leq f_i \leq i$, with $1 \leq i < m$ and $0 < f_m \leq m$, separated by spaces, as described above.

# Constraints and clarifications
- $2 \leq X \leq {10}^{15}$
- $1 < m \leq 100\ 000$
- $0 \leq f_i \leq {10}^9$
- For solving the first task correctly, $30\%$ of the score will be awarded, and for the second task, $70\%$ of the score will be awarded.

# Example 1
`bazaf.in`
```
1
17
```
`bazaf.out`
```
3 1 2 2
```
## Explanation
$V = 1$, so **only** the first task is solved. $X = 17$.

The decomposition of the number $X = 17$ in *factorial base* contains $3$ terms and is composed of the coefficients $1$, $2$, $2$ ($17 = 1! \cdot 1 + 2! \cdot 2 + 3! \cdot 2$).

# Example 2
`bazaf.in`
```
2
2 10 5
```
`bazaf.out`
```
3 0 1 3
```
## Explanation
$V = 2$, so **only** the second task is solved.

The decomposition `2 10 5` is a decomposition with $2$ terms with coefficients $10$, $5$ and corresponds to the number $Y = 20$.

The decomposition in *factorial base* of the number $Y = 20$ will be `3 0 1 3` ($20 = 1! \cdot 0 + 2! \cdot 1 + 3! \cdot 3$).