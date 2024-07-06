For a non-zero natural number $x$, we define the rotation operation by $k$ digits as moving the first $k$ digits of $x$ to the end, in the same order. The rotation operation by $k$ digits is possible only if the number of digits of $x$ is strictly greater than $k$.

Examples:
* applying the rotation operation by $3$ digits to the number $123\ 456$ results in $456\ 123$;
* applying the rotation operation by one digit to the number $222$ results in $222$;
* applying the rotation operation by two digits to the number $1\ 000$ results in $10$.

A sequence of $n$ non-zero natural numbers is given. Rotation operations can be applied to some numbers in the sequence so that no two numbers have the same number of digits after rotation.

# Task

Determine the maximum sum that can be obtained by summing the numbers in the given sequence, after convenient rotation of some numbers in the sequence, according to the specifications in the statement.

# Input data

The input file `numbers.in` contains the number $n$ on the first line, and on the second line a sequence of $n$ non-zero natural numbers, separated by a space.

# Output data

The output file `numbers.out` will contain a single line that will print the maximum sum obtained.

# Constraints and clarifications

* $1 \leq n \leq 10\ 000$
* The numbers in the sequence are non-zero natural numbers and have at most $15$ digits.

|#|Score|Constraints|
|-|-|-|
|1|20|$1 \leq n \leq 8$|
|2|60|$10 \leq n \leq 200$|
|3|20|No additional constraints|

# Example 1

`numbers.in`
```
3
2 15 31
```

`numbers.out`
```
84
```

## Explanation

Rotate $15$ by one digit to obtain $51$. $2 + 51 + 31 = 84$.

# Example 2

`numbers.in`
```
4
17 15 204 1
```

`numbers.out`
```
507
```

## Explanation

Rotate $17$ by one digit and $204$ by two digits. The sum is $71 + 15 + 420 + 1 = 507$.

# Example 3

`numbers.in`
```
4
21 31 42 87
```

`numbers.out`
```
181
```

## Explanation

No number is rotated. The maximum sum is $21 + 31 + 42 + 87 = 181$.

# Example 4

`numbers.in`
```
4
23 113 45719 55588
```

`numbers.out`
```
183469
```

## Explanation

Rotate $23$ by one digit, $113$ by two digits, $45\ 719$ by $4$ digits and $55\ 588$ by $3$ digits. The maximum sum is $32 + 311 + 94\ 571 + 88\ 555 = 183\ 469$.