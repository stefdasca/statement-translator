You are the owner of a football team. You have found the perfect strategy to win any match your team plays. This strategy consists of telling each player to **pass the ball to exactly one person**. Even though it initially seems like a poor strategy, it has helped you reach the championship finals at the village level.

In a team, other "*sub-teams*" are formed. A "*sub-team*" represents a set of players where any player can pass to any other player via an indirect pass or a series of passes. In these "*sub-teams*" you have established certain roles that **at least one** player must have, specifically $K$ different roles.

# Task

Knowing that there are $N$ players in the team, $K$ different roles, and each pass a player can make, determine the number of ways to assign roles to the team.

# Input data

The first line of the input file `echipe.in` contains $N$ followed by $K$. The next line contains a sequence of natural numbers $p_1$, $p_2$, $\\cdots$, $p_N$. For each $i$, $1 \\leq i \\leq N$, player $i$ can pass the ball to player $p_i$.

# Output data

The first line of the output file `echipe.out` will contain a single integer, which represents the remainder of the division by $10^9 + 7$ of the number of ways to assign roles to the team.

# Constraints and clarifications

* $1 \\leq K \\leq N \\leq 2 \\cdot 10^5$
* Each number in the interval $[1, N]$ appears in the sequence $p$ only once
* It is guaranteed that there is at least one way to assign roles to the team

# Subtasks

|#|Points|Constraints|
|-|-|--------|
|1|12|$1 \\leq N \\leq 15$, $1 \\leq K \\leq 4$|
|2|40|$1 \\leq N,K \\leq 1\\ 000$|
|3|48|No additional constraints|

# Example

`echipe.in`
```
5 2
2 3 1 5 4
```

`echipe.out`
```
12
```

## Explanation

~[echipe.png|align=right|width=30%]

The sub-teams formed are: $\\{ \\texttt{1, 2, 3} \\}$ and $\\{ \\texttt{4, 5} \\}$

And here are the passes that the players will make, and the ways in which roles can be assigned are as follows ($r_i$ indicates the role of player $i$):

|#|r₁|r₂|r₃|r₄|r₅|
|-|-|--------|-|-|-|
1|1|1|2|1|2|
2|1|1|2|2|1|
3|1|2|1|1|2|
4|1|2|1|2|1|
5|1|2|2|1|2|
6|1|2|2|2|1|
7|2|1|1|1|2|
8|2|1|1|2|1|
9|2|1|2|1|2|
10|2|1|2|2|1|
11|2|2|1|1|2|
12|2|2|1|2|1|