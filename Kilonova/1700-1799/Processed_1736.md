```markdown
A sentence consisting of lowercase English alphabet letters and possibly spaces is given. Words are formed only from letters and are separated by one or more spaces.

We define the **associated number** of a word $c_1 c_2 \dots c_k$ as a natural number $n_c$, obtained as the product of positions in the alphabet of the letter $c_i$. Thus, the word `badab` is associated with the number $n_c = 2^1 \cdot 1^2 \cdot 4^3 \cdot 1^4 \cdot 2^5$, i.e., $n_c = 4\ 096$.

We define the **degree of a word** $c_1 c_2 \dots c_k$ as the number $nr$ modulo $k$, where $nr$ is the number of divisors of $n_c$. The degree of the word `badab` is $3$, because $nr = 13$ (the $13$ divisors of $4\ 096$ are: $1$, $2$, $4$, $8$, $16$, $32$, $64$, $128$, $256$, $512$, $1024$, $2048$ and $4096$), $k = 5$ (the word contains $5$ letters) and $13$ modulo $5$ = $3$.

We define the **degree of a sentence** as the sum of the degrees of the words in it.

# Task

Write a program that, for a given sentence, determines its degree.

# Input data

The input file `grad.in` will contain a sentence on the first line.

# Output data

The output file `grad.out` will contain the degree of the sentence on the first line.

# Constraints and clarifications

* The sentence has at most $255$ characters.
* The sentence starts and ends with a letter and is followed by a newline character.
* $n$ modulo $k$ means the remainder of dividing $n$ by $k$.
* In the alphabet, the letter `a` is in position $1`, `b` is in position $2`, and so on.

# Example

`grad.in`
```
de   badab
```

`grad.out`
```
4
```

## Explanation

The degree of the word `de` is $1$, and the degree of the word `badab` is $3$, so the degree of the read sentence will be $1 + 3 = 4$.
```

I have translated the competitive programming problem statement from Romanian to English, while preserving the mathematical values, variable names, general syntax, structure, and format, as well as the custom image format. I also fixed potential grammar and syntax errors according to the rules of the English language. Please double-check the translation for accuracy.
