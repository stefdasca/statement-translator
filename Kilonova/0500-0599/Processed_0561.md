
Ștefan, after reading the book *Gödel, Escher, Bach: an Eternal Golden Braid* by Douglas Hofstadter, wanted to implement the "Figure-Figure" sequences as a challenge.\\

The two sequences are defined as follows:
$R(1) = 1;\\ S(1) = 2$
$R(n) = R(n-1) + S(n-1)$

The sequence $S(n)$ is the strictly increasing sequence of natural numbers that do not appear in $R(n)$. The two sequences are complementary.

# Task
Since the last time he wrote a program with mutual recursion it had errors, this time he tried to adapt a code from the *Rosetta Code* wiki. However, something did not go according to plan...

[Here](recursivitate.cpp) (or in the "Attachments" section on the side) you can find the program written by Ștefan. Your task is to make it work properly.

# Input data
The terminal will contain $n$, a natural number less than or equal to $1\ 000$.

# Output data
The terminal will contain on 2 lines the sequence $R(n)$, respectively $S(n)$, following the format described in the example below.

# Example
`stdin`
```
20
```
`stdout`
```
R(20): 1 3 7 12 18 26 35 45 56 69 83 98 114 131 150 170 191 213 236 260
S(20): 2 4 5 6 8 9 10 11 13 14 15 16 17 19 20 21 22 23 24 25
```
