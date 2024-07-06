# Rugby Game

In the game of rugby, a team can score points in the following ways:
- 3 points for a converted penalty or drop goal (we are only interested in the number of points, not the method);
- 5 points for a try;
- Immediately after scoring a try, the team has the right to an additional penalty worth 2 points if it is converted.

Given a score, determine the number of ways it can be obtained.
Two ways to obtain a given score are different if the sequences of scores after each scoring differ in at least one position.

# Input data

The input file `rugby.in` contains on the first line two natural numbers $a$ and $b$, separated by a space, representing the scores of each team at the end of the game.

# Output data

The output file `rugby.out` will contain the remainder of the requested value divided by $1 \ 000 \ 000 \ 007$.

# Constraints and clarifications

* The numbers in the input file are natural, between $0$ and $1 \ 000$ inclusive.
* In the case of a score of $37$ points, we have $a \leq 30$ and $b \leq 30$.

# Example

`rugby.in`
```
10 3
```

`rugby.out`
```
9
```

## Explanation

Option 1: $(3 - 0, 8 - 0, 10 - 0, 10 - 3)$
Option 2: $(3 - 0, 3 - 3, 8 - 3, 10 - 3)$
Option 3: $(0 - 3, 3 - 3, 8 - 3, 10 - 3)$
Option 4: $(0 - 3, 5 - 3, 10 - 3)$
Option 5: $(0 - 3, 5 - 3, 7 - 3, 10 - 3)$
Option 6: $(5 - 0, 7 - 0, 10 - 0, 10 - 3)$
Option 7: $(5 - 0, 7 - 0, 7 - 3, 10 - 3)$
Option 8: $(5 - 0, 10 - 0, 10 - 3)$
Option 9: $(5 - 0, 5 - 3, 10 - 3)$

Notice that the option $(3 - 0, 8 - 0, 8 - 3, 10 - 3)$ is not possible because the two points (jump from $8$ to $10$) can only be obtained by the team that achieved a try, immediately after the try.