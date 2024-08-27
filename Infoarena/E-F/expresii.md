# Algebraic Expressions

An algebraic expression can be represented by a tree. We can evaluate the expression by traversing its corresponding tree. The tree representation of an algebraic expression is not necessarily unique. For example, the expression $1+2+3*4$ can be represented by the following two trees: Upon closer inspection, we observe that the sequence of operations $+$ and $*$ is maintained, and the order of operands remains unchanged. In the first tree, the evaluation order will be: $3*4 = 12$ ; $2+12 = 14$ ; $1+14 = 15$ . In the second tree, the expression will be evaluated as: $1+2 = 3$ ; $3*4 = 12$ ; $3+12 = 15$ . Both representations produce the desired result. In this problem, we will consider simple algebraic expressions that contain only single-digit numbers, $+$ , $*$, and parentheses. The expression is evaluated according to normal algebraic rules.

## Task

Determine the number of tree representations that correctly evaluate the expression.

## Input data

The first line of the input file `expresii.in` contains the number of tests $T$. The following lines contain the $T$ tests. Each test consists of a single line, which contains the algebraic expression.

## Output data

For each test, print in the file `expresii.out` a line that follows the format: "Number of trees = $XXX$.", where $XXX$ will be replaced by the number of representations that will evaluate the expression correctly. If the algebraic expression is syntactically incorrect, then the number of correct representations is $0$.

## Constraints and clarifications

The expression does not contain spaces and its length is between $1$ and $50$

$0 < T < 120$

## Example

`expresii.in`
```
6
1+2+3+4
(1+2)+(3+4)
1+2+3*4
1+2+(3*4)
1+*7
1+2*(3+(4*5))
```

`expresii.out`
```
Number of trees = 5.
Number of trees = 1.
Number of trees = 2.
Number of trees = 2.
Number of trees = 0.
Number of trees = 0.
```