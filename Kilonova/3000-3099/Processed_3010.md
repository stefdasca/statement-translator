Given a string $S$ consisting of uppercase and lowercase English letters, spaces, and the character `⌂` which has the ASCII code $127$. Each character of $S$ is encoded using a sequence of $1$s and $0$s representing the ASCII code of the character in base $2$. The code starts with the digit $1$, so for the character `A` the encoding is $1000001$. A word can be formed from letters and the character `⌂`. Consider the matrix $M$ made up of the words from the string $S$ encoded and stored on separate lines in the order in which they appear in the sentence.

# Task

Write a program that, given $S$ and $K$, solves the following two tasks:
1. Determine $L$, the side of the largest square in the matrix $M$ that contains only values of $1$.
2. Determine $NR$, how many squares of side $K$ with all elements equal to $1$ exist in the matrix $M$.

# Input data

The input file `asciimat.in` contains on the first line the task that needs to be solved ($1$ or $2$). The second line contains the string $S$, and the third line contains the value $K$, having the significance from the statement.

# Output data

If the task is $1$, the output file `asciimat.out` will contain a single line on which $L$ will be written, the side of the largest square in the matrix $M$ that contains only values of $1$.
If the task is $2$, the output file `asciimat.out` will contain a single line on which $NR$ will be written, how many squares of side $K$ with all elements equal to $1$ exist in the matrix $M$.

# Constraints and clarifications

* The string $S$ has at most $3000$ characters
* $3 \leq K \leq 50$
* The length of a word does not exceed $100$ characters
* Each word is encoded on a single line
* Each letter is encoded on $7$ bits
* The lines contain the concatenation of ASCII codes of the letters of a word, so the remaining free values of a line will have the value $0$.
* The number of words in the string does not exceed the value $300$
* For tests worth $40$ points the task is $1$
* For tests worth $50$ points the task is $2$
* $10$ points are awarded by default

# Example 1

`asciimat.in`
```
1
Ana are mere
3
```

`asciimat.out`
```
3
```

# Example 2

`asciimat.in`
```
2
Ana are mere
2
```

`asciimat.out`
```
7
```

## Explanation

The resulting matrix is:
```
1000001110111011000010000000
1100001111001011001010000000
1101101110010111100101100101
```

At position $(1,8)$ in the matrix is the top-left corner of a square with side $3$ with all elements equal to $1$.
There are $7$ squares of side $2$ with all elements equal to $1$.