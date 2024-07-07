
# Task

Alice and Bob are playing (once again!) a game. This time, they have a natural number $n$, and the two players, starting with Alice, will proceed as follows:

On each of her turns, Alice can subtract an even number less than or equal to $n$, and Bob can subtract an odd number less than or equal to $n$.

The player who reduces the number to $0$ is declared the winner. 

Ștefan quickly figured out who wins; can you do the same?

# Input data

The first line contains $t$, the number of tests. The following $t$ lines contain the values of $n$ corresponding to each game.

# Output data

For each test, print `Alice` if Alice wins, or `Bob` if he wins.

# Constraints and clarifications

* $1 \\leq t \\leq 10^5$
* $1 \\leq n \\leq 10^9$

# Example

`stdin`
```
3
2
7
14
```

`stdout`
```
Alice
Bob
Alice
```
