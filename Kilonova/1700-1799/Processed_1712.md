Dorel, the "jack-of-all-trades," plans to "disrupt" the harmony of a string $S$ consisting of $N$ lowercase English alphabet characters, $S = (S_1, S_2, \dots, S_N)$.

He randomly chooses a character from the string, located at position $k \ (1 \leq k \leq N)$ and searches to the left of $k$ for the first character greater than or equal to $S_k$, located at position $i$, $S_k \leq S_i$. If this does not exist, $i = 1$. This selection is not enough. Dorel searches to the right of $k$ for the first character less than or equal to $S_k$, located at position $j$, $S_j \leq S_k$. If this does not exist, $j = N$. He extracts from the string $S$ the subsequence thus delimited. As a result of the made choice, Dorel obtains two subsequences:

- $X = (S_1, S_2, \dots, S_{i-1}, S_{j+1}, S_{j+2}, \dots, S_N)$
- $Y = (S_i, S_{i+1}, \dots, S_j)$

# Task

Given the string $S$, help Dorel answer $Q$ questions of the form:

- For a position $k$ in the string $S$, determine the maximum length of a **common palindromic subarray** of the strings $X$ and $Y$.

# Input data

The input file `dorel.in` contains on the first line a string of characters. The second line contains a positive natural value $Q$. The next line contains the $Q$ questions in the specified format.

# Output data

The output file `dorel.out` will contain the answers to the $Q$ questions.

# Constraints and clarifications

* $1 \leq N \leq 10\  000$
* $1 \leq Q \leq 5\  000$
* $N \cdot Q \leq 5\  000\  000$
* $X$ and $Y$ are non-empty strings
* A palindromic subarray of a string is understood as a sequence of characters located at consecutive positions in the string which is a palindrome (the sequence traversed from left to right is identical to the sequence traversed from right to left).
* The maximum length of a common palindromic subarray $\leq 1\  000$

# Example 1

`dorel.in`
```
xexxxdexxexaegf
4
6 8 15 3
```

`dorel.out`
```
4 2 0 3
```

## Explanation

Answers to the 4 questions

$X$ = `xexxegf`, $Y$ = `xdexxexa`.
Common palindromic subarray = `exxe` having length = $4$

$X$ = `xexxexaegf`, $Y$ = `xdexx`
Common palindromic subarray = `xx` having length = $2$

$X$ = `xexxxdexxexae`, $Y$ = `gf`
Common palindromic subarray = ` ` having length = $0$

$X$ = `xdexxexaegf`, $Y$ = `xexx`
Common palindromic subarray = `xex` having length = $3$