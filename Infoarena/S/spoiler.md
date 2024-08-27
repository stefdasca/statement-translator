# Spoiler

John and Charlie are passionate fans of the game Starcraft and love watching replay matches. Tonight, they are watching a replay of a match between two top players, HerO and Maru. The match is a best-of-$N$, meaning that the two will compete in multiple rounds until one of them wins the majority of the $N$ rounds ($N$ is an odd number). If a player reaches a majority before $N$ rounds, they win immediately (the remaining rounds are not played). For example, a best-of-$7$ match ends when a player wins $4$ times, so the match can last between $4$ rounds (which ends with $4-0$) and $7$ rounds (which ends with $4-3$). There are no ties in Starcraft, and HerO and Maru have equal chances of winning each round. John accidentally peeked at the list and saw that the match lasted $K$ rounds. Charlie does not know $K$. This spoils John's enjoyment, as he likes to watch only interesting rounds, rounds whose winner is not known in advance. John can also predict the outcome of a round, carelessly saying "I know who will win the next round", at which point he tells Charlie the value of $K$.

## Task

Given $N$ and $K$, what is the expected number of interesting rounds that can be watched tonight, from Charlie's perspective?

## Input data

The input file `spoiler.in` contains a single line that contains the values $N$ and $K$.

## Output data

The output file `spoiler.out` must contain the answer as an irreducible fraction. Print the numerator on the first line and the denominator on the second.

## Constraints and clarifications

$1 \leq N \leq 2000$

$N$ is odd.

$(N + 1) / 2 \leq K \leq N$

For $20\%$ of the tests $N < 50$

For $60\%$ of the tests $N < 300$

For $80\%$ of the tests $N < 1600$

## Example

`spoiler.in`
`spoiler.out`
7 4 
1 1

## Explanation

In this case, only the first round is interesting. Because the match lasts $4$ rounds, it must end $4-0$. Therefore, whoever wins the first round must win all rounds, making rounds $2$, $3$, and $4$ uninteresting.

## Example

`spoiler.in`
`spoiler.out`
5 4 
5 2

## Explanation

We know that this match will end $3-1$ (or $1-3$). The first two rounds will be interesting because the winners cannot be predicted. However, after these rounds, the score can be:

- $2-0$ with a $25\%$ chance. In this case, the last two rounds will not be interesting, as the score can only become $2-1$, and then $3-1$.
- $0-2$ with a $25\%$ chance. Similar to the above case, the last $2$ rounds will not be interesting.
- $1-1$ with a $50\%$ chance. In this case, the third round will also be interesting. Yet, whoever reaches $2-1$ will win the fourth round with $3-1$, so it will not be interesting.