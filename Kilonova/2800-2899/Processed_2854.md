# Task

Given an expression formed according to the description, decide if it is correct and if so, calculate its value.

# Input data

The input file `expresie.in` contains on the first line an expression formed only from braces and natural numbers.

# Output data

The output file `expresie.out` will contain on the first line the value of the expression if it is correct. If the expression in the input file is not correct, then the message `expresie gresita` will be written.

# Constraints and clarifications

* The numbers that appear in expressions are integers and are within the range $0$ to $30\ 000$.
* The expression in the input file is at most $200$ characters long.

# Example 1

`expresie.in`
```
[[34][23[12][]
```

`expresie.out`
```
expresie gresita
```

## Explanation

The expression is incorrect because the braces do not close correctly (for example, the first brace does not close), not all numbers are enclosed in braces and not all pairs of braces contain numbers or subexpressions.

# Example 2

`expresie.in`
```
[4][[6][10]]
```

`expresie.out`
```
6
```

## Explanation

The value of the expression is $6$ because
$[6] = 3$
$[10] = 5$
$[4] = 2$
$[[6][10]] = [(3 + 5)] = 4$
so $[4][[6][10]] = 2 + 4 = 6$.

