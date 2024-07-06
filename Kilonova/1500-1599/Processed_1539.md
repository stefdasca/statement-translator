```
A set with natural number elements can be written in a **reduced form** if, when ordered in increasing order, the difference between any two consecutive values is the same. For example, set $D = \\{11, 14, 17, 20, 23\\}$ can be written as `D=11-23/3`, specifying the minimum element, the maximum element, and the difference between elements.

Given $N$ sets written in reduced form, each labeled with a capital letter of the English alphabet, it is required to calculate an expression that can contain:
- the union operation, denoted by `+`;
- the intersection operation, denoted by `*`;
- the letters associated with the sets;
- round brackets.

We consider that the **value of the expression** is the set obtained after performing the specific set operations considering that intersection operations have higher priority than union operations.

# Task
Knowing the reduced form of the $N$ sets and an expression, calculate the value of the given expression.

# Input data
The input data is read from the file `multimi.in`, which has the following structure:
- The first line contains the natural number $N$, representing the number of sets;
- The next $N$ lines contain the reduced forms of the $N$ sets, one set per line;
- On line $N+2$ contains the expression to be calculated.

# Output data
The output data will be written to the file `multimi.out`, as follows:
- The first line should contain the number of elements of the set obtained after evaluating the given expression;
- The second line should contain, in increasing order, the elements of that set, separated by a space.

# Constraints and clarifications:
- $1 < N \\leq 16$
- The elements of the sets are natural numbers between $0$ and $1\\ 000\\ 000\\ 000$.
- The number of elements in a set is at most $10\\ 000$.
- The number of characters in the expression is between $3$ and $1\\ 000$.
- The reduced form of a set and the given expression do not contain spaces.
- It is guaranteed that, for all test data, the value of the expression cannot be the empty set.
- It is guaranteed that, in tests totaling 30 points, the expression does not contain parentheses.
- It is guaranteed that, in tests totaling 60 points, the cardinality of each set given at the input does not exceed $1\\ 000$.

# Example 1
`multimi.in`
```
3
A=2-8/2
C=11-23/3
B=4-16/4
A*(B+C)
```
`multimi.out`
```
2
4 8
```

## Explanation
The sets have the following elements:
$A = \\{2, 4, 6, 8\\}$
$B = \\{4, 8,12, 16\\}$
$C = \\{11, 14, 17, 20, 23\\}$

Performing the operations we get:
$B \\cup C = \\{4, 8, 11, 12, 14, 16, 17, 20, 23\\}$
$A \\cap (B \\cup C) = \\{4, 8\\}$

# Example 2
`multimi.in`
```
3
A=2-7/1
B=1-5/1
C=3-9/3
B*A+A*C
```
`multimi.out`
```
5
2 3 4 5 6
```

## Explanation
The sets have the following elements:
$A = \\{2, 3, 4, 5, 6,7\\}$
$B = \\{1, 2, 3, 4, 5\\}$
$C = \\{3, 6, 9\\}$

Performing the operations we get:
$B \\cap A = \\{2, 3, 4, 5\\}$
$A \\cap C = \\{3, 6\\}$
$(B \\cap A) \\cup (A \\cap C) = \\{2, 3, 4, 5, 6\\}$
```

I have double-checked the statement for grammar and syntax errors and corrected any that I found. The structure and format of the original statement have been preserved.