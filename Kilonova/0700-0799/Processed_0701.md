Once upon a time, there was a dragon with $6$ heads. One day, Prince Charming got upset and cut off one of its heads. Overnight, the dragon grew another $6$ heads in its place. On the same neck! The next day, Prince Charming cut off another head, but overnight the dragon grew another $6$ heads in its place... and this continued for $n$ days. On the ($n+1$)-th day, Prince Charming got bored and went home!

# Task

Write a program that reads $n$, the number of days, and calculates how many heads the dragon has after $n$ days.

# Input data

The input file `balaur.in` will contain the number $n$.

# Output data

The output file `balaur.out` will contain a single number representing how many heads the dragon had after $n$ days.

# Constraints and clarifications

* $1 \leq n \leq 400\ 000\ 000$

# Example

`balaur.in`
```
3
```

`balaur.out`
```
15
```

## Explanation

Initially, the dragon had $6$ heads. On the first day, Prince Charming cut off one head and it had $5$ left. Overnight, it grew another $6$, so the next morning the dragon had $11$ heads. On the second day, Prince Charming cut off one more head, leaving the dragon with $10$ heads. Overnight, it grew another $6$, so on the third morning, the dragon had $16$ heads. But on the third day, Prince Charming cut off another head, leaving the dragon with $15$ heads after the third day.