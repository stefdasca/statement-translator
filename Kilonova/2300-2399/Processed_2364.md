```markdown
# Statement

We construct a recurrent sequence as follows:
$T_n = a \times {T_{n - 2}}^2 + b \times {T_{n - 1}}^2 + x \times T_{n - 2} + y \times T_{n - 1} + z$

# Task

Given $T_0, T_1, a, b, x, y, z$ and $n$, calculate $T_n \ modulo$ a natural number $M$.

# Input data

The input file `sir.in` contains on the first line the natural numbers $T_0, T_1, a, b, x, y, z, M$ and $n$, separated by space, with the meaning from the statement.

# Output data

The output file `sir.out` will contain a single line where a natural number representing $T_n \ modulo \ M$ will be written.

# Constraints and clarifications

* $0 \leq a, b, c, y, z \leq 1\ 000$;
* $0 \leq T_0, T_1 \leq 1\ 000\ 000\ 000$;
* $0 \leq n \leq 10^{16}$;
* $0 < M \leq 7\ 000$;

# Example

`sir.in`
```
1 1 0 0 1 1 0 1000 7
```

`sir.out`
```
21
```

## Explanation

The terms of the sequence are:

$T_0 = 1$

$T_1 = 1$

$T_2 = 0 \times 1^2  + 0 \times 1^2 + 1 \times 1 + 1 \times 1 + 0 = 2$

$T_3 = 0 \times 1^2  + 0 \times 2^2 + 1 \times 1 + 1 \times 2 + 0 = 3$

$T_4 = 0 \times 2^2  + 0 \times 3^2 + 1 \times 2 + 1 \times 3 + 0 = 5$

$T_5 = 0 \times 3^2  + 0 \times 5^2 + 1 \times 3 + 1 \times 5 + 0 = 8$

$T_6 = 0 \times 5^2  + 0 \times 8^2 + 1 \times 5 + 1 \times 8 + 0 = 13$

$T_7 = 0 \times 8^2  + 0 \times 13^2 + 1 \times 8 + 1 \times 13 + 0 = 21$

The result is $T_7 \ mod \ 1\ 000 = 21$.
```