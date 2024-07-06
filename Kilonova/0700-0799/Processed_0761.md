# Georgel wants to test Săndel's mathematical knowledge. To do this, he presents Săndel with two natural numbers $a$ and $b$. By placing the first digit of number $a$ in the place of the first digit of number $b$, a new number is formed. Another number is formed by placing the first digit of number $a$ in the place of the last digit of number $b$. Two more new numbers are formed by placing the second digit of number $a$ in the place of the first digit of number $b$, and in the place of the last digit of number $b$, respectively. The formation of other numbers continues by using the same rules until all digits of the number $a$ are exhausted (if the number $a$ has $3$ digits, then $6$ numbers will be formed).

# Task

Given the two numbers $a$ and $b$, Săndel must find the largest prime number formed according to the above rule, knowing that the initial values of the numbers $a$ and $b$ are also taken into account. If there is no prime number according to the above requirements, the largest number that can be formed, including the initial values of the numbers $a$ and $b$, will be displayed.

# Input data

The first line of the input file `test.in` contains the two numbers $a$ and $b$, in this order.

# Output data

The first line of the output file `test.out` will contain the requested number.

# Constraints and clarifications

* $10 \\leq a, b \\leq 1 \ 000 \ 000$

# Example 1

`test.in`
```
19 913
```

`test.out`
```
919
```

## Explanation

The numbers formed are: $113$ (using the first digit from $a$ in place of the first digit from $b$), $911$ (using the first digit from $a$ in place of the last digit from $b$), $913$ (using the second digit from $a$ in place of the first digit from $b$), $919$ (using the second digit from $a$ in place of the last digit from $b$). To these numbers, the initial values of $a$ and $b$ are added, which are $19$ and $913$. It is observed that the largest prime number among the above numbers is $919$.

# Example 2

`test.in`
```
260 444
```

`test.out`
```
644
```

## Explanation

The numbers formed are: $244$ (using the first digit from $a$ in place of the first digit from $b$), $442$ (using the first digit from $a$ in place of the last digit from $b$), $644$ (using the second digit from $a$ in place of the first digit from $b$), $446$ (using the second digit from $a$ in place of the last digit from $b$), $44$ (using the third digit from $a$ in place of the first digit from $b$) and $440$ (using the third digit from $a$ in place of the last digit from $b$). To these numbers, the initial values of $a$ and $b$ are added, which are $260$ and $444$. It is observed that there is no prime number, so the largest number among the above numbers, namely $644$, will be displayed.