## Task

In modern table tennis, the speed of the game has increased considerably in recent times, and for this reason, most points are won following very short rallies. To adapt to this situation, professional players spend a significant portion of their training time studying and practicing ways to win the first few points of a rally. Specifically, we call the first ball the player's serve, the second ball the return of serve, and so on.

According to the new rules, a table tennis match consists of at most five sets, with the player who wins three sets first being the winner of the match. A set is played until one player reaches $11$ points and has an advantage of at least two points over the other player. The player who starts serving in the first set is determined by a coin toss. In a set, the serve changes every two serves, and if the score reaches $10 \\ - \\ 10$, the serve alternates at every point, and the set ends when one of the players has an advantage of two points. At the beginning of a set (except for the first one), the other player serves compared to who started serving in the previous set.

The probabilities $p_1, \\dots, p_5$ are known, with the meaning that the first player wins the point immediately with probability $p_i$ if he hits the $i$-th ball in a rally, and $q_1, \\dots, q_5$ have the same meaning for the second player. That is, the first player will immediately win the serve with probability $p_1$, and with probability $1 - p_1$, the point will continue with the second ball. In turn, the second player will immediately win the second ball with a probability of $q_2$, and with a probability of $1 - q_2$, the game will continue with the third ball, and so on. In other words, the probabilities of successful decisive shots are given, and it is assumed that there will be no unforced errors.
If a rally reaches the sixth ball, the first player will win the point with a probability of $p$, and the second player with a probability of $1 - p$.

## Task

Determine the probability that the first player will win the match.

## Input data

The first line of the input file `pingpong.in` contains five real numbers $p_1, \\dots, p_5$, with the meaning from the statement. The second line contains the numbers $q_1, \\dots, q_5$, and the third line contains the number $p$.

## Output data

In the output file `pingpong.out` print a single number with three **rounded** decimal places, representing the probability that the first player will win the match.

## Constraints and clarifications

* $0 < p_1, \\dots, p_5, q_1, \\dots, q_5 < 1$;

## Example

`pingpong.in`
```
0.9 0.5 0.5 0.5 0.5
0.6 0.5 0.5 0.5 0.5
0.2
```

`pingpong.out`
```
0.995
```