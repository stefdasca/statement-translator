~[dartz.png|align=right]

Alex is a great darts player. For this game, a disc-shaped board divided into regions is used, and each region has an associated score (a non-zero natural number). The game is played in four stages. In each stage, the player has three darts to throw at the board. The score obtained for each dart is equal to the score of the region it lands in. The total score $S$ obtained by the player at the end of the game is the sum of the scores from the four stages.

Having no partner to play with, Alex decides to play all four stages by himself. Also, to practice arithmetic, he decides that the score for each stage should be equal to the product of the scores obtained by the three darts. For example, if in one stage the scores obtained by the three darts are: $3$, $4$, $5$, then the stage score will be $60$ ($60 = 3 \cdot 4 \cdot 5$).

To Alex's surprise, after throwing the darts, in each stage the scores obtained by the three darts are consecutive natural numbers. Moreover, the sum of the scores of two stages is equal to the sum of the scores of the other two stages.

# Task

Write a program that reads the total score $S$ and determines the smallest score that a dart can obtain for each stage.

# Input data

The input file `dartz.in` contains a single line with the natural number $S$.

# Output data

The output file `dartz.out` will contain a single line with four non-zero natural numbers $a$, $b$, $c$, $d$, each separated by a space, where $a$ represents the smallest score that a dart can obtain in the first stage, $b$ represents the smallest score that a dart can obtain in the second stage, $c$ represents the smallest score that a dart can obtain in the third stage, and $d$ represents the smallest score that a dart can obtain in the fourth stage.

# Constraints and clarifications

* $1 \leq S \leq 80 \ 000 \ 000$
* $S$ is a natural number
* There may be multiple solutions. Only one is required.
* For all the tests used in evaluation, a solution exists.

# Example

`dartz.in`
```
1560
```

`dartz.out`
```
3 8 3 8
```

## Explanation

A possible solution can be with the scores for each stage:

* stage $1$: $3$, $4$, $5$
* stage $2$: $8$, $9$, $10$
* stage $3$: $3$, $4$, $5$
* stage $4$: $8$, $9$, $10$

In stages $1$ and $3$, the scores obtained are $60$, while in stages $2$ and $4$, the scores are $720$. The total score is $60$ + $720$ + $60$ + $720$ = $1 \ 560$. It can be observed that the restriction "the sum of the scores obtained in two stages is equal to the sum of the scores from the other two stages" is satisfied ($60$ + $720$ = $60$ + $720$).