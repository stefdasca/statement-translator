~[goe.png|align=right]
Goe is a cute but very lazy child. He doesn't like either writing or counting. His mother had a hard time convincing him to learn the numbers, but he still can't write all of them. He doesn't like the digits $2$, $4$, $5$, and $7$, and he confuses the digit $6$ with $9$, and vice versa. And that's not all. When his mother gives him numbers to copy, to practice writing the digits, he writes them in reverse order. For instance, the number $138$ will be written by Goe as $831$.
Goe's mother writes every day, in ascending order, $9$ natural numbers, but skipping any number divisible by $10$, as shown in $Figure \\ 1$.
Goe copies these numbers every day. Unfortunately, he doesn't correct any of his mistakes: he writes the numbers in reverse order, does not write numbers that contain the digits $2$, $4$, $5$, and $7$, and continues to confuse the digit $6$ with $9$ and vice versa (see $Figure \\ 2$).

# Task

Write a program that reads the non-zero natural numbers $k$, $p$, and $n$, and determines:

1. The number of numbers written by Goe in the first $k$ days;
2. The $p^{th}$ correctly written palindrome by Goe; a number is a palindrome if it is equal to its mirror image;
3. The largest number written by Goe in the first $n$ days.

# Input data

The file `goe.in` contains a single line that contains three natural numbers $k$, $p$, and $n$, separated by a space.

# Output data

The output file `goe.out` will contain $3$ lines:

* The first line will contain the number of numbers written by Goe in the first $k$ days;
* The second line will contain a natural number representing the $p^{th}$ correctly written palindrome by Goe;
* The third line will contain the largest number written by Goe in the first $n$ days.

# Constraints and clarifications

* $1 \leq k \leq 100 \ 000$
* $1 \leq p \leq 750$
* $1 \leq n \leq 32 \ 000 \ 000$
* Solving task $1$ earns $40\%$ of the points, task $2$ earns $30\%$ of the points, and task $3$ earns $30\%$ of the points.

# Example

`goe.in`
```
5 8 3
```

`goe.out`
```
15
111
91
```

## Explanation

$15$ numbers were written by Goe in the first $5$ days.
The first $8$ correctly written palindromes by Goe are: $1$, $3$, $8$, $11$, $33$, $88$, $101$, $111$.
The largest number written by Goe in the first $3$ days is $91$.