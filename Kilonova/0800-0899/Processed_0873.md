Ana and Bogdan have invented a new game they called **ks**. On the game board, there are placed consecutively $n$ tokens, with each token having a non-zero natural number written on it. Ana is the first to move and she is allowed to extract exactly $k$ tokens placed consecutively on the board.

Bogdan moves second and he is also allowed to extract exactly $k$ tokens, from those remaining on the board, also placed consecutively.

The score associated with a move is equal to the sum of the numbers written on the extracted tokens for that move.

Ana's goal is to make her move such that Bogdan's score is as low as possible. We assume that both Ana and Bogdan play optimally.

# Task

Given the number of tokens on the game board, the values written on them, as well as the value $k$, write a program that determines the best possible score Bogdan can achieve, knowing that both players play optimally.

# Input data

The input file `ks.in` contains on the first line two natural numbers separated by space $n \ k$, having the meaning from the statement. The second line contains $n$ non-zero natural values, separated by a space, representing the values written on the $n$ tokens, in the order they are placed on the game board.

# Output data

The output file `ks.out` will contain a single line which will have a natural number representing the maximum score Bogdan can achieve on his move, knowing that both players play optimally.

# Constraints and clarifications

* $3 \leq n \leq 100\ 000$;
* $1 \leq k \leq n/3$;
* The values written on tokens are non-zero natural numbers $\leq 10^9$;
* After Ana extracts her tokens, the remaining tokens on the board will keep their initial positions.

# Example

`ks.in`
```
10 3
1 2 5 4 15 2 4 5 1 6
```

`ks.out`
```
12
```

## Explanation

There are several optimal moves for Ana. One of them is to select the tokens $5, 4, 15$.

In this case, the best move for Bogdan is to select the tokens $5, 1, 6$ which would bring him a score equal to $12$, the maximum possible. Another optimal move for Ana is to choose the tokens $4, 15, 2$, or $15, 2, 4$, the maximum score Bogdan can achieve remaining the same, $12$.