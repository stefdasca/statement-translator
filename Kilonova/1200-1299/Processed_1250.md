# Task

Analyzing the results obtained by competitors in $n$ competitions in a sports discipline where scores range between $2$ and $5$, a coach notices that all his students have exhibited the same strange behavior, namely:

- if one of them scores two consecutive $4$'s or two consecutive $3$'s, they will continue to prepare without special motivation and will receive a score of $3$ in the next competition;
- if the athlete scores two $5$'s, they consider themselves a star, stop preparing, and will receive a score of $2$ in the next competition;
- if the athlete scores two different scores, the next score they receive will be equal to the highest of the two different scores.

The coach has also noticed that no athlete starts with two $2$'s.

# Task

Given the scores that an athlete receives in the first two competitions as well as the number $n$ of competitions the athlete has participated in, calculate the arithmetic mean of the $n$ scores obtained, accurate to two decimal places.

# Input data

From the file `sport.in` we read:
- the first line contains two values $a$ and $b$, separated by a space, representing the first two scores;
- the second line contains a value $n$ which represents the number of competitions in which the athlete with the initial scores $a, b$ participated.

# Output data

In the file `sport.out` print a single number representing the arithmetic mean of the scores obtained, accurate to two decimal places.

# Constraints and clarifications

* $2 \leq a, b \leq 5$; $a$ and $b$ are natural numbers;
* $2 < n < 5 \ 000 \ 000$

# Example 1

`sport.in`
```
4 5
5
```

`sport.out`
```
4.20
```

## Explanation

The $5$ scores are: $4, 5, 5, 2, 5$

# Example 2

`sport.in`
```
4 3
6
```

`sport.out`
```
3.66
```

## Explanation

The $6$ scores are: $4, 3, 4, 4, 3, 4$