Amalia has gathered $n$ cards that she can use in several games. Each card has a single number written on it, which has at least two digits and at most nine digits. In the game Numersum, she uses the cards with numbers where the first digit is equal to the sum of the other digits in the number. Amalia wants to select the cards for this game and arrange them in ascending order based on the numbers written on them.

# Task

Write a program that, given the number of cards $n$ and the numbers written on the $n$ cards, determines in ascending order the numbers that Amalia can use in the Numersum game.

# Input data

The input file `joc.in` contains on the first line the natural number $n$, which represents the number of cards. The second line of the file contains $n$ natural numbers $c_1, c_2, \dots, c_n$, representing the numbers written on the $n$ cards.

# Output data

The output file `joc.out` contains a single line which contains the numbers written on the cards that can be used in the Numersum game, in ascending order, separated by a space.

# Constraints and clarifications

* $3 \leq n \leq 40\ 000$
* $10 \leq c_i < 10^9$ for $1 \leq i \leq n$
* There is at least one card in Amalia's set that can be chosen for the Numersum game.

# Example

`joc.in`
```
7
211 58 55 514 101 9867 101
```

`joc.out`
```
55 101 101 211 514
```

## Explanation

The numbers from the given sequence that can be used in the Numersum game are: $211 (2=1+1)$, $55 (5=5)$, $514$, $101 (1=0+1)$, $101$, and they will be displayed in ascending order.