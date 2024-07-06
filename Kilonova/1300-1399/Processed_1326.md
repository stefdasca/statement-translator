# Task

Due to an unfortunate mistake, editor Vasile has deleted all spaces from the text he was working on.

The text is written in an unknown language, using only lowercase English letters. Vasile knows that a word must contain at least one vowel and cannot have a length greater than $20$ letters. Also, being a meticulous person, he knows that the text originally had (before the deletion of spaces) exactly $N$ words.

Vasile needs to restore the text, inserting spaces between words. As there are numerous ways to restore the text, Vasile decided to choose the version in which the letters are distributed among words most harmoniously. To measure harmony, Vasile calculated the sum of the squares of the lengths of the words. The text is more harmonious if the resulting sum is smaller.

# Task

Given the text without spaces, determine how many possible ways there are to restore it (in total, regardless of their harmony), as well as the most harmonious way to restore it.

# Input data

The input file `text.in` contains the text without spaces on the first line. The second line contains the natural number $N$, representing the number of words in the original text.

# Output data

The output file `text.out` will contain on the first line a natural number representing the total number of possible ways to restore the text **modulo** $1 \ 000 \ 003$ (the remainder when divided by $1 \ 000 \ 003$). On the second line, it will contain the measure of the harmony of the restored text (the minimum sum of the squares of the lengths of the words in the text). On the third line will be written the most harmonious text obtained after restoration. A single space will be written between any two consecutive words.

# Constraints and clarifications

* $0 < $ Length of string $ \leq 200$
* The vowels of the English alphabet are `a`, `e`, `i`, `o`, `u`, `y`.
* There is always a solution for the test data.
* If there are multiple optimal restoration solutions, the first variant in lexicographic order will be written (it is known that ` ` (space) $ < $ `a`).
* The string $(x_1, x_2, ..., x_n)$ is lexicographically smaller than $(y_1, y_2, ..., y_n)$ if there exists $k \ (1 \leq k \leq n)$ such that $x_i = y_i \ (\forall \ 1 \leq i \lt k)$ and $x_k < y_k$.
* For $40\%$ of the tests, the length of the text is $ \lt 70$ and $N \leq 7$.
* Scoring will be as follows: $50\%$ for the total number of restoration ways modulo $1 \ 000 \ 003$; $80\%$ for the total number of restoration ways modulo $1 \ 000 \ 003$ and the minimum sum; $100\%$ for correctly solving all requirements.

# Example

`text.in`
```
bcaeiouxtz
3
```

`text.out`
```
6
34
bca eio uxtz
```

## Explanation

The possible restorations are:
`bca eio uxtz` (harmony: $9 + 9 + 16 = 34$)
`bca ei ouxtz` (harmony: $9 + 4 + 25 = 38$)
`bca e iouxtz` (harmony: $9 + 1 + 36 = 46$)
`bcae io uxtz` (harmony: $16 + 4 + 16 = 36$)
`bcae i ouxtz` (harmony: $16 + 1 + 25 = 42$)
`bcaei o uxtz` (harmony: $25 + 1 + 16 = 42$)
The most harmonious variant is `bca eio uxtz`