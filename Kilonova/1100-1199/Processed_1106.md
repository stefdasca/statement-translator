Below is the translated text according to the specified instructions:

---

The teacher begins the lesson by writing the following sequence of numbers on the board: 
$1, 1, 1, 2, 1, 1, 2, 3, 1, 3, 1, 2, 3, 4, 1, 3, 1, 2, 3, 4, 5, 1, 3, 5, 1, 2, 3, 4, 5, 6, 1, 3, 5, \dots$. 

The children interrupt him and announce that they have found the rule according to which the terms of the sequence are constructed successively, namely: write $1$ followed by $1$, then $1, 2$ followed also by $1$, then $1, 2, 3$ followed by $1$ and $3$, then $1, 2, 3, 4$ followed also by $1$ and $3 \dots$ Always, at some point after the sequence $1, 2, \dots, k$ the odd numbers from $1$ to $k$ are written. Obviously, this is an infinite sequence. Starting the numbering from $1$, we have, for example, at position $3$ the value $1$, at position $4$ the value $2$, at position $8$ the value $3$, etc. The teacher is happy but tells the kids that for large positions it is difficult to mentally calculate the values in the sequence. Ștefan, a good programming student, says he can write a source to calculate many values in the sequence.

# Task

Given a position in the sequence, determine the value at that position. Given a value, determine the smallest position in the sequence where the value is found.

# Input data

From the keyboard, two numbers $C$ and $V$ are read. If $C = 1$, the value at position $V$ in the sequence must be determined. If $C = 2$ it is required to determine the smallest position in the sequence where the value $V$ is found.

# Output data

The screen will contain a single natural number corresponding to the result obtained for each task.

# Constraints and clarifications

* $1 \leq C \leq 2$
* For $25$\% of the score, $C = 1$ and $V \leq 100\ 000$
* For $25$\% of the score, $C = 1$ and $100\ 000 \lt V \leq 1\ 000\ 000\ 000$
* For $50$\% of the score, $C = 2$ and $1 \lt V \leq 35\ 000$

# Example 1

`stdin`
```
1
8
```

`stdout`
```
3
```

## Explanation

$C = 1$, the value at position $8$ is required. This is $3$.

# Example 2

`stdin`
```
2
3
```

`stdout`
```
8
```

## Explanation

$C = 2$, the smallest position where the value $3$ is found is required. This is $8$.

---

Please review the translation and confirm if there are more details or modifications needed.