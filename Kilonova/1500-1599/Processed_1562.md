```
Archaeologists have found an artifact that seems to contain a mathematical equation, which uses the symbols of an unknown script. A series of hypotheses have begun to emerge, so they propose to solve the equation in order to decipher the symbols. The equation contains $N + M$ terms, each term representing a number encoded by a sequence of symbols, which have been replaced with uppercase English alphabet letters from $A$ to $Z$. It is assumed that the sum of the first $N$ numbers must be equal to the sum of the last $M$ numbers. Also, each letter corresponds to a digit from $0$ to $9$, and two different letters are associated with two different digits.

# Task

The task is to find how many distinct solutions the given equation admits.

# Input data

In the file `artifact.in` the first line contains two non-zero natural numbers $N$ and $M$ separated by a space. The second line contains the $N + M$ character strings, separated by a space, representing the terms of the equation.

# Output data

In the file `artifact.out` the first line will contain the number of distinct solutions of the given equation.

# Constraints and clarifications

* $1 \leq N$
* $1 \leq M$
* $N+M \leq 5\ 000$;
* Each number is encoded by at most 14 characters
* Numbers encoded with at least two digits cannot have the most significant digit equal to $0$;
* It is guaranteed that the equation has at least one solution;
* Two solutions are distinct if at least one of the letters has different values in the two solutions;

# Example 1

`artifact.in`
```
3 1
A A A BA
```

`artifact.out`
```
1
```

## Explanation

A + A + A = BA admits only one solution: $5 + 5 + 5 = 15$

# Example 2

`artifact.in`
```
2 1
THIS IS EASY
```

`artifact.out`
```
7
```

## Explanation

THIS + IS = EASY admits $7$ solutions:
$7962 + 62 = 8024$

$5974 + 74 = 6048$

$1974 + 74 = 2048$

$2974 + 74 = 3048$

$5987 + 87 = 6074$

$1987 + 87 = 2074$

$2987 + 87 = 3074$
```
