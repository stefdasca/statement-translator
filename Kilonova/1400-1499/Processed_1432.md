Construct a sequence of natural numbers that respects the following constraints:

* the first number in the sequence is $9$;
* the numbers are generated in strictly increasing order;
* the sequence contains all the numbers formed only with the digits $7$, $8$, and $9$ with the property that the number of $9$ digits is greater than or equal to the number of $8$ digits, and the number of $8$ digits is greater than or equal to the number of $7$ digits.

The first $14$ terms of the sequence, in order, are: $9$, $89$, $98$, $99$, $789$, $798$, $879$, $897$, $899$, $978$, $987$, $989$, $998$, $999$. Starting from these numbers, Liv invented an interactive game: $N$ rabbits are arranged in a sequence, each holding a card. Each card has two sides, a white side with a number from this sequence and a gray side, with the position of that number in the sequence, the positions being numbered in order, starting with the value $1$.
~[iepurasi.png|align=right]

**Examples.** The card with the number $1$ inscribed on the gray side will have the number $9$ inscribed on the white side, and the card with the number $5$ inscribed on the gray side will have the number $789$ inscribed on the white side. The rabbits are arranged in some order and hold the cards so that the gray side is visible. The game consists in rearranging the rabbits from left to right, in descending order according to the numbers written on the gray sides, using only the $TAP$ operation on a rabbit. When a $TAP$ operation is applied to a rabbit, the sequence of rabbits, starting from the one tapped and up to the end of the sequence (to the right), is reversed (as in the image on the right). After the reversal, all the rabbits in that sequence hold the cards so that the white side is visible. The goal is to apply as few $TAP$ operations as possible to rearrange the rabbits.

# Task

Write a program that reads the natural numbers $N$ (representing the number of rabbits) and $a_1$, $a_2$, $\\dots$, $a_N$ (representing, in order, the numbers written on the gray sides) and that determines:

1. The minimum number of $TAP$ operations required to rearrange the rabbits;
2. The smallest number on a hidden white side, in case there are cards not turned over. If all the cards have been turned over (all showing the white side), the largest number on the white side of a card is printed.

# Input data

The input file `iepurasi.in` contains on the first line the natural number $N$ representing the number of rabbits. The second line of the file contains, in order, the $N$ numbers: $a_1$, $a_2$, $\\dots$, $a_N$, separated by a space, representing in order, the numbers written on the gray sides of the cards.

# Output data

The output file `iepurasi.out` will contain on the first line a number representing the minimum number of $TAP$ operations required to rearrange the rabbits. The second line will contain a number representing the smallest number on a hidden white side (in the case there are cards not turned over), respectively the largest number on the white side of a card, in case all the cards have been turned over (with all showing the white side).

# Constraints and clarifications

* $2 \\leq N \\leq 10 \ 000$;
* $1 \\leq a_i \\leq 10 \ 000$ ($1 \\leq i \\leq N$);
* $N$, $a_1$, $a_2$, $...$, $a_N$ are natural numbers;
* For solving Task 1, $50\\%$ of the score is awarded, and for Task 2, $50\\%$ of the score is awarded.

# Examples

`iepurasi.in`
```
5
14 5 8 9 10
```

`iepurasi.out`
```
1
999
```

# Explanation

One $TAP$ operation is applied to the rabbit with the order number $5$. The unturned card has the order number $14$ ($999$). 

