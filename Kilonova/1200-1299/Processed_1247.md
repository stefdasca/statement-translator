The big group at kindergarten has invented a game. A number of $n$ children are **in a circle** around the kindergarten teacher, who stands in the center. Each child holds an even number of marbles. When the teacher claps her hands, each child will simultaneously give half of their marbles to the child on their right, receiving from the child on their left half of their marbles. If after such a move a child ends up having an odd number of marbles, they will immediately receive a marble from the kindergarten teacher. The game ends when all children have the same number of marbles.

# Task

Write a program that reads $n$ (the number of children) and the initial number of marbles for each child and determines how many times the teacher claps her hands until the game ends, as well as the number of marbles each child will have at the end of the game.

# Input data

The input file `joc.in` will contain data for multiple games. Each data set will start with a value $n$ representing the number of children participating in the game followed by $n$ even natural numbers representing the number of marbles each child initially has. Each number will be represented on a line. The file ends with the value $-1$. The data in the file is correct.

# Output data

The output file `joc.out` will contain for each game a line with two space-separated numbers. The first number represents how many rounds the game will have (how many times the teacher claps her hands until all children have the same number of marbles), and the second number will represent the number of marbles each child has at the end of the game.
The file ends with a value representing the number of games described in the input file.

# Constraints and clarifications

* $0 \leq n \leq 1\ 000$, $n$ represents the number of children
* $0 < \text{initial number of marbles of each child} < 32\ 700$
* Each game will definitely end in a finite number of steps.
* A file contains at most $100$ games.
* No partial scores will be awarded.

# Example

`joc.in`
```
6
36
2
2
2
2
2
4
2
4
6
8
-1
```

`joc.out`
```
15 14
4 8
2
```

## Explanation of the second game

| Round $1$ | Round $2$ | Round $3$ | Round $4$ |
| --------- | --------- | --------- | --------- |
| Player $1$: $1 + 4 = 5 \rightarrow 6$ marbles | Player $1$: $3 + 4 = 7 \rightarrow 8$ marbles | Player $1$: $4 + 4 = 8 \rightarrow 8$ marbles | Player $1$: $4 + 4 = 8 \rightarrow 8$ marbles |
| Player $2$: $2 + 1 = 3 \rightarrow 4$ marbles| Player $2$: $2 + 3 = 5 \rightarrow 6$ marbles | Player $2$: $3 + 4 = 7 \rightarrow 8$ marbles | Player $2$: $4 + 4 = 8 \rightarrow 8$ marbles |
| Player $3$: $3 + 2 = 5 \rightarrow 6$ marbles | Player $3$: $3 + 2 = 5 \rightarrow 6$ marbles | Player $3$: $3 + 3 = 6 \rightarrow 6$ marbles | Player $3$: $3 + 4 = 7 \rightarrow 8$ marbles |
| Player $4$: $4 + 3 = 7 \rightarrow 8$ marbles | Player $4$: $4 + 3 = 7 \rightarrow 8$ marbles | Player $4$: $4 + 3 = 7 \rightarrow 8$ marbles | Player $4$: $4 + 3 = 7 \rightarrow 8$ marbles |