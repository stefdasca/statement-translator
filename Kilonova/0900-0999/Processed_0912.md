
Gigel, passionate about numbers, knows that any natural number can be written in a numeral system of base $b$ as a sequence of symbols that have values from $0$ to $b - 1$. For example, the number $7$, written in base $10$, is $111$ in base $2$, and the number $26732$, written in base $10$, is a sequence of $3$ symbols in base $37$, the first two having the value $19$, and the last one having the value $18$. He discovered that there are numbers which can be written in **exactly two** different bases with exactly three identical symbols. For example, the number $931 \\ (10)$ is $777 \\ (11)$ in base $11$, and $111 \\ (30)$ in base $30$.

# Task

Given a natural number $N$, determine the largest natural number less than or equal to $N$, which has the property that it can be written in exactly two different bases using exactly $3$ identical symbols.
1. Write the determined number.
2. Write the two determined bases and the respective values of the symbols.

# Input data

The input file `cate3cifre.in` contains on the first line the task ($1$ or $2$). The second line of the input file contains the natural number $N$.

# Output data

The output file `cate3cifre.out` will contain on the first line, if the task is $1$, the determined number. If the task is $2$, the first and the second line of the output file have the same structure: on each line, write, separated by a space, two natural numbers $b \\ c$, representing the base and the value of the required symbol in that base. The two bases are displayed in ascending order.

# Constraints and clarifications

* $0 < N \leq 1 \ 000 \ 000$;
* For correctly solving task $1$, $60$ points will be awarded. For task $2$, $30$ points will be awarded.
* For $50$ points, $N \leq 10 \ 000$;
* $10$ points are given by default (tests corresponding to these points will be the same as the first example)
* The number $xyz \\ (b)$ written in base $b$ with symbols $x, y, z$ is written in base $10$ as a value calculated as follows: $x \cdot b^2 + y \cdot b + z$ (where the symbols $x, y, z$ are replaced with the corresponding values)
* For each test, there is a solution.

# Example 1

`cate3cifre.in`
```
1
1000
```

`cate3cifre.out`
```
931
```

## Explanation

The determined number is $931$

The determined number is written in base $11$ as $777 \\ (11)$

The same number is written in base $30$ as $111 \\ (30)$

# Example 2

`cate3cifre.in`
```
2
1000
```

`cate3cifre.out`
```
11 7
30 1
```

# Example 3

`cate3cifre.in`
```
1
30000
```

`cate3cifre.out`
```
26733
```

## Explanation

The determined number is $26733$

The determined number is written in base $37$ as $(19)(19)(19) \\ (37)$

The same number is written in base $163$ as $111 \\ (163)$

# Example 4

`cate3cifre.in`
```
2
30000
```

`cate3cifre.out`
```
37 19
163 1
```
