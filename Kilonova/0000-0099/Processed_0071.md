```markdown
# Task

Miguel has $Q$ square tables (matrices) **indexed from 1**. Each element of a table is equal to the $gcd$ of the indices. He wants to know how many values equal to 1 are there in total.

For example, here is a table of size $4$:

~[masa1.png]

# Input data

The first line contains the number of tables $Q$. The second line contains $Q$ natural numbers, the sizes of each table.

# Output data

Print the total number of values equal to 1.

# Constraints and clarifications

* $1 \leq Q \leq 100000$;
* $0 \leq size\ of\ a\ table \leq 1000000$;
* If the table has size $0$, then it contains $0$ values equal to 1.
* The $gcd$ of two values is the greatest common divisor of these values.

# Example

`stdin`
```
3
1 3 4
```

`stdout`
```
19
```

# Explanation

The table of length $1$ contains $1$ value equal to $1$, the table with length $3$ contains $7$, and the table with length $4$ contains $11$.
```
