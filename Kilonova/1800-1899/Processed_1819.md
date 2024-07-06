Dorel has an arithmetic expression represented as a string of length $N$, containing non-zero digits as operands, and addition and multiplication as arithmetic operators, represented by `+` and `*`. The arithmetic expression can undergo at most $K$ swaps between two operators.

For example, for the expression $2 \cdot 3 + 5 + 7 + 1$, which has a value of $19$, if we perform a swap between the first and third operators, we get the expression $2 + 3 + 5 \cdot 7 + 1$, which has a value of $41$.

# Task

Determine the maximum value of the expression after performing at most $K$ swaps between two operators.

# Input data

The input file `expresia.in` contains:
- The first line contains the integers $N$ and $K$, separated by a space.
- The second line contains the arithmetic expression.

# Output data

The output file `expresia.out` will contain a single line which will display the maximum value of the arithmetic expression.

# Constraints and clarifications

* $3 \leq N < 1000$
* $0 \leq K \leq 100$
* $0 \leq P \leq 18$, where $P$ is the number of `*` operators
* $N$ is an odd number

|#|Points|Constraints|
|-|-|-----------|
|1|12|$K = 0$|
|2|17|$P = 1$, $K = 1$|
|3|20|$1 \leq K < P$, $3 \leq N < 40$|
|4|32|$1 < P \leq K$, $41 \leq N < 1\ 000$|
|5|19|$1 \leq K < P$, $41 \leq N < 1\ 000$|

# Example 1

`expresia.in`
```
9 1
2*3+5+7+1
```

`expresia.out`
```
41
```

## Explanation

For the first example, a swap is performed between the first and the third operator, resulting in the expression $2+3+5 \cdot 7+1$ which has a value of $41$.

# Example 2

`expresia.in`
```
19 2
2+4+1+5*3+9+1*6+1+7
```

`expresia.out`
```
157
```

## Explanation

For the second example, a swap is performed between the fifth and the seventh operators, resulting in the expression $2+4+1+5 \cdot 3 \cdot 9+1+6+1+7$ which has a value of $157$.