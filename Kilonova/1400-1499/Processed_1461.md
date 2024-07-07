The provided text translates to the following English version while preserving the format, structure, and custom image syntax:

```markdown
Let's consider a non-zero natural number $n$.
Let us consider an expression of the form: $x_1 - x_2 - x_3 - ... - x_n$
It is known that subtraction is not an associative operation, i.e., $x_1 - (x_2 - x_3) \neq (x_1 - x_2) - x_3$.
As a result, by placing pairs of parentheses in the expression, we can obtain different values. 
For our problem, we will denote a subtraction as an expression of the above form which may also include correctly closed round parentheses. The value of a subtraction is obtained by performing the subtraction operations in order from left to right; if parentheses appear, the operations within parentheses are performed first.

# Task

Given the values of the variables $x_1, x_2, ..., x_n$ involved in subtraction, write a program that solves the following two tasks:
1. Determine the maximum value of a subtraction (obtained by conveniently inserting round parentheses in the expression $x_1 - x_2 - x_3 - ... - x_n$), as well as a subtraction having the maximum value.
2. Determine the value of a specified subtraction.

# Input data

The input file `scadere.in` contains on the first line a natural number $c$ indicating the task that needs to be solved ($1$ or $2$). The second line contains the natural number $n$, which represents the number of variables involved in the subtraction. The variables are numbered from $1$ to $n$ in the order they appear in the subtraction. The following $n$ lines contain the values of the variables $x_1, x_2, ..., x_n$, one value per line. If the task is $2$, the file also contains a line with a string representing a subtraction.

# Output data

The output file `scadere.out` will contain for $c = 1$ two lines; the first line will contain an integer representing the maximum value of a subtraction (obtained by conveniently inserting round parentheses in the expression $x_1 - x_2 - x_3 - ... - x_n$), and the second line a subtraction having the maximum value. If $c = 2$, the output file will contain a single line with an integer representing the value of the subtraction specified on the last line of the input file.

# Constraints and clarifications

* $3 \leq n \leq 5 \ 000$
* The values of the variables $x_1, x_2, ..., x_n$ are integers in the range $[-100, 100]$.
* The subtraction in the input file, respectively the subtraction of maximum value displayed in the output file, will have a maximum of $40 \ 000$ characters which can only be digits, the lowercase letter `x`, round parentheses, and the `-` (minus) operator.
* For tests worth $50\%$ of the score, the task will be $1$. For a correct display of the maximum value, $40\%$ of the score per test is awarded. Full points are awarded for correctly displaying both the maximum value and a subtraction of maximum value.

# Example 1

`scadere.in`
```
1
4
-7
5
-10
19
```

`scadere.out`
```
17
x1-x2-(x3-x4)
```

## Explanation

The parentheses that lead to the maximum value are: $x_1 - x_2 - (x_3 - x_4) = - 7 - 5 - (- 10 - 19) = - 12 - (- 29) = - 12 + 29 = 17$

# Example 2

`scadere.in`
```
2
4
-7
5
-10
19
x1-((x2-x3)-x4)
```

`scadere.out`
```
-3
```

## Explanation

$x_1 - ((x_2 - x_3) - x_4) = - 7 - ((5 - 10) - 19) = - 7 - (15 - 19) = - 7 - (- 4) = - 7 + 4 = - 3$
