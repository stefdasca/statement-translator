Given $a$ and $b$ are two non-zero natural numbers.

# Task
Write a program that reads two values $a$ and $b$ from the input file, determines the number of natural numbers formed by exactly $a$ digits where the product of the digits is equal to $b$, and then prints the remainder of this number divided by $9\ 973$ to the output file.

# Input data
The input file `numere.in` contains on the first line the numbers $a$ and $b$ separated by a space.

# Output data
The output file `numere.out` will contain on the first line a single value representing the remainder of the number of natural numbers formed by exactly $a$ digits where the product of the digits is equal to $b$ when divided by $9\ 973$.

# Constraints and clarifications
* For $10\%$ of the tests, $1 \leq a \leq 6, 1 \leq b \leq 1\ 000$
* For $20\%$ of the tests, $7 \leq a \leq 150, 1 \leq b \leq 100$
* For $30\%$ of the tests, $151 \leq a \leq 1\ 000, 1 \leq b \leq 100$
* For $40\%$ of the tests, $1\ 001 \leq a \leq 9\ 000, 100 \leq b \leq 9\ 000$

# Examples

`numere.in`
```
3 9
```

`numere.out`
```
6
```

`numere.in`
```
4 15
```

`numere.out`
```
12
```

`numere.in`
```
1000 210
```

`numere.out`
```
833
```

# Explanations

For the first test:
The six numbers are:
`119 133 191 313 331 911`

For the second test:
`1135 1153 1315 1351 1513 1531 3115 3151 3511 5113 5131 5311`