
# Task

We are given a matrix with $n$ rows and $n$ columns. The elements are characters (uppercase or lowercase letters of the alphabet). We are also given $k$ words and we must determine for each if it is present in the matrix (either on a row - arranged as a sequence from left to right, or on a column, arranged as a sequence from top to bottom).

# Input data

The file `rebus.in` contains on the first line the number $n$. Each of the following $n$ lines contains $n$ characters. The next line contains the number $k$. The following $k$ lines each contain one word.

# Output data

The file `rebus.out` contains a line with $k$ characters, each being $0$ or $1$ (for each word in the order they appear in the input, write $0$ if it does not appear in the matrix and $1$ if it does).

# Constraints and clarifications

* $1 \leq n \leq 500$;
* $1 \leq k \leq 10 \ 000$;
* The match is not case sensitive (the letter $a$ and the letter $A$ are considered identical);
* The words given have a maximum length of $500$.

# Example

`rebus.in`
```
4
Abcd
Xyzt
Mnop
aaaa
4
Xm
cza
pon
nop
```

`rebus.out`
```
1001
```
