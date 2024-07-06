We have a text composed of lowercase English alphabet letters and spaces. In the text, words are separated by one or more spaces. Each letter in the alphabet is associated with a number representing its position in the alphabet. Thus, `a` is associated with the number $1$, `b` with the number $2$, `c` with the number $3$, and so on. Using this association, we define the *degree* of a word as the sum of the numbers associated with each letter. For example, the word `bac` has a *degree* of $2+1+3=6$.

Using the words of a text, we can form groups of words. Two words belong to the same group if they have the same *degree*.

# Task

Write a program that, for a given text, determines the number of words and the number of groups.

# Input data

The input file `grad.in` will contain on the first line a natural number $n$ representing the number of characters in the text, and on the second line the text.

# Output data

The output file `grad.out` will contain on the first line the number of words, and on the second line the number of groups.

# Constraints and clarifications

* $1 \leq n < 255$
* The text contains at least one word.
* The first and last character in the text is a letter.
* Correct determination of the number of words earns $30\%$ of the score. Correct determination of both values earns $100\%$ of the score.

# Example

`grad.in`
```
17
bac daca aaac bbb
```

`grad.out`
```
4
2
```

## Explanation

The text contains $4$ words and two groups.
The first group is formed by the words `bac`, `aaac`, and `bbb`, each having a *degree* of $6$.
The second group contains only the word `daca`, with a *degree* of $9$.