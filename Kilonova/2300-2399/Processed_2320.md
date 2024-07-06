Ana and Bogdan are passionate about message encryption. They have studied various encryption methods. The latest algorithm they studied involves writing a word in uppercase letters of the English alphabet. Then, under this word, all its circular permutations with one position to the left are written, thus obtaining a character matrix. Arrange the lines of the matrix lexicographically, memorize the last column, and add to the end of the resulting string the line number where the initial word is located, the resulting string being called the crypt of the initial word. Analyzing the obtained character matrix, they noticed that there are submatrices with the property that in their four corners is the same character.

# Task

Write a program that reads a natural number $c$, representing the task that needs to be solved, then reads a word. The program solves the following tasks:
1. If $c=1$, the read string is an unencrypted word, the program will determine and display the crypt obtained according to the algorithm described earlier.
2. If $c=2$, the read string is a crypt, the program will determine and display the unencrypted word.
3. If $c=3$, the read string is an unencrypted word, the program will determine the character matrix obtained according to the previously described algorithm and will display the maximum number of elements in a subarray with the property that in its corners is the same character.

# Input data

The first line of the input file `criptare.in` contains the task ($1$, $2$ or $3$). The second line of the file contains a word. If the task is $1$ or $3$ the word is unencrypted, if the task is $2$ the word is a crypt.

# Output data

If the task is $1$, the first line of the output file `criptare.out` will contain the crypt of the read word. If the task is $2$ the first line will contain the unencrypted word. If the task is $3$ the first line will contain a natural number representing the maximum number of elements in a submatrix that has the same character in its corners.

# Constraints and clarifications

* $3 \leq$ the length of the word on the first line of the file $\leq 100$
* In the word matrix, rows and columns are numbered from $0$.
* If the initial string appears on multiple lines of the matrix, the first occurrence is considered to represent the initial string.
* For $20$ points, $C=1$.
* For $50$ points, $C=2$.
* For $20$ points, $C=3$.

# Example 1

`criptare.in`
```
1
ANA
```

`criptare.out`
```
NAA1
```

## Explanation

~[img1.jpg|width=40em]

# Example 2

`criptare.in`
```
2
NAA1
```

`criptare.out`
```
ANA
```

# Example 3

`criptare.in`
```
3
MERE
```

`criptare.out`
```
6
```

## Explanation

~[img2.jpg|width=40em]