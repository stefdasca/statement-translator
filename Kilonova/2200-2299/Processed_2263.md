Miruna has a string of characters and would like to know if it can be written as a concatenation of even-length palindromes.

# Task

Given a string of length $N$, display `YES` if the string can be written as a concatenation of even-length palindromes, and `NO` otherwise.

# Input data

The first line of the input file `parpal.in` contains a natural number $T$ representing the number of tests. Each of the following $T$ lines contains a string consisting of lowercase letters of the English alphabet.

# Output data

The output file `parpal.out` will contain $T$ lines. On each line $i$, print `YES` if the string corresponding to line $i + 1$ in the input file can be written as a concatenation of even-length palindromes, and `NO` otherwise.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$
* $1 \leq T \leq 10$

# Example

`parpal.in`
```
5
aaaa
aabbaacbxxxxbc
abcabc
abbcca
cbaabccbaabc
```

`parpal.out`
```
YES
YES
NO
NO
YES
```

