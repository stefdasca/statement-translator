
Passionate about astronomy, Teodora wishes to keep track of the number of stars in galaxies. To make things more interesting, she encodes these numbers in her own system, transforming them into a sequence of letters and digits according to the following algorithm:
 - she denotes each power of $2$, strictly less than $2^{26}$, with a letter of the alphabet, as shown
 ~[figura_stele.png|align=center]
 - she represents each number as a sequence of digits and letters obtained by writing that number as a sum of powers of $2$; if a power is used multiple times in the decomposition of the number, it will be preceded by the number of uses in the sequence.

A number can be represented in several ways. For example, for the number 100 some of the possible representations are: 
$\texttt{100} = \texttt{cfg} = 2^2 + 2^5 + 2^6 = 4 + 32 + 64 = 100$
$\texttt{100} = \texttt{2ab2cde2f} = 2 \times 2^0 + 2^1 + 2 \times 2^2 + 2^3 + 2^4 + 2 \times 2^5 = 2 \times 1 + 2 + 2 \times 4 + 8 + 16 + 2 \times 32 = 100$
$\texttt{100} = \texttt{16bcg} = 16 \times 2^1 + 2^2 + 2^6 = 16 \times 2 + 4 + 64 = 100$

# Task

Write a program that solves the following tasks:
1. Given $s$, the number of stars in a galaxy, determine an encoded representation of this number consisting only of distinct lowercase letters ordered alphabetically;
2. Given $g$, representing the number of galaxies, and $g$ numbers in encoded writing, representing the number of stars in each galaxy, determine the decimal writing of the total number of stars in the $g$ galaxies.

# Input data

The input file `stele.in` contains the following:
- The first line contains a natural number $c$, representing the task that needs to be solved ($1$ or $2$). 
- If the task is $1$, the second line contains a natural number $s$, representing the number that needs to be encoded.
- If the task is $2$, the second line contains a natural number $g$ representing the number of galaxies, and on the following $g$ lines there is a sequence of characters representing the number of stars in a galaxy, encoded using the algorithm described above.

# Output data

The output file `stele.out` will contain a single line that will either contain a sequence of distinct lowercase letters, ordered alphabetically, representing the encoded writing of the number $s$ (if the task is $1$), or a natural number in decimal writing representing the total number of stars in the $g$ galaxies (if the task is $2$).

# Constraints and clarifications

* $1 \leq s \leq 2^{26} - 1$
* $1 \leq g \leq 1\ 000$
* Encoded representations in the input file can have a maximum of $420$ characters.
* The number that can appear in front of a letter can have a maximum of $15$ digits.
* For tests worth $30\%$ of the score, the task is $1$.
* For tests corresponding to task $2$ worth $20\%$ of the score, the obtained value does not exceed $10^{18}$.

# Example 1

`stele.in`
```
1
100
```

`stele.out`
```
cfg
```

## Explanation

The task is $1$. The representation of the number $100$ that meets the requirement is: $\texttt{cfg} = 2^2 + 2^5 + 2^6 = 4 + 32 + 64 = 100$

# Example 2

`stele.in`
```
2
5
2a7g
17b5d14g
100a2000b
7e15f
2d6f
```

`stele.out`
```
6320
```

## Explanation

The task is $2$ and we have $5$ numbers:
$\texttt{2a7g} = \texttt{450}$
$\texttt{17b5d14g} = \texttt{970}$
$\texttt{100a2000b} = \texttt{4100}$
$\texttt{7e15f} = \texttt{592}$
$\texttt{2d6f} = \texttt{208}$
Their sum is: $450 + 970 + 4100 + 592 + 208 = 6320$
