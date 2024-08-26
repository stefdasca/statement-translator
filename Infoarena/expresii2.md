## Task

A logical expression is formed from variables (uppercase Latin letters) and operators ($+$ for disjunction, $*$ for conjunction, and $!$ for negation). For example, $!((A + B) * A)$ is a logical expression in infix form. An expression in postfix form is characterized by the disappearance of parentheses and the placement of operators at the end. Here is an example of expressions in infix and postfix forms:
infix form -> postfix form: 
$!((A + B) * A)$ -> $AB+A*!$
$(A + B) * C * (B + A)$ -> $AB+C*BA+*$

We consider a lexicographic order on the set of operators and on the set of variables ($a\dots z < + < * < !$). First, we need to count all postfix expressions of length $N$ that have variables among the first $K$ letters of the Latin alphabet, and operators among those mentioned above. Then, we need to display the expression at position $P$ in the sorted list of expressions (the first expression in the list is at position $1$).

## Input data

The file `expresii2.in` will contain, on the first line, $N$, $K$, and $P$.

## Output data

The file `expresii.out` will contain on the first line the number of possible expressions, and on the second line print the $P$-th expression from the lexicographically sorted list.

## Constraints

$1 \leq N \leq 30$

$1 \leq K \leq 26$

$1 \leq P \leq \text{number of possible expressions}$

$N$ and $K$ will be chosen such that the number of expressions is less than $2^{63}$

$40\%$ of the tests will have $P = 1$

## Example

`expresii2.in`
```
4 2 3
```

`expresii2.out`
```
26
AA!+
```

## Explanation

Here are the first 5 of the 26 possible expressions:
$AA+!$
$AA*!$
$AA!+$
$AA!*$
$AB+!$