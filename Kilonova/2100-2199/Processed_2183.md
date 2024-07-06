# Task

How many words of length $N$ exist that contain the word $X$ as a substring?

# Input data

The first line contains $N$. The second line contains the word $X$.

# Output data

Print the number of words modulo $10^9+7$.

# Constraints and clarifications

* $1 \leq N \leq 1000$
* $1 \leq |X| \leq 100$, $|X|$ is the length of the word $X$
* The words must be composed only of uppercase letters $A...Z$

# Example 1

`stdin`
```
6
ABCDB
```

`stdout`
```
52
```

## Explanation

All words of the form $xABCDB$ and $ABCDBx$ are valid.

# Example 2

`stdin`
```
122
AABA
```

`stdout`
```
956357460
```
