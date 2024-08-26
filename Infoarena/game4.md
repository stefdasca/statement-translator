# Game4

Alice and Bob are playing a mathematical game in which they take turns alternately. Initially, they start the game with an array of $N$ non-zero natural numbers $a_1, a_2, \dots, a_N$. A move consists of choosing a number in the form $p^k$, where $p$ is a prime number and $k$ is a non-zero natural number, followed by dividing all the numbers $a_i$ which are divisible by this value by $p^k$ (there must be at least one value $a_i$ in the current array that will be modified in this step). Alice always makes the first move. The player who makes the last move wins, and the one who cannot move anymore loses (all values $a_i$ have become 1). On each move, if the current player has a winning strategy, they will play according to this strategy. Otherwise, the player has to make a possible move.

## Task

Determine the winner of the game. Determine the number $V$ of distinct ways to make the first move for the player who wins the game. For example, assuming Alice wins, $V$ = the number of distinct values $p^k$ that Alice can choose on her first move so that she is sure to win the game in the end. Assuming Bob wins the game, $V$ = the number of distinct values $p^k$ from which Bob can choose on his first move so that he wins in the end (don't forget that Alice starts the game). If Bob can choose the same value $p^k$ for two different initial moves of Alice that would lead him to win, this value will be counted only once.

## Input data

The input file `game4.in` contains $T$ tests. The first line contains the natural numbers $T$ and $C$, the number of tests, and the required task (1 or 2). The next $T$ lines contain one game each given by $N$ and the numbers $a_1, a_2, \dots, a_N$ separated by a space. For all tests in the same file, the same task $C$ is solved.

## Output data

The output file `game4.out` will contain $T$ lines, on the $i$-th line will be the answer for the $i$-th test. If $C = 1$, for each game, print the name of the winner "Alice" or "Bob". If $C = 2$, print for each game the number $V$ of distinct moves from which the winner could choose their first move, according to the clarifications in point 2.

## Constraints

$2 < T < 10$ \\
$1 < N < 100000$ \\
$1 < a_i < 1000000, 1 < i < N$ 

For test cases worth 40 points, $C = 1$. \\
For test cases worth 60 points, $C = 2$. For part of these, worth 20 points, Alice always wins. \\
For test cases worth 30 points, $a_i < 20, 1 < i < N$ 

## Example

`game4.in`
```
4 1
2 7 25
2 10 21
10 43 89 47 29 68
2 27 52 92 27 7 23 1 529 19
1 529 29
```

`game4.out`
```
Alice
Bob
Alice
Bob
```

## Explanation

There are 4 tests to solve for task 1. In the first game, $N=2$ and $a_1=7$, $a_2=25$ and Alice wins. She can initially choose $p^k=5^1$, $p^k=5^2$ or $p^k=7^1$. Possible variants: $p^k=5^1$, divide by $5^1$ obtaining $a_1=7$ and $a_2=5$. If Bob then chooses 7, we get $a_1=1$ and $a_2=5$. Alice will choose 5, getting $a_1=1$ and $a_2=1$ and she will win. Similarly, if Bob had chosen 5 instead of 7. The cases $p^k=5^2$ or $p^k=7^1$ for Alice's first move will allow Bob to choose either 7 or $5^2$ and win. Consequently, Alice wins only if she chooses $p^k=5^1$. In the second game, $N=2$ and $a_1=10$, $a_2=21$ and Bob wins. Alice can initially choose $p^k=2^1$, $p^k=5^1$, $p^k=3^1$ or $p^k=7^1$. For each of Alice's choices, Bob can choose any of the remaining three variants. In the next two moves, one will be Alice's choice and the last value will be chosen by Bob, who will win.

`game4.in`
```
4 2
2 7 25
2 10 21
10 43 89 47 29 68
2 27 52 92 27 7 23 1 529 19
1 529 29
```

`game4.out`
```
1
4
1
4
```

## Explanation

There are 4 tests to solve for task 2 (see the explanation above). In the first game, $N=2$ and $a_1=7$, $a_2=25$ and Alice wins, who can initially choose only the variant $p^k=5^1$ which allows her to win. Therefore, there are $V=1$ distinct variants. In the second game, if Alice chooses $p^k=2^1$, Bob can initially choose $p^k=5^1$, $p^k=3^1$ or $p^k=7^1$. Similarly, if Alice chooses any of $p^k=5^1$, $p^k=3^1$ or $p^k=7^1$, Bob will be able to choose the first move from the remaining three variants. Consequently, the number of distinct values that Bob can initially choose is $V=4$. We see that Bob can choose as the first move, $p^k=3^1$ in all three cases when Alice initially chose $p^k=2^1$ or $p^k=5^1$ or $p^k=7^1$, but this move is counted only once.