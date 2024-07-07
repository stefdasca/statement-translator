
We consider a natural number $N$. We define the set of numbers with **communicating digits**, denoted by $A$, as the set consisting of all numbers with $N$ digits, containing only **non-zero digits** and having the sum of the digits equal to $N + 8$. For example, for $N = 2$, the set $A$ is $\\{19, 28, 37, 46, 55, 64, 73, 82, 91\\}$.

# Task

Write a program that reads the natural number $N$ and two elements of the set $A$, $x$ and $y$ ($x < y$) and determines the number of elements in the set $A$, with values between $x$ and $y$ inclusive.

# Input data

The input file `cifreco.in` contains on the first row the natural number $N$, the second row contains the natural number $x$, and the third row contains the natural number $y$, with the above meanings.

# Output data

The output file `cifreco.out` contains on the first line the determined number.

# Constraints and clarifications

* $2 \leq N \leq 18$
* $19 \leq x < y \leq 911\ 111\ 111\ 111\ 111\ 111$
* For $50\%$ of the tests $N \geq 14$.

# Example

`cifreco.in`
```
2
37
82
```

`cifreco.out`
```
6
```

## Explanation

$N = 2$, $x = 37$ and $y = 82$. There are 6 two-digit non-zero numbers, with the sum of the digits equal to 10, between $37$ and $82$ inclusive: $37$, $46$, $55$, $64$, $73$, $82$.
