# Sistem2

Given a number $N$. We are asked for a permutation of the set $\{1,2,\dots,N\}$ that respects certain constraints. The $M$ constraints are given in the form of expressions involving the variables $X_1, \dots, X_N$. Each expression contains at least 1 and at most 4 operands, and the operators can be $+$, $-$, $*$, $/$, $=$. Parentheses do not appear. The order of operations is the known one. The operator $/$ can only be used when the IMMEDIATE result of the division is an integer; for example, we can write $2*6/4$ but not $2/4*6$. Each expression ends with a single "$=$" followed by a POSITIVE number (greater than or equal to $0$). In a constraint, each variable appears AT MOST ONCE. It is known that there is at least one solution. If there are multiple solutions, only one is required. Operators are spaced to facilitate reading the data.

## Input data

The first line of the `sistem2.in` input file will contain the numbers $N$ and $M$. The next $M$ lines contain each one constraint.

## Output data

In the `sistem2.out` output file you will print a single line containing the values of the variables $X_1,\dots,X_N$, separated by a space.

## Constraints and clarifications

$1 \leq N \leq 12$
$1 \leq M \leq 20$

## Example

` sistem2.in `
```
4 3
X4 + X2 + X3 = 6
X4 * X3 = 6
X4 + X1 = 6
```

` sistem2.out `
```
4 1 3 2
```

## Explanation

$2 + 1 + 3 = 6$
$2 * 3 = 6$
$2 + 4 = 6$