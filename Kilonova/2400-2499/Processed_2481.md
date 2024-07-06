# Volleyball Team UNSTPB

The volleyball team UNSTPB lines up at various distances from each other.

A player with power $k$ can perform the following action: throw the ball $k$ positions to the right or left, stopping at the first player it touches. If it does not touch a player on the first throw, it will continue to bounce in $k$-increments until hitting someone or going out.

The player who receives the ball, having a different power $k$, can pass it to the left or right in the same way.

We know the player who initially has the ball. We will simulate all cases (for each player, when they receive the ball, first to the left, then to the right). How many players will have had the ball in at least one of the cases?

# Task
You have a C++ program ([here](volei.cpp) or in the "Attachments" section on the side) that implements the above problem but contains a few bugs. Correct the program.

## Hint
A fill algorithm is used, where an array $v$ of $1$ and $0$ is utilized as follows:
- if $v_i$ becomes $1$, then player $i$ was touched at some point;
- if $v_i$ remains $0$, then player $i$ was never touched.

Initially, $v_{start} = 1$, and the rest of the elements are $0$. We have two cases:
- the ball is thrown to the left, in $k$-increments;
- the ball is thrown to the right, in $k$-increments.

If player $i$ is touched in either case, we assign $v_i = 1$ and recursively call the fill function for player $i$.

The process repeats until no new players can be touched.

# Input data

Read $n$ from the keyboard.

The next $n$ lines contain a pair of natural numbers $a_i \\ b_i$, where $a$ represents the position of player $i$ and $b$ is their power.

Next, read $start$, the index of the player who initially has the ball.

# Output data
Print the number of players who receive the ball at a moment in any case.

# Constraints and clarifications
- $1 \le n \le 1\ 000$
- $1 \le a_i \le 1\ 000\ 000\ 000$
- $1 \le b_i \le 1\ 000$
- $1 \le start \le n$
- It is guaranteed that players are already sorted in the order they are lined up, starting from the lowest position.
- The initial player count is also considered.
- No two players are at the same position.

# Example 1
`stdin`
```
8
1 1
2 10
4 3
5 2
7 4
9 5
11 9
12 1000
4
```
`stdout`
```
6
```
## Explanation
The lineup of players looks like this ($\textcolor{red}{\text{x}}$ denotes a position with no player):

$ 1\ 10 \textcolor{red}{\text{ x }} 3\ 2 \textcolor{red}{\text{ x }} 4 \textcolor{red}{\text{ x }} 5 \textcolor{red}{\text{ x }} 9\ 1000 $

- Player 4 (power $3$) touches $1$ and $7$.
- Player $1$ touches $2$.
- Player $7$ touches $11$.
- Player $2$ touches $12$.
- Player $11$ touches $2$.
- Player $12$ touches no one.

In total, 5 players were touched.

# Example 2
`stdin`
```
3
4000 7
293644 8
8661523 11
1
```
`stdout`
```
2
```
## Explanation
- Player $4000$ throws the ball to the right, bouncing from $7$ to $7$ until stopping at player $8661523$.
- Player $8661523$ cannot pass the ball to anyone.
- Player $293644$ does NOT receive the ball.