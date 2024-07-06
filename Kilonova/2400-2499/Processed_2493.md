Mihaela enjoys matrix multiplication. Sometimes, her brother tampers with the result of the multiplication: adding or subtracting $1$ from one of the matrix elements. She has created a randomized program with complexity $O(n^2)$ that checks if her brother has tampered with the result.

# Task

So far, the program worked, but Mihaela's brother played a prank and obfuscated the code. Help Mihaela fix the program. It can be found [here](yzzid.cpp) or on the right side of the page under "Attachments".

# Input data

We read from the keyboard $n$, the size of the square matrices. Then, we read matrices $A$, $B$, and $C$, all of size $n \times n$.

# Output data

Print `1` on the screen if $A$ multiplied by $B$ is equal to $C$. Otherwise, print `0`.

# Constraints and clarifications

* $2 \leq n \leq 1\ 800$
* The elements of matrices $A$ and $B$ are integers from the interval $[-30, 30]$.
* It is guaranteed that $C$ is either the result of matrix multiplication or the result where one element has been added $1$ or subtracted $1$.

# Example 1

`stdin`
```
3
-6 22 -27
-29 29 -30
17 -15 27
-8 -14 24
9 5 1
13 15 -17
-105 -211 337
103 101 -157
80 92 -66
```

`stdout`
```
1
```

## Explanation

The third matrix is the product of the first two.

# Example 2

`stdin`
```
3
-6 22 -27
-29 29 -30
17 -15 27
-8 -14 24
9 5 1
13 15 -17
-105 -211 337
103 101 -157
80 92 -67
```

`stdout`
```
0
```

## Explanation

The last element of the result has been subtracted by $1$.