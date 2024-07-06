Alecu is a mischievous child who breaks everything. He wrote a word on a sheet of paper. Being a first-grade student, he has only learned the first $X$ lowercase letters of the English alphabet, and the word on the sheet is written using only these letters.

He plans to cut the sheet into multiple pieces but wants to obtain only words with the same number of letters and at the same time, all obtained words from the cutting should be palindromes. A word is a palindrome if it reads the same from left to right as it does from right to left. An example of a palindrome is the word `abcba`.

In order to obtain only palindrome words after cutting, Alecu can change any letter of the word to any other letter he knows, but each such change has a known cost. Moreover, a letter in the initial word can be changed at most once.

We denote by $Nr(c)$ the minimum number of palindromes of equal lengths into which the word on the sheet can be cut, allowed to change letters but not exceeding a total cost greater than $c$. Alecu knows how to determine the value $Nr(c)$ for any natural number $c$.

# Task

Write a program that for a natural number $Q$ and the sequence of natural numbers $0$, $1$, $2$, $ \\dots $, $Q - 1$, $Q$, determines the sum: $Nr(0)$ + $Nr(1)$ + $Nr(2)$+ $ \\dots $ + $Nr(Q - 1)$ + $Nr(Q)$.

# Input data

In the file `kpal.in` the first line contains the natural number $X$. The next $X$ lines contain $X$ numbers each. For all these lines, the $j$-th number on the $i$-th line represents the cost of transforming the $i$-th letter into the $j$-th letter of the English alphabet ($cost_{ij}$).

On line $X + 2$ contains a string of English alphabet letters, representing the word initially written on the sheet. The last line of the file contains the natural number $Q$.

# Output data

The file `kpal.out` will contain on the first line a natural number representing the determined sum.

# Constraints and clarifications

* $1 \leq$ the length of the word $\leq 100\ 000$, and the word contains only lowercase letters;
* $1 \leq X \leq 26$;
* $0 \leq Q \leq 1\ 000\ 000\ 000$;
* $1 \leq cost_{ij} \leq 10\ 000$, where $1 \leq i, j \leq X$ and $i \neq j$;
* $cost_{ii} = 0$, where $1 \leq i \leq X$;
* If the initial word is a palindrome, then we consider it was obtained also from a cut;

# Example 1

`kpal.in`
```
3
0 1 2
3 0 2
3 8 0
aabbbc
3
```

`kpal.out`
```
16
```

## Explanation

For a maximum cost of $0$, there is a partition into $6$ palindromes; $Nr(0) = 6$;
For a maximum cost of $1$, there is a partition into $6$ palindromes; $Nr(1) = 6$;
For a maximum cost of $2$, there is a partition into $3$ palindromes by changing the last $b$ into $c$; $Nr(2) = 3$;
For a maximum cost of $3$, there is a partition into $1$ palindrome by changing the first $a$ into $c$ and the second $a$ into $b$; $Nr(3) = 1$;
The total sum $Nr(0)$ + $Nr(1)$ + $Nr(2)$ + $Nr(3)$ = $6$ + $6$ + $3$ + $1$ = $16$.

# Example 2

`kpal.in`
```
2
0 1
3 0
aabbaa
2
```

`kpal.out`
```
3
```

## Explanation

For a maximum cost of $0$, there is a partition into $1$ palindrome; $Nr(0) = 1$;
For a maximum cost of $1$, there is a partition into $1$ palindrome; $Nr(1) = 1$;
For a maximum cost of $2$, there is a partition into $1$ palindrome; $Nr(2) = 1$;
The total sum $Nr(0)$ + $Nr(1)$ + $Nr(2)$ = $1$ + $1$ + $1$ = $3$.