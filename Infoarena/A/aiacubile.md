# Aiacubile

Bulanil the Kangaroo must take care of $N$ children. To avoid boredom, he thought of a game to play with them. Bulanil the Kangaroo places the children in a circle and assigns each one a number from $1$ to $N$. The positions where the children are seated are also numbered from $1$ to $N$. Being in a circle, each position has a successor: after $1$ follows $2$, after $2$ follows $3$, $\dots$ after $N-1$ follows $N$, and after $N$ follows $1$. Initially, each child sits in the position equal to their index: child $1$ sits in position $1$, child $2$ sits in position $2$, $\dots$ child $N$ sits in position $N$. The game is played over several turns. A turn of the game occurs as follows: Bulanil starts from position $1$ and jumps $K$ positions at a time until he lands on a position he has already visited during the current turn. The children sitting at positions visited by Bulanil receive a ball from him. At the end of the turn, the children change their order as follows: a child at position $i$ moves to position $P[i]$. After all children change their order, a new turn of the game begins as described previously. For example, if we consider the game is played with $N = 6$ children, and Bulanil jumps $K = 2$ positions, then:
The children are initially seated in a circle. Bulanil starts from position $1$ and leaves a ball for child $1$. Bulanil jumps $2$ positions, reaches position $3$, and leaves a ball for child $3$. Bulanil jumps $2$ positions, reaches position $5$, and leaves a ball for child $5$. Bulanil jumps $2$ positions, reaches position $1$. Since he has already visited position $1$ during the current turn, he stops. At the end of the turn, children $1$, $3$, and $5$ have received one ball each. Before the next turn begins, the children change their positions as follows: if for this game we consider the sequence $P$ to be $5\, 3\, 1\, 6\, 2\, 4$, then the child on position $1$ (child $1$) will move to position $5$, the child on position $2$ (child $2$) will move to position $3$, the child on position $3$ (child $3$) will move to position $1$, the child on position $4$ (child $4$) will move to position $6$, the child on position $5$ (child $5$) will move to position $2$, and the child on position $6$ (child $6$) will move to position $4$. Hence, the children at each position from $1$ to $6$ will be, in order, $3\, 5\, 2\, 6\, 1\, 4$. Bulanil will jump to positions $1$, $3$, and $5$ and leave a ball for children $3$, $2$, and $1$, respectively. The game ends when the children return to their initial arrangement.

## Task

Bulanil wants to play multiple such games. For each game, knowing the number $N$ of children, the length $K$ representing the number of positions Bulanil can jump, and the sequence $P$ describing how the children change their positions in each turn, determine how many children receive at least one ball during the entire game.

## Input data

The input file `aiacubile.in` contains on the first line the natural number $T$, representing the number of games Bulanil participates in. The following $2*T$ lines describe the $T$ games as follows: on line $2*i$ contain the natural numbers $N$ and $K$, with the meanings described in the task, and on line $2*i+1$ contain $N$ natural numbers forming the sequence $P$, which describes how the children change their order in each turn, for the $i$-th game.

## Output data

The output file `aiacubile.out` will contain $T$ lines. Each line contains a natural number representing the number of children who received at least one ball during the $i$-th game.

## Constraints and clarifications

For all tests, $1 \leq T \leq 10$.
For all tests, $1 \leq P[i] \leq N$, and the sequence $P$ contains only distinct numbers.
It is guaranteed that, at any moment of any game, there will be exactly one child at each position.
It is guaranteed that each game has a finite number of turns.
For tests worth 20 points, $1 \leq N \leq 1000$, and the number of turns each game has is guaranteed to be $\leq 1000$.
For tests worth 90 points, $1 \leq N \leq 100000$.
For all tests, $1 \leq K \leq N$.
The problem will be evaluated on tests worth 90 points.

## Example

`aiacubile.in`
```
2
6 2
5 3 1 6 2 4
12 9
1 6 7 4 9 8 3 12 10 11 5 2
```
`aiacubile.out`
```
4
8
```

## Explanation

## Explanation for the first game:
In the first turn of the game, the children are in the order $1\, 2\, 3\, 4\, 5\, 6$. Children $1$, $3$, and $5$ each receive a ball (as described in the task). In the second turn of the game, the children are in the order $3\, 5\, 2\, 6\, 1\, 4$. Children $3$, $2$, and $1$ each receive a ball (as described in the task). In the third turn of the game, the children are in the order $2\, 1\, 5\, 4\, 3\, 6$. Children $2$, $5$, and $3$ each receive a ball. In the fourth turn of the game, the children are in the order $5\, 3\, 1\, 6\, 2\, 4$. Children $5$, $1$, and $2$ each receive a ball. In the fifth turn of the game, the children are in the order $1\, 2\, 3\, 4\, 5\, 6$. Being the initial order, the game stops. Children $1$, $2$, $3$, and $5$ have each received at least one ball during the game, so the answer for the first game is $4$. For the second game, children $1$, $3$, $4$, $5$, $7$, $9$, $10$, $11$ are the ones who receive balls, so the answer is $8$.