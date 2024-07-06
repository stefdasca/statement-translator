A word formed from lowercase letters of the English alphabet is a palindrome if reading it from left to right or from right to left gives the same word. For example, `ghihg` or `lool` are palindromes.
Let's consider a string formed only from lowercase letters of the English alphabet. In this string, spaces can be occasionally inserted such that it transforms into a text containing only palindrome words. For example, `abbbabaca` can be split into palindrome words in multiple ways, of which we exemplify all decompositions into $5$ palindromes in lexicographic order:
1. `a b b bab aca`
2. `a bbb a b aca`
3. `a bbb aba c a`
4. `abbba b a c a`

Let's consider all decompositions of a string into exactly $p$ palindromes, the solutions obtained being arranged in lexicographic order. The character ` ` (space) is smaller than any letter.

# Task

Given a string of lowercase letters and two natural numbers $p$ and $q$, determine the decomposition with the order number $q$ from the set of all lexicographically ordered solutions formed from $p$ palindromes.

# Input data

The input file `ppal.in` contains on the first line the natural number $n$. The second line contains a string of $n$ lowercase letters of the English alphabet. Starting from the $3$rd line until the end of the file, each line contains a pair of natural numbers $p$ and $q` separated by a space.

# Output data

The output file `ppal.out` will contain for each pair of numbers $p \ q$ from the input file a line on which the decomposition with the order number $q$ from the set of all solutions formed from $p$ palindromes, arranged lexicographically, or $0$ (zero) if the solution with the order number $q$ does not exist.

# Constraints and clarifications

* $0 < p \leq n \leq 500$
* $0 < q \leq 999 \ 999 \ 999 \ 999 \ 999 \ 999$
* The maximum number of pairs $p \ q$ will not exceed $250 \ 000$

# Example

`ppal.in`
```
9
abbbabaca
5 3
5 1
5 5
3 1
3 2
```

`ppal.out`
```
a bbb aba c a
a b b bab aca
0
abbba b aca
0
```

## Explanation

The third decomposition from the previous example  
The first decomposition from the previous example  
There are no $5$ solutions, so $0$ is written  
There is a single decomposition of $3$ palindromes  
The second solution does not exist, so $0$ is written