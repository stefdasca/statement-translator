For a string $S$, we denote by $lmax[S]$ the maximum length of a palindromic subsequence contained in the string $S$. Thus, for the string `S = abAabaabC`, $lmax[S]=4$, and for the string `S = a`, $lmax[S]=1$. By the palindromic subsequence of a string $S$ we mean a subsequence of characters on consecutive positions that form a palindrome.

# Task

Given $N$ strings $S_{1}, S_{2}, \ldots, S_{n}$ and a natural value $L$, determine the number of string subsequences of the form: $S_{i}, S_{i+1}, \ldots, S_{j}$, with $i \leq j$, for which $lmax[S_{i}]+lmax[S_{i+1}]+ \cdots +lmax[S_{j}]=L$.

# Input data

The input file `secvpal.in` contains:
- The first line contains two natural numbers $N$, $L$ as described above.
- Each of the next $N$ lines contains a string.

# Output data

The output file `secvpal.out` will contain on a single line a natural number nr that represents the number of string subsequences that satisfy the given condition.

# Constraints and clarifications

* $2 \leq N \leq 50\ 000$;
* $0 \leq nr \leq 10\ 000$;
* $1 \leq$ maximum length of any string $S_{i} \leq 10\ 000$, $1 \leq i \leq N$;
* $1 \leq$ maximum length of a palindromic subsequence **lmax($S_{i}$)** $\leq 1\ 000$;
* $1 \leq (\text{maximum length of string } S_{i}) \times N \leq 1\ 000\ 000$;
* The $N$ strings contain only the characters `A`..`Z`, `a`..`z`;
* A **palindrome** is a string that reads the same from left to right or from right to left.

# Example 1

`secvpal.in`
```
5 11
aCCACCACaBa
AAPAPAACCAA
acaacc
capac
CACAACAACACCAACP
```

`secvpal.out`
```
2
```

## Explanation

1. $lmax(\text{â€œaCCACCACaBaâ€})=6$
2. $lmax(\text{â€œAAPAPAACCAAâ€})=7$
3. $lmax(\text{â€œacaaccâ€})=4$
4. $lmax(\text{â€œcapacâ€})=5$
5. $lmax(\text{â€œCACAACAACACCAACPâ€})=11$

The two subsequences with length $11$ are: $2,3$ and $5$