```markdown
The control digit of a natural number is obtained by summing the digits of the number; if the obtained result is a digit, that is the control digit of the given number; otherwise, the sum of the digits of the obtained result is calculated, repeatedly applying this procedure until a single-digit result is obtained.
For example, the control digit of the number $998 979$ is $6$, because: $9 + 9 + 8 + 9 + 7 + 9 = 51$, then $5 + 1 = 6$

# Task

Given two natural numbers $a$ and $b$, as well as a digit $c$, determine how many numbers between $a$ and $b$, inclusive of $a$ and $b$, have the control digit equal to $c$.

# Input data

The input file `control.in` contains on the first line the values $a b c$ separated by a space.

# Output data

The output file `control.out` will contain a single line which will contain a natural number $k$ that represents the number of values between $a$ and $b$ (inclusive) that have a control digit equal to $c$.

# Constraints and clarifications

* $1 \leq a \leq b \leq 2 000 000 000$
* $1 \leq c \leq 9$

# Example

`control.in`
```
10056 10105 7
```

`control.out`
```
6
```

## Explanation

The $6$ numbers that have the control digit $7$ between $10056$ and $10111$ are:
$10060: 1 + 0 + 0 + 6 + 0 = 7$
$10069: 1 + 0 + 0 + 6 + 9 = 16; 1 + 6 = 7$
$10078: 1 + 0 + 0 + 7 + 8 = 16; 1 + 6 = 7$
$10087: 1 + 0 + 0 + 8 + 7 = 16; 1 + 6 = 7$
$10096: 1 + 0 + 0 + 9 + 6 = 16; 1 + 6 = 7$
$10105: 1 + 0 + 1 + 0 + 5 = 7$
```
