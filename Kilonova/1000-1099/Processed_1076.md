A correct parenthesization is obtained by applying one of the following rules:

* The empty string is a correct parenthesization;
* If $S$ is a correct parenthesization, then `(S)` is a correct parenthesization, and the two parentheses `(` and `)` that enclose the string `S` are called pair parentheses;
* If $S_1$, $S_2$, $\\dots$, $S_k$ are correct parenthesizations then the string $S_1 \\ S_2 \\ \\dots \\ S_k$ obtained by concatenating these is a correct parenthesization.

For example, the strings `()`, `()()`, `(())`, and `(()())()` represent correct parenthesizations, while `)(`, `()()(`, and `(()())))` are not correct parenthesizations.
Let $S$ be a string that represents a correct parenthesization. For each pair of parentheses in the string $S$ we associate a cost equal to the difference between the position of the closing parenthesis in $S$ and the position of the matching opening parenthesis. We consider the positions in the string numbered starting from $1$. The total cost of a correct parenthesization is the sum of the costs of all the pair parentheses.
For example, the string `(()())` consists of three pair parentheses, located at positions $2$ and $3$, then $4$ and $5$, respectively $1$ and $6$. The total cost of the parenthesization is $3 - 2 + 5 - 4 + 6 - 1 = 7$.
We call the _swap_ operation the interchange of two adjacent parentheses in the string. This operation is valid only if the new string obtained is itself a correct parenthesization and if the new parenthesization has a total cost strictly less than the initial one.

# Task

Write a program that reads a sequence of $N$ characters representing a correct parenthesization and determines:

1. The total cost associated with the read parenthesization;
2. The minimum cost of a parenthesization obtained by performing a single valid _swap_ operation on the read parenthesization;
3. The number of ways to perform a single valid swap operation on the initial parenthesization to obtain the cost determined according to requirement 2.

# Input data

The input file `swap.in` contains the first line a natural number $N$ and the second line a sequence of $N$ characters representing a correct parenthesization.

# Output data

The output file `swap.out` will contain on the first line a natural number representing the cost of the read parenthesization. The second line will contain a natural number representing the minimum cost determined according to requirement 2 or the value $-1$ when no valid swap operation can be performed on the read parenthesization. The third line of the file will contain a natural number representing the answer to requirement 3 or $0$ if the number displayed according to requirement 2 was $-1$.

# Constraints and clarifications

* $2 \\leq N \\leq 90 \\ 000$;
* Each of the $3$ lines of the output file should contain a single integer. If the number on the first line is correct, $20$% of the test score is awarded. If the number on the second line is correct, $20$% of the score is awarded. If the number on the third line is correct, $60$% of the score is awarded.

# Example

`swap.in`
```
8 
()(())()
```

`swap.out`
```
6
4
1
```

## Explanation

For requirement 1, the cost of the parenthesization is $2 - 1 + 6 - 3 + 5 - 4 + 8 - 7 = 6$. Performing a _swap_ operation between the parentheses at positions $4$ and $5$ results in the string `()()()()` which has a cost of $4$, and this is the only way to obtain this cost.