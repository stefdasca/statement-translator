Gigel, passionate about card games and computers, aims to create a program that simulates a card game between two players \(A\) and \(B\) according to the following rules:
* The game is played as a sequence of alternative moves by the two players; the number of these moves is determined at the start of the game;
* Initially, both players receive the same number of cards, in a certain order; the maximum number of cards received by a player is \(1\ 000\);
* A move consists of placing a card on the table by one of the players;
* Players alternately place a card from the cards received, in the order they received them;
* When a player places a card on the table that has the same value as one already present on the table, that player will take all the cards between these two cards placed on the table, including them, in reverse order to how they were placed on the table. The cards thus taken from the table are placed in the stack of cards of the respective player, after their last card;
* The winner is the player who remains without any cards in hand, even if the number of moves made up to that point is less than the total number of moves. The game ends in a draw if after the established number of moves, both players still have cards in hand.

# Task

Write a program that determines the state of the game after \(n\) moves. By the state of the game, we understand:
* determining the winner \(A\) or \(B\);
* identifying the cards held by the player who lost the game, or in the case of a draw, the cards of both players at the end of the \(n\) moves, as well as identifying the cards on the table, if they exist.


# Input data

The input file `joc.in` has the following format:
* The first line contains a value \(n\) representing the number of moves.
* The second line contains the cards of player \(A\) separated by spaces. This sequence of cards ends with the value \(0\), which is not part of their cards;
* The third line of the input file contains the cards of player \(B\) in the same format.


# Output data

The output file `joc.out` will contain three lines according to the following possible cases:


|Player \(A\) wins|Player \(B\) wins|Draw game|
|--------|--------|--------|
|\(A\)|cards of \(A\)|cards of \(A\)|
|cards of \(B\)|\(B\)|cards of \(B\)|
|cards on the table|cards on the table|cards on the table|

If there are no cards on the table, the value \(0\) will be printed on the third line.


# Constraints and clarifications

* \(1 \leq N \leq 250\)
* \(1 \leq \) value of a card \(\leq 9\)
* For the test data, there is always a solution.

# Example

`joc.in`
```
4 
1 4 2 3 0
2 1 3 4 0
```

`joc.out`
```
2 3
3 4 1 4 2 1
0
```

## Explanation

* Move of \(A\): \(1\)
    * Table: \(1\) (Card placed by \(A\)); \(A\): \(4\ 2\ 3\); \(B\): \(2\ 1\ 3\ 4\)
* Move of \(B\): \(2\)
    * Table: \(1 \ 2\) (\(B\) placed the card \(2\)); \(A\): \(4\ 2\ 3\); \(B\): \(1\ 3\ 4\)
* Move of \(A\): \(4\)
    * Table: \(1 \ 2 \ 4\) (A placed the card \(4\)); \(A\): \(2\ 3\); \(B\): \(1\ 3\ 4\)
* Move of \(B\): \(1\)
    * Table: \(1 \ 2 \ 4 \ 1\) (\(B\) placed the card \(1\)); \(A\): \(2\ 3\); \(B\): \(3\ 4\)

The game ends in a draw (4 moves were made) \(B\) will take the cards \(1\ 2\ 4\ 1\) and will have \(3\ 4\ 1\ 4\ 2\ 1\).