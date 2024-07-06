Ionel and Georgel collect tokens found in Scooby-Doo magazines. The tokens have different values, distinct natural numbers, with a child unable to have two or more tokens with the same value. They propose the following game: having their own tokens in front of them, they together determine which token has the smallest common value and which token has the largest common value. After identifying these tokens, the winner is the one who will have the most tokens left after removing those with values between the minimum and maximum common values, including the minimum and maximum.

# Task

Determine the minimum and maximum common values, as well as the winner of the game.

# Input data

The input file `jeton.in` contains on the first line two natural numbers separated by a single space, $m$ and $n$ representing the number of tokens of the first child and respectively the number of tokens of the second child. The next line contains $m + n$ values separated by a space, which represent the tokens of the first child and then the tokens of the second child.

# Output data

The output file `jeton.out` contains on the first line three integer values $\\text{Min} \\ \\text{Max} \\ \\text{C}$ separated by a space, where $\\text{Min}$ is the smallest common value, $\\text{Max}$ is the largest common value, and $\\text{C}$ will be $0$ if the game ends in a draw, $1$ if the first child wins, or $2$ if the second child wins.

# Constraints and clarifications

* $0 \\lt n, m \\leq 28 000$
* $0 \\lt \\text{value on a token} \\leq 50 000$
* There will be at least two common values

# Example 1

`jeton.in`
```
10 6
1 3 2 4 7 5 8 19 27 9 3 8 80 6 18 19
```

`jeton.out`
```
3 19 1
```

## Explanation

The smallest common token is the one with the value $3$, and the largest has the value $19$. The first child is left with $3$ tokens (these are $1, 2, 27$) and the second child is left with only one (the token $80$), so player $1$ is the winner.

# Example 2

`jeton.in`
```
4 5
6 7 1 90 6 7 68 1 3
```

`jeton.out`
```
1 7 0
```

## Explanation

The smallest common token is the one with the value $1$, and the largest has the value $7$. The first child is left with one token (this is $90$) and the second child is left with only one (the token $68$), so it is a draw.