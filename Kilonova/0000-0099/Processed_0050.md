
An amateur cryptologist proposes to build an encryption machine that encrypts a text composed of exactly $N$ distinct symbols. The encryption is done by permuting the symbols that form the text.

Our cryptologist wants the reconstruction of the initial text to be possible by passing the encrypted text through the encryption procedure $K - 1$ more times. In other words, if the text resulting from the first encryption is encrypted again, the result is encrypted again and so on, starting from the initial text and applying a total of $K$ successive encryption operations, the initial text should be obtained.

Our cryptologist wants to find out, knowing $N$ and $K$, the number of distinct ways in which the encryption machine can be built. Two ways of building the machine differ if, there exists at least one text, after the encryption of which, in the two resulting texts, there is at least one position where different symbols are found.

# Task
Write a program that determines the remainder of the division of the number of distinct ways in which the encryption machine can be built by $19\ 997$.

# Input data
The file `cifru.in` contains a single line with two natural numerical values separated by a space, $N$ and $K$ (with the meaning from the statement).

# Output data
The file `cifru.out` will contain on the first line, the number of distinct ways to build the encryption machine modulo $19\ 997$.

# Constraints and clarifications
* $1 \leq N \leq 2\ 000$
* $2 \leq K \leq 1\ 000\ 000\ 000$
* for $30\%$ of the tests $N, K < 13$
* for $50\%$ of the tests $N, K \leq 100$

# Examples

`cifru.in`
```
3 3
```

`cifru.out`
```
3
```

`cifru.in`
```
9 6
```

`cifru.out`
```
11560
```

`cifru.in`
```
100 200
```

`cifru.out`
```
13767
```