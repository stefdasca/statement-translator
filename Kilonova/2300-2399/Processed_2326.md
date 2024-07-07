
Alexandru and Tudor have invented a game called the Game of Divisors. In this game, each of the two players draws a sequence of $n$ numbers. Alexandru is player number $1$ and Tudor is player number $2$. For each number $x$ in the sequence, its prime divisor with the highest power is obtained, called the **p-divisor**; if the number $x$ has several prime divisors with the same highest power, then the p-divisor is the largest among these prime divisors. Thus, the p-divisor of the number $36$ is $3$, the p-divisor of the number $12$ is $2$, the p-divisor of the number $30$ is $5$.

The rules of the game are as follows:
* Each player chooses the first number from their sequence in the given order and determines its **p-divisor**.
* Among the two p-divisors, the largest number is chosen, called the **winning number**. The player who obtained this number receives $10$ points. If the $2$ p-divisors are equal, they represent winning numbers and each player receives $5$ points.
* Each player chooses the second number from their sequence in the given order and determines its **p-divisor**, according to the previous rules. Thus, the selection of numbers from the two sequences continues until the sequences are exhausted.
* The game is won by the player who obtains the highest score.
* If the players have equal scores at the end of the game, the player who obtained the largest p-divisor among all winning numbers wins.

# Task

Write a program that reads the number $n$, the $n$ numbers from Alexandru's sequence, and then the $n$ numbers from Tudor's sequence, and determines the order number of the winner of the game, the score of the game winner, and the largest number among all the winning numbers in the game.

# Input data

The input file `joc.in` contains a natural number $n$ on the first line, representing the number of numbers in each player's sequence. The second line of the file contains $n$ non-zero natural numbers, separated by spaces, representing Alexandru's game sequence. The third line of the file contains $n$ non-zero natural numbers, separated by spaces, representing Tudor's game sequence.

# Output data

The output file `joc.out` contains a single line with three natural numbers, separated by spaces, representing the order number of the game winner ($1$, if Alexandru wins the game, or $2$, if Tudor wins), the score of the game winner, and the largest number among all the winning numbers in the game.

# Constraints and clarifications

* $2 \leq n \leq 700$
* Any number in the two players' sequences has at most $8$ digits and is greater than $1$.
* It is ensured that for the input tests used, there is a single winner.

# Example 1
`joc.in`
```
5
12 23 45 9 100
42 24 60 54 225
```

`joc.out`
```
1 30 23
```

## Explanation

The first number is chosen from the two sequences: $12$ (has p-divisor equal to $2$) and $42$ (has p-divisor equal to $7$), the winning number is $7$ and the second player receives $10$ points.
The second number chosen from the two sequences: $23$ (has p-divisor $23$) and $24$ (has p-divisor $2$), the first player receives $10$ points, etc.

The first player has $30$ points ($0 + 10 + 10 + 5 + 5 = 30$), the second player has $20$ points ($10 + 0 + 0 + 5 + 5 = 20$). The first player wins the game.

The largest number among all the winning numbers in the game is $23$.

# Example 2

`joc.in`
```
4
9 225 7 4
11 32 16 18
```

`joc.out`
```
2 20 11
```

## Explanation

The two players obtain equal scores, each having $20$ points. The game is won by the second player who has the largest winning p-divisor, equal to $11$.
