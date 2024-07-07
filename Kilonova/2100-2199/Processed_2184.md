
# Task

Given a word, rearrange its letters to become a palindrome.

# Input data

The first line contains the word.

# Output data

The minimum lexicographic palindrome word or $-1$ if it is not possible.

# Constraints and clarifications

* $1 \leq |C| \leq 10^6$, $|C|$ is the length of the word.
* The word consists only of uppercase letters.
* The minimum lexicographic word must be printed.
* If no solution exists, print $-1$.
* A word is a palindrome if it reads the same backward as forward.

# Example 1

`stdin`
```
AAAACACBA
```

`stdout`
```
AAACBCAAA
```

# Example 2

`stdin`
```
AB
```

`stdout`
```
-1
```
