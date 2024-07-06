```markdown
Let $a$ and $b$ be two natural numbers $0 < a \leq b$.

# Task
Determine the number of different fractions $\\frac{x}{y}$ that can be formed using non-zero natural numbers, having the properties:
- $\\frac{a}{b} \leq \\frac{x}{y} \leq \\frac{b}{a}$
- $2 \leq x + y \leq a + b$

For example, for $a = 2$ and $b = 4$, there are $9$ different fractions with the properties: $\\frac{2}{4} \leq \\frac{x}{y} \leq \\frac{4}{2}$ and $2 \leq x + y \leq 6$. These are $\\{ \\frac{2}{4}, \\frac{1}{1}, \\frac{2}{2}, \\frac{3}{3}, \\frac{2}{1}, \\frac{1}{2}, \\frac{2}{3}, \\frac{3}{2}, \\frac{4}{2} \\}$.

# Input data
The input file `nfrac.in` contains on the first line a natural number $T$, and on each of the following $T$ lines a pair of numbers $a$ and $b$ with the above significance.

# Output data
The output file `nfrac.out` will contain $T$ lines. On line $i$, $1 \leq i \leq T$, it will contain the number of required fractions, corresponding to the pair found on line $i+1$ of the input file.

# Constraints and clarifications
- $0 < a \leq b \leq 1000000$
- $1 \leq T \leq 100$
- **Two fractions $\\frac{x_1}{y_1}$ and $\\frac{x_2}{y_2}$ are considered distinct if and only if $x_1 \neq x_2$ or $y_1 \neq y_2$**

# Example
`nfrac.in`
```
3
2 4
128 256
12345 56789
```
`nfrac.out`
```
9
24768
1536317971
```

# Explanation
The input file contains $T = 3$ pairs of numbers.

There are $9$ fractions with the properties:
- $\\frac{2}{4} \leq \\frac{x}{y} \leq \\frac{4}{2}$
- $2 \leq x + y \leq 6$

There are $24768$ fractions with the properties:
- $\\frac{128}{256} \leq \\frac{x}{y} \leq \\frac{256}{128}$
- $2 \leq x + y \leq 384$

There are $1536317971$ fractions with the properties:
- $\\frac{12345}{56789} \leq \\frac{x}{y} \leq \\frac{56789}{12345}$
- $2 \leq x + y \leq 69134$
```