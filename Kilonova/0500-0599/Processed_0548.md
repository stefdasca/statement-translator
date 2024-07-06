Richard has prepared a magic trick to impress Dara. To perform this magic trick, Richard bought a deck of $N$ cards, each with a non-zero natural number written on its back.

However, Richard considers that the deck of cards is not good enough for his magic trick. He decided to choose a set of at least two cards from the bought deck so that it has the highest possible *magic coefficient*.

The *magic coefficient* of a set of cards is the product of the sum of the numbers written on those cards and their greatest common divisor. For example, for the set of cards with numbers $\\{2, \\ 3, \\ 6, \\ 7, \\ 8\\}$, the maximum *magic coefficient* is $32$ and is obtained for the set of cards with numbers $\\{2, 6, 8\\}$ (See Example $2$).

# Task

Given the numbers written on the $N$ cards in the deck, determine:
1. The *magic coefficient* of the entire deck of cards;
2. The maximum *magic coefficient* obtained by selecting a set of at least two cards from the deck.

# Input data
The input file `magictrick.in` contains the following:
1. The first line contains the natural numbers $C$ and $N$, where $C$ represents the task to be solved ($1$ or $2$), and $N$ represents the number of cards bought by Richard.
2. The next line contains $N$ values, representing the numbers written on the back of each card. The numbers present in the same line of the file are separated by a space.

# Output data
The output file `magictrick.out` should contain either only the answer for task $1$ (if $C=1$) or only the answer for task $2$ (if $C=2$).

# Constraints and clarifications
* $C \in \\{1, 2\\}$;
* $2 \\leq N \\leq 100 \\ 000$;
* The numbers written on the $N$ cards have values between $[1, 500 \\ 000]$.

|# | Score | Constraints|
| - | - | ------------|
| 1 | 20| $C = 1$ |
| 2 | 9 |$C=2$, $N \\leq 1 \\ 000$, and each number written on the $N$ cards is between [$1$, $6$]|
| 3 | 11|$C=2$, $N \\leq 1 \\ 000$, and each number written on the $N$ cards is between [$1, 1 \\ 000$]|
| 4 | 13|$C=2$, and the numbers written on the $N$ cards are powers of the same number in the interval $[2, 6]$|
| 5 | 47|without additional constraints.|

# Example 1

`magictrick.in`
```
1 5
1 2 3 4 5
```

`magictrick.out`
```
15
```

## Explanation

The *magic coefficient* of the deck is: $(1 + 2 + 3 + 4 + 5) \\cdot {gcd}(1, 2, 3, 4, 5) = 15 \\cdot 1 = 15$

# Example 2

`magictrick.in`
```
2 5
2 3 6 7 8
```

`magictrick.out`
```
32
```

## Explanation

The maximum *magic coefficient* is: ${gcd}(2, 6, 8) \\cdot (2 + 6 + 8) = 2 \\cdot 16 = 32$