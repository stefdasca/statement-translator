
Fascinated by Ancient Egypt, Rareș wants to build as many pyramids as possible from identical square cards. He has $N$ cards numbered from $1$ to $N$, either white or grey, arranged in strictly increasing order of numbers.

The first pyramid will be built using the first three cards. The base of the pyramid will be formed from cards $1$ and $2$ placed side by side, with card $3$ placed on top (the peak of the pyramid).

The second pyramid will have its base formed from cards $4$, $5$, and $6$ placed side by side, above which cards $7$ and $8$ will be placed side by side, with card $9$ placed on top (the peak of the pyramid).

Going forward, he will construct complete pyramids in sequence with bases formed from $4$ cards (numbered $10$ to $13$), $5$ cards (numbered $20$ to $24$), $6$ cards (numbered $35$ to $40$), etc., as long as he can build a complete pyramid. For example, if Rareș has $N = 75$ cards, then he will build complete pyramids $1$, $2$, $3$, $4$, and $5$ as shown in the following images. Out of the $75$ cards, he will only use the first $55$ cards, as the last $20$ cards are insufficient to build the $6^{th}$ pyramid with a base formed of $7$ cards.

~[piramide.png]

# Task

Write a program to read the natural numbers $N$ (representing the number of cards), $X$ (representing the number of a card), $K$ (representing the number of white cards), and the numbers of the $K$ white cards $c_1$, $c_2$, ..., $c_K$ and to determine:

* the number $P$ of the complete pyramid containing the card numbered $X$;
* the maximum number $M$ of complete pyramids built by Rareș;
* the number $C$ of unused cards;
* the number $A$ of the first complete pyramid containing the most white cards.

# Input data

The input file `piramide.in` contains the three numbers $N$, $X$, and $K$, separated by a space, on the first line. The second line of the file contains, in order, the $K$ numbers $c_1$, $c_2$, ..., $c_K$, separated by a space, representing the numbers of the $K$ white cards out of the $N$.

# Output data

The output file `piramide.out` will contain on the first line the number $P$ or the value $0$ (zero) if none of the constructed complete pyramids contain the card numbered $X$.

The second line will contain the number $M$. 

The third line will contain the number $C$. 

The fourth line will contain the number $A$ or the value $0$ (zero) if no complete pyramid contains at least one white card.

# Constraints and clarifications

* $1 \\leq a, b \\leq 1 \\ 000 \\ 000$;
* $3 \\leq N \\leq 100 \\ 000$; 
* $1 \\leq X \\leq N$; 
* $1 \\leq K \\leq N$; 
* $1 \\leq c_1 < c_2 <...< c_K \\leq N$;
* A complete pyramid with a base formed from $b$ cards is constructed by arranging the necessary cards in $b$ rows: $b$ cards in the first row (the base), then $b - 1$ cards in the second row, $b - 2$ in the third row, $\\dots$, two cards in the $b - 1^{th}$ row, and one card (the peak of the pyramid) in the $b^{th}$ row.
* Solving requirement a) awards 20% of the score, solving requirement b) 20% of the score, solving requirement c) 20% of the score, and solving requirement d) 40% of the score.

# Example

`piramide.in`
```
75 15 23
5 9 11 18 20 21 25 27 28 30 35 37 45 46 51 55 60 65 68 69 70 71 72
```

`piramide.out`
```
3
5
20
4
```

## Explanation

Pyramid $3$ ($P = 3$) contains the card numbered $X = 15$. Rareș can build only $M = 5$ complete pyramids, leaving $20$ unused cards ($C = 20$) insufficient to construct the 6th pyramid. The maximum number of white cards in a complete pyramid is $6$. Pyramids $4$ and $5$ each contain a maximum number of white cards ($6$), the first of these being pyramid $4$ ($A = 4$). The last $7$ white cards (numbered: $60$, $65$, $68$, $69$, $70$, $71$, $72$) are not used in constructing complete pyramids.
