It is considered the English alphabet composed of lowercase letters, from `a` to `z`.

A **word** is a finite, possibly empty, sequence of letters from this alphabet.

A **pattern expression** is a string of characters from the alphabet in which the characters `?` and `*` can also appear.

A word matches a pattern expression if it can be obtained from it as follows:

* The character `?` is replaced with a single letter from the alphabet
* The character `*` is replaced with any word, possibly empty
* From the pattern expression, before performing the replacements of characters `?` and `*`, a single letter character can be removed or not.

# Task

Given a pattern expression and a sequence of words, determine, for each word separately, whether it matches the given pattern expression or not.

# Input data

The input file `sablon.in` contains:
The first line contains a pattern expression $E$.
The second line contains a natural number $N$, representing the number of words in the sequence.
Each of the next $N$ lines contains one word $S_{i}$ ($1 \leq i \leq N$).

# Output data

The output file `sablon.out` will contain on each of the first $N$ lines the value $1$ or $0$, depending on whether the word $S_{i}$ ($1 \leq i \leq N$) matches the pattern expression $E$ or not.

# Constraints and clarifications

* $1 \leq n \leq 10$;
* For $16\%$ of the tests, the pattern expression $E$ does not contain the character $*$ and the length of $E$ and any word $S$ is between $1$ and $1\ 000$ characters.
* For another $16\%$ of the tests, the lengths of $E$ and $S$ are between $1$ and $20$ characters.
* For another $32\%$ of the tests, the lengths of $E$ and $S$ are between $1$ and $100$ characters.
* For the remaining $36\%$ of the tests, the lengths of $E$ and $S$ are between $1$ and $1\ 500$ characters.

# Example

`sablon.in`
```
a*a?b
7
ababb
aab
aabb
bac
abcaab
abcaab
ababa
```

`sablon.out`
```
1
1
1
0
1
1
0
```

## Explanation

The words $ababb$, $aabb$ and $abcaab$ match the pattern expression. The word $aab$ matches the pattern expression obtained by preemptively removing one of the characters 'a'. The words $bac$ and $ababa$ cannot be obtained in any way from the pattern expression.