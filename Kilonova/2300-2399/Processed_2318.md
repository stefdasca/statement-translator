On Christmas Eve, eagerly waiting for Santa Claus, Andrei and Bogdan decide to play a game, the winner being the first who will receive the gift from Santa Claus.

They write $n$ natural numbers on $n$ tickets, one number on each ticket. Each of them draws a ticket from a bowl.

A ticket is lucky if the number written on it is a *fantastic number*.

A number is *fantastic* if it has an even number of digits and is a multiple of $2024$. The winner of the game is the one who draws the most lucky tickets. If by the end of the game both boys have drawn an equal number of lucky tickets, they are both considered winners and will receive the gift at the same moment.

# Task

Given the number $n$ of tickets as well as the numbers written on the $n$ tickets, determine the total number of lucky tickets drawn by the two children.

# Input data

The input file `fantastic.in` contains the first line a number $n$, representing the number of tickets in the bowl and the next line contains the $n$ natural numbers inscribed on the $n$ tickets.

# Output data

The output file `fantastic.out` will contain the number $k$ representing the number of lucky tickets drawn by both children.

# Constraints and clarifications

* $n$ is a non-zero natural number, of a maximum of $6$ digits.
* The numbers written on the tickets are natural numbers with a maximum of $9$ digits.
* Numbers can be repeated on tickets.

# Example 1

`fantastic.in`
```
8
1205
4048
202400
70840
2024
2024
4046
49158912
```

`fantastic.out`
```
5
```

## Explanation

The first child drew $2$ lucky tickets ($202400$ and $2024$), the second child drew $3$ lucky tickets ($4048$, $2024$ and $49158912$).

# Example 2

`fantastic.in`
```
5
1205
4048
202400
2023
20240
```

`fantastic.out`
```
2
```

## Explanation

The first child drew $1$ lucky ticket ($202400$), the second child drew $1$ lucky ticket ($4048$).