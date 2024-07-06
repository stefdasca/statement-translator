```markdown
Transmitting and storing information requires various encoding systems to optimize the available space. A very commonly used system associates a sequence of characters $i$ with a number.

We consider words formed only with the lowercase letters of the English alphabet $a,b,c, \\ldots, z$ ($26$ characters). From all these words, we only consider those whose characters are in strictly lexicographical order (the character at any position is strictly smaller than any following character).

The encoding system is obtained as follows:

* The words are ordered in increasing order of their lengths.
* Words of the same length are ordered lexicographically (in the alphabetical order of the words in a dictionary).
* We encode these words by numbering them starting with $a$, as follows:

$$
a \\to 1 \\\\
b \\to 2 \\\\
\\ldots \\\\
z \\to 26 \\\\
ab \\to 27 \\\\
\\ldots \\\\
az \\to 51 \\\\
bc \\to 52 \\\\
\\ldots \\\\
vwxzy \\to 83\ 681
$$

# Task

Given a word, specify whether it can be encoded according to the encoding system. If affirmative, specify its code.

# Input data

The input file `cod.in` contains a word on a line.

# Output data

The file `cod.out` will contain the code of the word that needs to be encoded, or $0$ if the word cannot be encoded.

# Constraints and clarifications

* The maximum number of letters in a word is $10$
* The number of characters in the English alphabet is $26$

# Example 1

`cod.in`
```
bf
```

`cod.out`
```
55
```

# Example 2

`cod.in`
```
aab
```

`cod.out`
```
0
```

# Example 3

`cod.in`
```
vwxyz
```

`cod.out`
```
83681
```
```