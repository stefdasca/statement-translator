Sure, here is the translated text:

```markdown
For the game to be played, $k$ sets of $n+2$ balls each are used. Among the $n+2$ balls:
- $n$ are inscribed with distinct numbers from $1$ to $n$, representing the value of each ball.
- $2$ are inscribed with the number $0$, which have a special role and do not have value.

There are $k$ players in the game, numbered distinctly from $1$ to $k$.
The game is played as follows:

- From the first set of balls, the first player receives $p$ balls that they must arrange in a line such that the numbers inscribed on these balls form a subarray of consecutive values and have the maximum sum;
- From the second set of balls, the second player receives $p$ balls that they must arrange in a line such that the numbers inscribed on these balls form a subarray of consecutive values and have the maximum sum;
- $\\dots$
- From the $k$-th set of balls, the $k$-th player receives $p$ balls that they must arrange in a line such that the numbers inscribed on these balls form a subarray of consecutive values and have the maximum sum;
- A subarray can contain balls with value $0$ that can replace any nonzero value without modifying the sum of values in the subarray.

The player who obtains the subarray with the maximum sum of ball values wins, and this is called the winning sum.

# Task

Write a program that reads the number $n$, the number $k$, the values of the balls received by each player, and determines the number of the winning player and the value of the winning sum.

# Input data

The first line of the file `joc.in` contains three numbers, $n$, $k$, $p$, separated by a space, with the meaning given in the statement. Each of the following $k$ lines (in ascending order of the player numbers) contains $p$ natural numbers, separated by a space, representing the values of the balls received by each player.

# Output data

The first line of the file `joc.out` will contain two natural numbers, separated by a space. The first value represents the number of the winning player. The second value represents the winning sum.

# Constraints and clarifications

* $1 \leq n \leq 500\ 000$
* $1 \leq k \leq 20$
* $1 \leq p \leq \min(100\ 000, n+2)$
* It is guaranteed that each player receives balls with distinct values, except for the special balls.
* If the winning sum is obtained by multiple players, the winning player will be the player with the smallest number.
* For determining the correct number of the winning player, $40\%$ of the points are awarded.
* For determining the correct value of the winning sum, $60\%$ of the points are awarded.

# Example

`joc.in`
```
6 3 5
5 1 6 3 2 
6 1 3 4 0 
2 0 6 4 0 
```

`joc.out`
```
2 13
```

## Explanation

There are $3$ players in the game; each receives $5$ balls, their values being between $1$ and $6$.
The first player does not have special balls. They can construct the subarray with the maximum sum $11$, namely: $5\ 6$. The second player has one special ball. They can construct the subarray with the maximum sum $13$, namely: $3\ 4\ 0\ 6$. The third player has two special balls. They can construct the subarray with the maximum sum $12$, namely: $2\ 0\ 4\ 0\ 6$. The winning sum is $13$ and is obtained by player $2$.
```