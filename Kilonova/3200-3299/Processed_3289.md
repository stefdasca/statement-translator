> You've seen that bad things happen easily.
> Surely it's economical. Like when you put labels; people label: The sky is clear every day of the year because that's how I was taught at school.
> Maybe it's not clear every day of the year.
> --- Ion Durduroiu, Dialogurile Puterii

You've bought a game from Noriel. In this game, there are $N$ pawns. Each pawn is associated with a set of tokens $S_i$ and has a height $H_i$. $S_i$ will always be a set $\{L_i, L_i + 1, \dots, R_i\}$.

The magic of these pawns is that they play on their own. That is, you buy them and just watch them, like on TV.

In a round, two pawns $i$ and $j$ are designated to meet. Then, if $card(\Delta(S_i, S_j)) = |card(S_i) - card(S_j)|^1$, either $i$ or $j$ can adjust its height to be equal to the other. If the condition is not met, nothing will happen.

The instructions on the box say that the game can be stopped anytime. However, you have noticed that when you stop the game board, the pawns start to revolt, forming a tower by stacking one on top of the other, creating a Mega-Pawn with a height equal to the sum of all its component pawns.

$^1$: The set of all elements that belong exactly to one of $A$ or $B$ is denoted by $\Delta(A, B)$. The notation $card(S)$ refers to the number of elements in that set.

# Task

With this in mind, you know there is someone very evil who has bought this game and left it running in a room, intending to stop it when they see that the resultant Mega-Pawn would have maximum height. Therefore, you want to alert the authorities responsible about the maximum height that a Mega-Pawn can achieve, so you can protect the country from this very real threat. However, this game comes in multiple editions, so you should determine the maximum case for each edition.

# Input data

The first line of the input file contains $T$, the number of different editions in which this game comes. There are $T$ descriptions of a game, and the first line of such a description contains $N$, the number of pawns that come with that game. Then there are $N$ lines, each describing a pawn in the game by $L_i$, $R_i$, and $H_i$.

# Output data

Print a single line for each edition, specifically the maximum height of a Mega-Pawn that can be formed according to the rules of the game rounds.

# Constraints and clarifications

* $1 \le T \le 5 \ 000$;
* $1 \le N \le 200 \ 000$;
* $\sum{N} \le 200 \ 000$, where $\sum{N}$ denotes the sum of all $N$s in a single test;
* $1 \le H_i \le 1 \ 000 \ 000 \ 000$;
* $1 \le L_i \le R_i \le 1 \ 000 \ 000 \ 000$.

| #  | Score | Constraints |
|----|-------|-------------|
| 1  |   7   | $1 \le L_i \le R_i \le 2 \cdot N$, $\{L_i, R_i\} \cap \{L_j, R_j\} = \{\ \}$ and there exists an $i$ such that $L_i = 1$ and $R_i = 2 \cdot N$ |
| 2  |  31   | $\sum{N} \leq 2 \ 000$ |
| 3  |  20   | $1 \le L_i \le R_i \le 2\,000$, $\sum{\max{R_i}^2} \le 8 \ 000 \ 000$ |
| 4  |  22   | $1 \le H_i \le 2$ |
| 5  |  20   | No additional constraints |

The notation $\sum{\max{R_i}^2}$ denotes the sum of the square of the maximum value of an $R_i$ from an edition across all editions given in a test.

# Example

`stdin`
```
3
8
6 14 1
11 13 8
3 8 4
1 7 9
5 16 8
4 12 8
2 9 9
10 15 5
3
1 2 1
2 3 3
2 2 2
3
1 1 1
2 2 1
3 3 2
```

`stdout`
```
67
9
4
```

## Explanation

In the first possible edition of the game, the pawns can make the following moves to achieve the maximum Mega-Pawn height:

1. The $3$rd meets the $7$th pawn, equalizing their heights.
2. The $8$th meets the $2$nd pawn, equalizing their heights.
3. The $1$st meets the $5$th pawn, equalizing their heights.

## Illustration

~[output.png|align=center]
$$
\text{Illustration of the first edition shown in the example}
$$