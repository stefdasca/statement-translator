Green and Riemann are two good friends who like to play a game called "enigma." In this game, one of them writes a word consisting of $N$ characters, and the other comes up with $M$ words of at most $S$ characters. The goal of the second player is to figure out how many ways the first word can be formed by concatenating prefixes of some of the $M$ words.
If a way to form the first word is found, then each position $i$ of the word will be associated with a pair $(x, y)$, indicating that position $i$ is covered by the $y$-th character of the $x$-th word. Thus, two ways of forming the first word are considered different if there are two positions $i$ and $j$, with associated pairs $(x_1, y_1)$ and $(x_2, y_2)$ such that $x_1\neq x_2$ or $y_1\neq y_2$.

# Task

Create a program to solve the game "enigma"!

# Input data

The input file `enigma.in` will contain on the first line two numbers $N$ and $M$ with the significance from the statement. The second line will contain the first word consisting of $N$ characters. The next $M$ lines will each contain a word of at most $S$ characters.

# Output data

The output file `enigma.out` will contain on the first line the number of ways in which the first word can be obtained by concatenating prefixes of some of the $M$ words, modulo $31 \ 333$.

# Constraints and clarifications

* $1 \leq N \leq 300 \ 000$
* $1 \leq M \leq 4 \ 500$
* $1 \leq S \leq 100$
* a character is defined as a lowercase letter from the English alphabet
* a word may appear multiple times
* prefixes of words can only be concatenated, not overlapped

# Example 1

`enigma.in`
```
7 3
xxxabdc
xxx
abdc
c
```

`enigma.out`
```
8
```

## Explanation

Considering the numbering of the words from the input file, the pairs associated with the positions of the first word are:

1. $(1, 1) \ (1, 1) \ (1, 1) \ (2, 1) \ (2, 2) \ (2, 3) \ (2, 4)$;
2. $(1, 1) \ (1, 2) \ (1, 1) \ (2, 1) \ (2, 2) \ (2, 3) \ (2, 4)$;
3. $(1, 1) \ (1, 1) \ (1, 2) \ (2, 1) \ (2, 2) \ (2, 3) \ (2, 4)$;
4. $(1, 1) \ (1, 2) \ (1, 3) \ (2, 1) \ (2, 2) \ (2, 3) \ (2, 4)$;
5. $(1, 1) \ (1, 1) \ (1, 1) \ (2, 1) \ (2, 2) \ (2, 3) \ (3, 1)$;
6. $(1, 1) \ (1, 2) \ (1, 1) \ (2, 1) \ (2, 2) \ (2, 3) \ (3, 1)$;
7. $(1, 1) \ (1, 1) \ (1, 2) \ (2, 1) \ (2, 2) \ (2, 3) \ (3, 1)$;
8. $(1, 1) \ (1, 2) \ (1, 3) \ (2, 1) \ (2, 2) \ (2, 3) \ (3, 1)$;
