Mircea the Young must constantly improve the performance of the computers he manages. It sometimes happens that some new components he uses are not compatible with the old computers. For this reason, the operation of the "improved" computers may not be correct. To verify the correctness of the operation of these computers, Mircea proposes to test them with the help of a program that checks the equivalence of logical expressions.

# Task
Write a program that determines whether two logical expressions are equivalent or not. Each expression is composed of:
* variables, the $26$ lowercase letters of the English alphabet, from 'a' to 'z';
* binary operators `|`, `&`, `^` (OR, AND, and XOR respectively);
* the unary operator `~` (NEGATION);
* round brackets.

The expressions will be evaluated respecting the priority rules of the operators and parentheses for the evaluation of logical expressions involving the bits $0$ and $1$. The priorities in decreasing order are: round brackets `(`, `)`, unary operator `~`, binary operators in decreasing order `&`, `^`, `|`.
Two expressions are equivalent if:
* they contain the same set of variables, regardless of the number of occurrences of the variable in the expression;
* for any set of input data for the variables (values $0$, $1$) the result obtained is the same.

# Input data

The input file `logic.in` contains on the first line a natural number $n$, representing the number of tests to be evaluated. Each test represents the evaluation of two expressions. The next $2 \cdot n$ lines are character strings that constitute the expressions. These are written one per line.

# Output data

The output file `logic.out` will contain $n$ lines, on each line $k$ being the message "egale" or "diferite" depending on the result of evaluating the expressions on lines $2 \cdot k$ and respectively $2 \cdot k + 1$ from the input file.

# Constraints and clarifications

* $ 0 < n \leq 50$;
* $n$ represents the number of pairs of expressions to be evaluated;
* An expression contains at most $100$ operations and a maximum of $10$ variables;
* An expression can have at most $255$ characters. The space is not a separator within an expression;
* The name of a variable is a single character, a lowercase letter of the English alphabet;
* The given expressions are correct.

# Example

`logic.in`
```
4
a&(c|~c)
a
~(a|b|c|d)
~a&~b&~c&~d
z&b
a&b
a|b
(a|~a)&(a|~a)&(a|~a)&(a|b)
```

`logic.out`
```
diferite
egale
diferite
egale
```

## Explanation

For the last set of expressions the table is:

~[logic.JPG|align=left|width=80%]

where `E=(a|~a)&(a|~a)&(a|~a)&(a|b)