## Task

Aurel has learned about arithmetic expressions in mathematics. An arithmetic expression is defined in one of the following ways:

expression

explanation

$n$

$n$ - a non-zero natural number

$e$

$e$ - an arithmetic expression

$e_1+e_2$

$e_1$ and $e_2$ - arithmetic expressions

$e_1*e_2$

$e_1$ and $e_2$ - arithmetic expressions

Aurel would like to find out how many arithmetic expressions of value $V$ and length at most $L$ exist. Help Aurel answer this question.

## Input data

The input file `expresii3.in` will contain on the first line $T$, the number of tests. Each test will contain a single line containing two natural numbers, $L$ and $V$, having the meanings described above.

## Output data

The output file `expresii3.out` will contain $T$ lines, each line $i$ containing the answer for test $i$, modulo $666013$.

## Constraints and clarifications

$1 \leq T \leq 1000$

$1 \leq L, V \leq 50$

The value of an expression represents the result of evaluating the expression (using the rules of mathematics).

The length of an expression represents the number of characters in that expression.

An expression cannot contain spaces or other white characters.

## Example

`expresii3.in`
```
1
3 2
```

`expresii3.out`
```
5
```

## Explanation

The 5 expressions are:
$2$ $(2)$ $1+1$ $1*2$ $2*1$