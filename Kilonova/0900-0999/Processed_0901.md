Here is the translated version of the given text:

```markdown
Given a mathematical expression in which the characters `x`, `y`, `z`, `t`, digits, and the signs `+` or `-` may appear.

Adjacent digits form numbers. Letters represent variables. A variable can be preceded by a number. There are no other characters between the variable and the preceding number. A group consisting of a letter and, possibly, a preceding number forms a monomial. A monomial **does not** contain multiple letters. The number appearing in a monomial is called the coefficient.

The expression may also contain numbers that are not followed by a variable. These numbers are called constant terms.

Therefore, the expression consists of monomials and constant terms. Each monomial and each constant term is preceded by one of the signs `+` or `-`.

Examples:

| Correct expressions | Incorrect expressions |
| - | ------- |
| `-x+100`  | `x+100` (`x` is not preceded by `+` or `-`)   |
| `+3x+2y-3z+7x-15-3+8z-7y`  | `+x+y-3zt` (`3zt` is not a monomial because it contains two letters) |
| `+10x-7y+3x-7+5z-8t-z-x-y+3` | `-x + y -34*t + 5z - 5u` (the expression contains invalid characters, in this case spaces, the letter `u`, and the sign `*`)|

The mathematical value of an expression is the value obtained if we replace the letters appearing in the expression with numerical values and perform the calculations. The value of a monomial is obtained by multiplying the coefficient of the monomial by the value of the variable appearing in that monomial. For example, the value of the expression `+3x` for $x=2$ is $6$.

# Task

Given a correct expression, determine:

1. The mathematical value of the expression if $x$, $y$, $z$, and $t$ have the value $1$.
2. The number of distinct quartets $(x, y, z, t)$ of integer values that belong to a given interval $[a, b]$, for which the mathematical value of the corresponding expression is equal to a given value $E$. Two quartets are distinct if there is at least one position for which the corresponding values are different.

# Input data

The input data is read from the file `eq4.in`, which has the following structure:

* The first line contains the natural number $C$, which can be either $1$ or $2$, depending on the task to be solved
* The second line contains the given expression
* The third line contains the values $a \ b \ E$, separated by a space.

# Output data

The output data will be written to the file `eq4.out` as follows:

* If $C=1$, the first line should contain the answer to task $1$
* If $C=2$, the first line should contain the answer to task $2$.

# Constraints and clarifications

* The coefficients are natural numbers with at most $4$ digits
* $1 \leq$ length of the expression $\leq 100 \ 000$
* $-500 \leq a \leq b \leq 500$
* $-10^{15} \leq E \leq 10^{15}$
* In at least $30\%$ of tests, the given expression contains at most three of the letters `x`, `y`, `z`, or `t`.
* $10$ points are awarded by default.

| $C$ | Points |
| - | ------- |
| $1$ | 20      |
| $2$ | 70      |

# Example 1

`eq4.in`
```
1
+10x-7y+3x-7+5z-8t-z-x-y+3
-1 1 0
```

`eq4.out`
```
-4
```

## Explanation

We solve task $1$:
The value of the expression is: $10-7+3-7+5-8-1-1-1+3 = -4$.

# Example 2

`eq4.in`
```
1
-x+1
-1 1 0
```

`eq4.out`
```
0
```

## Explanation

We solve task $1$:
The value of the expression is $-1+1 = 0$.

# Example 3

`eq4.in`
```
2
+10x-7y+3x-7+5z-8t-z-x-y+3
-1 1 0
```

`eq4.out`
```
8
```

## Explanation

We solve task $2$:
There are $8$ quartets: $(-1,-1,0,-1)$, $(0,-1,-1,0)$, $(0,-1,1,1)$, $(0,0,-1,-1)$, $(0,0,1,0)$, $(0,1,1,-1)$, $(1,0,0,1)$, $(1,1,0,0)$ for which the expression equals $0$.

# Example 4

`eq4.in`
```
2
-x+1+0z
-1 1 0
```

`eq4.out`
```
27
```

## Explanation

We solve task $2$:
There are $27$ quartets: $(1,-1,-1,-1)$, $(1,-1,-1,0)$, $(1,-1,-1,1)$, $(1,-1,0,-1)$, $(1,-1,0,0)$, $(1,-1,0,1)$, etc. for which the expression equals $0$.
