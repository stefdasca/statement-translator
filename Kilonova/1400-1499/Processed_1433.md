It is assumed that some of the first calculating tools were counting sticks. In our problem, we will consider a number as a sequence of one or more sticks, a stick being represented by the letter `I`. In an expression, between any two numbers there is a `+` (addition) sign or a `*` (multiplication) sign.
Examples:
~[betisoare.png|align=center]

# Task

Write a program that evaluates such expressions.

# Input data

The input file `betisoare.in` contains on the first line a natural value $n$, which indicates the number of expressions that need to be evaluated. Each of the following $n$ lines contains a string of maximum $1 \ 000 \ 000$ characters that represents the expression to be evaluated.

# Output data

The output file `betisoare.out` will contain on each line $i$ of the first $n$ lines an integer number representing the result of evaluating the expression on line $i + 1$ from the input file.

# Constraints and clarifications

* $1 \leq n \leq 10$
* An expression can have at least $1$ character and at most $1 \ 000 \ 000$ characters.
* The values calculated during the process and the final value have a maximum of $18$ digits.
* Of the tests, $26\%$ contain only addition operations, $22\%$ only multiplication operations, and the remaining $52\%$ contain both operations.

# Example 1

`betisoare.in`
```
1
I+I*III+IIIIIII
```

`betisoare.out`
```
11
```

## Explanation

$1 + 1 \cdot 3 + 7 = 11$

# Example 2

`betisoare.in`
```
2
IIII
I+I
```

`betisoare.out`
```
4
2
```

## Explanation

$4 = 4$
$1 + 1 = 2$

# Example 3

`betisoare.in`
```
3
I+I+I+I+I+I+I+I+I
I*I*I*I*I*I*I
IIII*IIII+I
```

`betisoare.out`
```
9
1
17
```

## Explanation

$1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 9$
$1 \cdot 1 \cdot 1 \cdot 1 \cdot 1 \cdot 1 \cdot 1 = 1$
$4 \cdot 4 + 1 = 17$