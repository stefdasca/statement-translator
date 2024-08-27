Alice

Let's consider the following single-player game: Alice initially has $X$ USD. The dealer has a deck of $N$ black cards and $R$ red cards, shuffled together. The dealer turns over the cards from the deck one by one. Once a card is turned over, it is removed from the deck. If, at any moment, Alice has $X$ USD, then just before the next card is turned over, she can bet any amount $S$ from the interval $[0,X]$ (any real number within this interval) on the color of the card. If the card turned over is the color Alice bet on, Alice wins $S$ USD. Otherwise, she loses $S$ USD. Determine the maximum amount Alice can be guaranteed to obtain after all the cards have been turned over.

## Input data

The first line of the input file `alice.in` contains 3 integers, separated by a space, $N$, $R$, and $X$, representing the number of black cards in the deck, the number of red cards in the deck, and the initial amount Alice has.

## Output data

The output file `alice.out` will contain the maximum amount Alice can be guaranteed to obtain. If this amount is not an integer, print the lower integer part of that amount.

## Constraints and clarifications

$0 \leq N \leq 30$ 

$0 \leq R \leq 30$ 

The result will fit within a 32-bit integer. 

## Examples

`alice.in`

`alice.out`

0 1 300 

600 

1 2 300 

800 

8 2 3000 

68266 

## Explanation

For the third example, the actual amount obtained is $68266.6666666667$.