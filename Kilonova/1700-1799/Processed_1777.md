Inspiration drawn from the infamous Al-Qaeda, the terrorists from the city of Tomis have decided to sabotage the National Informatics Olympiad. To carry out their plan, they kidnapped Miruna and sent a letter to the contestants demanding a very large ransom. As a precautionary measure, the letter was not handwritten; instead, it was composed by pasting letters cut out from a newspaper. Detective Mirunel has a plan to identify the terrorists. The first thing Mirunel wants to do is to demonstrate that the terrorists read _Dilema veche_. The detective has the latest issue of the magazine and wants to know if the terrorist letter could have been written by cutting out letters only from this issue. Unfortunately, this task is too difficult for Mirunel because when a piece is cut out from a newspaper, it contains $2$ letters, one on each side. Each newspaper piece can be used in two ways, depending on the letter that will be used to reconstruct the sent letter, and this completely confused Mirunel.

# Task

Write a program to determine a valid way to reconstruct the letter sent by the terrorists using only the newspaper pieces cut out by Mirunel.

# Input data

The input file `teroristi.in` contains on the first line two natural numbers $n$ and $m$, representing the length of the letter sent by the terrorists and the number of newspaper pieces cut out, respectively. The second line contains the letter message in the form of a string of $n$ lowercase letters from the English alphabet. Each of the following $m$ lines contains exactly $2$ characters from the English alphabet separated by a space, representing the letters written on the two sides of a newspaper piece.

# Output data

The output file `teroristi.out` will contain a single line with a string of $n$ distinct numbers from the set $\{1, 2, \dots, m \}$. At position $i$ in the displayed string, the index of the newspaper piece (in the order they appear in the input file) used to represent the $i$-th letter of the letter will be found.

# Constraints and clarifications

* $1 \leq n \leq 1\ 000\ 000$
* $n \leq m \leq 1\ 000\ 000$
* For $10\%$ of tests $n, m = 3$
* For another $10\%$ of tests $n, m \leq 15$
* For another $30\%$ of tests $n, m \leq 1\ 000$
* If there are multiple solutions, any of them can be displayed.
* It is guaranteed that there is always a solution in the test data.

# Example 1

`teroristi.in`
```
6 8
miruna
b a
m i
f a
u g
f m
a g
b r
n a
```

`teroristi.out`
```
5 2 7 4 8 3
```

## Explanation

The following pieces will be used:

$5$ – `f m`
$2$ – `m i`
$7$ – `b r`
$4$ – `u g`
$8$ – `n a`
$3$ – `f a