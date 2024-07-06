The file content in English after translation while preserving mathematical values, variable names, general syntax, structure, and format is as follows:

---

Given $S = (S_1, S_2, \dots, S_N$) a sequence consisting of $N$ natural numbers less than $10$ and $x$ a natural number with $p$ digits, represented in base $10$ by $x$ = $x_1 x_2 \dots x_p$. Note that the positions in the sequence $S$ are numbered from left to right from $1$ to $N$, and the digits of the number $x$ are numbered from left to right from $1$ to $p$ (the digit $p$ being the units digit).

We will say that $x$ **appears as a subsequence** in the sequence $S$ if there exist positions $1 \leq j_1 < j_2 < \dots < j_p \leq N$ such that $S_{j_i} = x_i$ for any $1 \leq i \leq p$. For example, for $S=(2,3,7,9)$, $27$ appears as a subsequence in $S$, but $93$ does not appear as a subsequence in $S$.

We call the **length prefix** $j$ of $S$, the sequence $S_1, S_2, \dots, S_j$ (the sequence that starts at position $1$ and ends at position $j$).

# Task

Write a program that, knowing the sequence $S$, solves the following two requirements:
1. given $Nr$ pairs of the form $x \ j$, determine for each pair if the number $x$ appears as a subsequence in the length prefix $j$ of $S$ and display the value $1$ if affirmative, otherwise the value $0$;
2. given $Nr$ pairs of the form $a \ b$, determine and display for each pair the number of natural numbers in the closed interval $[a, b]$ that appear as a subsequence in the sequence $S$.

# Input data

The input file `subsir.in` contains on the first line a natural number $C$ which represents the requirement to be solved ($1$ or $2$). The second line contains the natural number $N$. The third line contains $N$ natural numbers less than $10$, $S_1, S_2, \leq, S_N$, representing the elements of the sequence $S$. On the fourth line contains a natural number $Nr$ which represents the number of pairs. The next $Nr$ lines contain one pair of natural numbers each. The numbers written on the same line in the input file are separated by a space.

# Output data

The output file `subsir.out` will contain $Nr$ lines, on the $i$-th line containing the result for the $i$-th pair among the $Nr$ pairs in the input file, according to requirement $C$.

# Constraints and clarifications

* $1 \leq N \leq 10 \ 000$;
* $1 \leq Nr \leq 10 \ 000$;
* $0 \leq x < 10^7$;
* $1 \leq j \leq N$;
* $0 \leq a \leq b < 10^7$;
* For tests worth $30$ points, the requirement is $1$.
* For tests worth $70$ points, the requirement is $2$.

# Example 1

`subsir.in`
```
1
10
5 6 1 0 3 2 5 2 3 1
5
1 4
1 2
153 6
153 9
72 8
```

`subsir.out`
```
1
0
0
1
0
```

## Explanation

The requirement is $1$, so we need to check for each of the $Nr=5$ pairs $x \ j$ specified whether $x$ appears as a subsequence in the length prefix $j$ of $S$.
The first pair is $1 \ 4$. The number $1$ appears as a subsequence in the prefix $5 \ 6 \ 1 \ 0$, so we print $1$.
The second pair is $1 \ 2$. The number $1$ does not appear as a subsequence in the prefix $5 \ 6$, so we print $0$.
The third pair is $153 \ 6$. The number $153$ does not appear in the prefix $5 \ 6 \ 1 \ 0 \ 3 \ 2$, so $0$ will be printed.
The fourth pair is $153 \ 9$. This time the number $153$ appears as a subsequence in the prefix $5 \ 6 \ 1 \ 0 \ 3 \ 2 \ 5 \ 2 \ 3$, so $1$ will be printed.
The fifth pair is $72 \ 8$. The number $72$ does not appear as a subsequence in any prefix of $S$, so neither in the length $8$ one and $0$ will be printed.

# Example 2

`subsir.in`
```
2
10
5 6 1 0 3 2 5 2 3 1
3
0 20
40 105
81 99
```

`subsir.out`
```
11
15
0
```

## Explanation

The requirement is $2$, so we need to determine for each of the $Nr = 3$ pairs $a \ b$ specified how many natural numbers in the interval $[a, b]$ appear as subsequences in $S$.
For the interval $[0, 20]$ there are $11$ numbers, these being $0, 1, 2, 3, 5, 6, 10, 11, 12, 13, 15$.
For the interval $[40, 105]$ there are $15$ numbers, these being $50, 51, 52, 53, 55, 56, 60, 61, 62, 63, 65, 101, 102, 103, 105$.
For the interval $[81, 99]$ the answer is $0$, because there is no number in this interval that is a subsequence of $S$.

---

Please review for any potential grammar and syntax errors according to the rules of the English language.