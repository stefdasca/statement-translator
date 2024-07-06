A specialized laboratory is studying the mutations of a pandemic virus to find the best vaccine to combat it.

*The code* of a virus is a string made up of letters (both uppercase and lowercase) of the English alphabet. We call a *mutation* of the pandemic virus a string of characters that has the same length as the virus code and contains a single position where the letter in the string is different from the letter found at that position in the pandemic virus code.

For example, for the pandemic virus with the code `abac`, the string `Bbac` is a mutation because it has the same length and differs only in the letter at the first position.

The laboratory receives a list containing the codes of several newly discovered viruses as a result of the tests.

# Task

Write a program that, given the code of the pandemic virus and the list of newly discovered virus codes, solves the following tasks:

1. Determine the number of existing mutations of the pandemic virus in the list, not necessarily distinct mutations;
2. Determine the mutation with the highest number of occurrences in the list; if there are multiple mutations with the same highest number of occurrences, the first mutation in lexicographical order will be determined.

# Input data

The input file `virus.in` contains on the first line a natural number $C$ representing the task that needs to be solved ($1$ or $2$). The second line contains the code of the pandemic virus. The third line contains a natural number $N$, representing the number of viruses in the list received by the laboratory. The next $N$ lines contain the codes of the viruses in the list, one code per line.

# Output data

The output file `virus.out` will contain a single line:

* If $C = 1$, the first line will contain a natural number representing how many elements in the list are mutations of the pandemic virus.
* If $C = 2$, the first line will contain a string of characters representing the mutation with the highest number of occurrences. If there are multiple mutations with the highest number of occurrences, the first (smallest) in lexicographical order will be displayed.

# Constraints and clarifications

* $2 \leq n \leq 50\ 000$;
* The maximum length of a virus code is $200$.
* If $a$ and $b$ are two strings of length $lg$, we say that the string $a = a_0 \ a_1 \ a_2 \dots a_{lg-1}$ is lexicographically smaller than the string $b = b_0 \ b_1 \ b_2 \dots b_{lg-1}$ if there exists a position $k \in \{ 0, 1, \dots,  lg - 1 \}$ such that $a_i = b_i$ for any $0 \leq i < k$ and $a_k < b_k$.
* In the ASCII code, the codes of uppercase letters are smaller than the codes of lowercase letters.
* For tests worth $31$ points: $C = 1$
* For other tests worth $16$ points: $C = 2, N \leq 500$ and the maximum length of a virus code is $40$.
* For other tests worth $53$ points: $C = 2$ and there are no additional restrictions

# Example 1

`virus.in`
```
1
abac
5
Abbbq
Zbac
abbC
Bac
Zbac
```

`virus.out`
```
3
```

## Explanation

The mutations are `Zbac`, `Bac` and `Zbac`.

# Example 2

`virus.in`
```
2
abcD
8
abcdD
XbcD
Xc
XbcD
XcD
XcD
Xc
ab
```

`virus.out`
```
XbcD
```

## Explanation

The mutations `XbcD` and `XcD` each appear $2$ times, the first in lexicographical order being `XbcD`. `XbcD` is lexicographically smaller than `XcD` because in the ASCII code: `A` < `B` < ... < `Z` < `a` < `b` < ... < `z`.