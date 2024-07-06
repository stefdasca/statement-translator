For the given text, here is the translation according to specified instructions:

---

To heal his wound caused by the Black Beardless, Prince Algorel needs the miraculous remedy held by the witch in the dark forest.

She promised him the remedy if he solves the following problem, which she has been thinking about in vain for a thousand years: starting from two initial words $A_1$ and $A_2$ and applying the "bifo formula" $A_n = A_{n-2} \cdot A_{n-1}$ for $n \geq 3$, the words $A_3, A_4, A_5$, and so on are obtained. By $A_{n-2} \cdot A_{n-1}$ we understand the concatenation of the words $A_{n-2}$ and $A_{n-1}$ in this order. All these words ($A_1, A_2, A_3, A_4, A_5$, and so on) are in turn concatenated, in order, forming an infinite string of characters called the __magic string__. The formula of the miraculous remedy has $M$ characters, which the witch does not know. However, the $M$ positions in the magic string where the formula characters appear, in order, are known.

# Task

With all his intelligence, Algorel cannot solve this problem. Help the prince get out of trouble by finding the formula for the magical remedy.

# Input data

The first two lines of the file `bifo.in` each contain a string of at most $100$ characters representing the words $A_1$ (the first line) and $A_2$ (the second line). The third line contains an integer $M$, representing the number of characters in the formula of the miraculous remedy. The next $M$ lines contain, in order, the positions in the magic string where the characters of the formula are found.

# Output data

The output file `bifo.out` will contain on the first line a string of $M$ characters representing the formula of the miraculous remedy.

# Constraints and clarifications

* $1 \leq M \leq 100$
* $A_1$ and $A_2$ contain only lowercase letters of the English alphabet
* The numbering of positions in the infinite string starts with $1$
* The $M$ positions will be integers (not necessarily distinct) of up to $100$ digits
* For $60\%$ of the tests, the positions will be integers between $1$ and $1\ 000\ 000\ 000$
* Each line in the input and output files ends with a newline character

# Example

`bifo.in`
```
ab
cdx
3
10
4
15
```

`bifo.out`
```
xdb
```

# Explanation

The first $5$ strings obtained using the "bifo formula" are: $ab, cdx, abcdx, cdxabcdx, abcdxcdxabcdx$

Concatenating these strings results in the magic string: $abcdxabcdxcdxabcdxabcdxcdxabcdx$...

---

Please double-check the text for completeness and potential translation errors.