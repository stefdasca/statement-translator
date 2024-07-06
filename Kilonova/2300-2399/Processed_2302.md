```markdown
Termopanes found a new friend, Boolanel, the master of Boolean in informatics and wants to have fun together with him. Since Termopanes likes natural numbers and Boolanel likes mirrored numbers, they decide to calculate the sum of numbers $X$ with $N$ digits that do not contain the digit $0$, with the property that $X$ modulo $K = 0$ and $reverse(X)$ modulo $K = 0$. Since the sum of the numbers can be very large, they want to find the sum modulo $M$.

# Task

Help the two calculate the sum from the statement.

# Input data

The input file `xreverse.in` will contain a single line with $3$ natural numbers $N$, $K$, and $M$ with the meanings from the statement.

# Output data

The output file `xreverse.out` will contain a single line that will contain the answer desired by the two.

# Constraints and clarifications

* $1 \leq N \leq 1\ 000\ 000$
* $1 \leq K \leq 32$
* $1 \leq M \leq 10\ 000$
* For $40\%$ of the tests $1 \leq N \leq 10\ 000$ and $1 \leq K \leq 20$
* By $reverse(X)$ it is understood to mirror $X$, for example: $reverse(1234) = 4321$, $reverse(542) = 245$

# Example

`xreverse.in`
```
2 9 6613
```

`xreverse.out`
```
495
```

## Explanation

The numbers $X$ with $2$ digits with the property that $X$ modulo $K = 0$ and $reverse(X) \% K = 0$ are: $18, 27, 36, 45, 54, 63, 72, 81, 99$
```
