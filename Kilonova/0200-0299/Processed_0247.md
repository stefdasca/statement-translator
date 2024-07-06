```markdown
We read from the keyboard a non-zero natural number $x$ written in base 16.

# Task
Calculate the integer part of the base 2 logarithm of the number $x$.
In short, calculate $\\lfloor \log_{2}(x) \\rfloor$.

# Input data
A non-zero natural number $x$ written in base 16.

# Output data
The natural number $\\lfloor \log_{2}(x) \\rfloor$ written in base 10.

# Constraints and clarifications
- **$x$ has a maximum of $100000$ digits in base 16**;
- **$x$ can have leading zeros**;
- The digits in base 16 are, in order, `0123456789ABCDEF`.

# Example 1
`stdin`
```
001
```
`stdout`
```
0
```

# Example 2
`stdin`
```
4A
```
`stdout`
```
6
```

# Explanations
In the first example, $\\text{001}_{(16)}$ is $1_{(10)}$, so $\\lfloor \log_{2}(x) \\rfloor = 0_{(10)}$.
In the second example, $\\text{4A}_{(16)}$ is $74_{(10)}$, so $\\lfloor \log_{2}(x) \\rfloor = 6_{(10)}$.
```