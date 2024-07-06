Alex received a very interesting game from Santa Claus. The game consists of a text with $n$ lowercase letters of the English alphabet. Each letter has a specific power, given by a natural number. The power $k$ of a letter $c$ means that if it is touched, all the letters in a subarray of $k$ letters, on the left and right, are transformed into $c$. For example, if the letter $x$ has the power $2$, then after being touched, the text $\text{abcbxpbrr}$ is transformed into $\text{abxxxxxrr}$. Knowing the power of each letter, the game is to determine the maximum number $m$ of letters, which after being touched, will transform any letter in the text at most once.

# Task

Write a program that reads a text with $n$ letters, the power of each letter, and displays the number of letters in the text with the maximum power, denoted by $q$, as well as the number $m$.

# Input data

In the input file `char.in` there are:
* The first line contains the natural number $n$
* The second line contains the $n$ letters of the text without spaces between them
* The third line contains the number $h$ of distinct letters in the text
* The fourth line contains $h$ natural numbers separated by a space, representing the power of the letters in alphabetical order.

# Output data

The output file `char.out` will contain:
* The first line contains the number $q$
* The second line contains the number $m$.

# Constraints and clarifications

* $1 \leq n \leq 10 \ 000$
* $1 \leq \text{letter power} \leq 100$
* If there are fewer letters on the left or right of a letter than its power, then touching it leads to the transformation of all the letters on the left or right, respectively.
* $30\%$ of the score is awarded for determining the number $q$ and $70\%$ for determining the number $m$.
* The first letter in the text is at position $1$, the second letter at position $2$, and so on.

# Example

`char.in`
```
12
acbbxacbbbxb
4
2 5 3 2
```

`char.out`
```
6
3
```

## Explanation

The letter `a` has the power $2$, the letter `b` has the power $5$, the letter `c` has the power $3$, and the letter `x` has the power $2$. The letter with the maximum power is `b` and it appears in the sequence 6 times. The maximum number of letters that can be touched such that any letter in the text is transformed at most once is $3$ (for example, letters at positions $1$, $6$, $11$ can be touched).

~[game_example.png]