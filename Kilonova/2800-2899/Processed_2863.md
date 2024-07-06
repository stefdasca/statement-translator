Let's consider an arithmetic expression containing only variable operands whose names are formed from single lowercase English alphabet letters. The initial values of the variables that can appear in the expression are: $a = 1$, $b = 2$, $...$, $z = 26$. The expression can use two binary operators (`+` and `–`, representing addition and subtraction respectively) and two unary operators (`++` and `--`, representing the increment operator and the decrement operator respectively). The unary operators `++` and `--` can be placed only before or after a variable. If the unary operator `++` appears before a variable, then the value of the variable is increased by $1$ before the variable's value is taken into account in the expression's calculation. For example, the value of the expression `++c–b` is $2$, and the value of the variable $c$ after evaluating the expression will be $4$. When the unary operator `++` appears after a variable, the value of the variable is increased by $1$ after the value of that variable is used in the expression's calculation. For example, the value of the expression `c++–b` is $1$, and the value of the variable $c$ after evaluating the expression will be $4$. The `--` operator behaves in the same way, with the observation that the value of the variable will be decreased by $1$. Unary operators have a higher priority than binary ones (specifically, increments/decrements are executed first, then additions and subtractions). If there are multiple operations with the same priority, they will be executed in order from left to right.

# Task

Write a program to determine the value of an expression, as well as the final values of the variables used in the expression.

# Input data

The input file `eval.in` contains on the first line the expression. It can also contain spaces.

# Output data

The output file `eval.out` contains on the first line an integer that represents the value of the expression, and on the following lines the values of the variables used in the expression, one value per line, in the alphabetical order of the variables.

# Constraints and clarifications

* The expression will contain at least one variable.
* The number of characters in the expression is less than $1\ 000$.
* The expression does not contain any ambiguity (e.g., `a+++b` or `a---b`).
* The operators `++` and `--` will not appear simultaneously before and after a variable (e.g., `++a++` or `++a--`).

# Example 1

`eval.in`
```
d -- + a – b
```

`eval.out`
```
3
1
2
3
```

## Explanation

The value of the expression is $3$.
* $a = 1$
* $b = 2$
* $d = 3$

# Example 2

`eval.in`
```
q- u   -+         +a-c++ - ++ t
```

`eval.out`
```
-30
2
4
17
21
21
```

## Explanation

The value of the expression is $-30$.
* $a = 2$
* $c = 4$
* $q = 17$
* $t = 21$
* $u = 21$