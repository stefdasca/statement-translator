## Task

Gigel and Ionel have started playing a new game after getting bored of the game from last year's Happy Coding (see problem obj). This time, they have a linear game board consisting of $N$ squares numbered from $1$ to $N$ from left to right. Initially, all $N$ squares are free. The two players take turns making the following type of move: the player whose turn it is must place a piece of size $1 \times K$ over $K$ consecutive free squares on the board; after placing the piece, the $K$ squares become occupied. The winner of the game is the one who makes the last move (equivalently, the loser is the player who, when it is their turn, cannot make any move). For multiple pairs $(K,N)$ given, determine who wins the game (the first player, meaning the one who makes the first move, or the second player), considering that both players will use an optimal strategy.

## Input data

The first line of the file `kboard.in` contains the integers $K$ and $T$, separated by a space. $K$ represents the size of the piece, and $T$ represents the number of game boards that will be given subsequently. Each of the following $T$ lines will contain an integer $N$, representing the number of squares on the game board.

## Output data

In the output file `kboard.out` you will print $T$ lines. The $i$-th of these lines will contain the winner of the game on a game board having $N$ squares given in the $i$-th test from the input file and the piece size $K$ given on the first line of the input file. If the winner of the game is the first player, print $1$. Otherwise, print $2$.

## Constraints and clarifications

$1 \leq K \leq 10\, 000\, 000$  
$1 \leq T \leq 100\, 000$  
If $K \leq 2$, then $1 \leq N \leq 1\, 000\, 000\, 000$  
If $K > 2$, then $1 \leq N \leq \max \{ 3000, 69 \times K - 19 \}$  

## Examples

`kboard.in`
```
1 3
1
2
3
```
`kboard.out`
```
1
2
1
```

`kboard.in`
```
2 4
1
2
5
6
```
`kboard.out`
```
2
1
2
1
```

`kboard.in`
```
3 4
999998
100256
1
1
```
`kboard.out`
```
2
1
2
1
```

`kboard.in`
```
9999999 20
89999988
289999962
129999982
16124217
299106936
60546243
524323847
649999916
449756549
64633851
209999972
368724199
152731683
89999988
77390991
649999916
25493701
289999962
225376567
223888509
```
`kboard.out`
```
2
2
2
1
1
1
1
2
1
1
2
1
1
2
1
2
1
2
1
1
```