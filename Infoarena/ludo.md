## Task

A new version of the well-known game "Don't Get Angry, Brother" has appeared in stores, called "Ludo". Deni and Bob immediately decided to buy it and start learning the rules: A game board is given, which has boxes numbered from $1$ to $N$. Certain boxes are neighbors. We have a pawn that can be placed in a box and can be moved to another neighboring box. The map is special - starting from a box, the pawn cannot return to it without passing through previously visited boxes. The first player chooses a box in which to place the pawn. Then it is the second player's turn to move, and they begin to alternately move the pawn from one box to another neighboring one. A previously visited box becomes marked and can no longer be used. The player who can no longer move the pawn to an unmarked neighboring box loses, and the other wins. Deni and Bob are experienced in such games; therefore, they will always play optimally. Deni starts. She knows how to choose a starting box such that she will always win. Write a program that reads the game's parameters and displays for each box whether it represents a winning or losing starting position.

## Input data

The input file `ludo.in` contains the numbers $N$ and $M$ on the first line - the number of boxes on the game board and the number of pairs of neighboring boxes. Each of the next $M$ lines contains two integers, $x$ and $y$, representing the indices of two neighboring boxes.

## Output data

The output file `ludo.out` will display a sequence of $0$ and $1$ without spaces, where $0$ means the position is a losing starting position and $1$ means it is a winning starting position.

## Constraints

$1 \leq N \leq 5 \* 10^5$

$1 \leq M \leq 5 \* 10^5$

For $10$ points, $1 \leq N, M \leq 10^4$ and the boxes form a straight line.

For $30$ points, $1 \leq N, M \leq 3 \* 10^3$

For $15$ points, $1 \leq N, M \leq 2 \* 10^5, N = 2^s - 1$ for a certain $s$ and $2^s-1$ boxes have one neighbor, one box has two neighbors, and the others have three neighbors each.

For $35$ points, $1 \leq N, M \leq 2 \* 10^5$

For $10$ points, $1 \leq N, M \leq 5 \* 10^5$

## Example

`ludo.in`
```
5 4
1 2
1 3
2 4
2 5
```

`ludo.out`
```
00011
```

## Explanation

For an optimal game mode, the output indicates that Deni loses if she initially places the pawn in one of the boxes marked with $1$, $2$, or $3$, and if she places it in any of the others, she wins. If Deni places the pawn in box number $1$, Bob can move the pawn to box number $3$, and Deni will not have any available moves because box $1$ is already marked. Similarly, Deni will lose if she places the pawn in box number $2$. For boxes $4$ and $5$, she has a winning strategy.