Here is the translated text:

---

Two teams, $F$ and $R$, each consisting of $n$ players, participated in the new edition of ktlon at $k$ events. After each event, $2 \cdot n$ values were recorded in the ktlon registry: the first $n$ represent the number of points won in the event by the team $F$ players, and the next $n$ represent the number of points won by the team $R$ players. For a team to win an event, at least one of its players must achieve a number of points strictly greater than each of the scores achieved by the players of the other team. The winning team of the event receives a number of stars. To determine the number of stars received, first, the number $M$ of players that achieved a number of points strictly greater than each of the scores achieved by the players of the other team is determined. Then the winning team receives a number of stars equal to the difference between the sum of the highest $M$ scores achieved by the players of the winning team and the sum of the highest $M$ scores achieved by the players of the other team.

For example, if the players of the two teams achieved scores $(8, 5, 8, 3, 9, 7)$ and $(5, 7, 5, 4, 5, 1)$, then $M = 3$ because three scores of the team $F$ players ($8$, $8$ and $9$) are higher than all scores achieved by the team $R$ players. Team $F$ wins the event and receives $8$ stars $= (9 + 8 + 8) - (7 + 5 + 5)$. If no player on either team achieves a number of points strictly greater than all the scores achieved by the players of the other team, the event ends in a draw and neither team receives any stars $(M = 0)$.

The competition is won by the team that accumulates the maximum number of stars at the end of all events.

# Task

Given $n$ – the number of players in each team, $k$ – the number of events, and for each event the scores achieved by the $2 \cdot n$ players of the two teams, determine:

1. the number of events won by team $R$;
2. the number of stars achieved by the winning team.

# Input data

The input file `ktlon.in` contains on the first line a number $C$ representing the task that needs to be solved ($1$ or $2$). The second line contains two natural numbers $n$ and $k$, which represent the number of players in each team and, respectively, the number of events, and on each of the next $k$ lines, $2 \cdot n$ natural numbers: the first $n$ represent the number of points won in the current event by the team $F$ players, and the next $n$ represent the number of points won by the team $R$ players. The numbers on the same line are separated by a space.

# Output data

If $C = 1$, the output file `ktlon.out` will contain the number of events won by team $R$. If $C = 2$, the output file will contain the number of stars won by the winning team.

# Constraints and clarifications

* $1 \leq C \leq 2$;
* $1 \leq n \leq 10\ 000$;
* $1 \leq k \leq 50$;
* The scores obtained by competitors are natural numbers between $0$ and $200\ 000$ inclusive.

|#|Score|Constraints|
|-|-|--------|
|1|35|$C = 1$|
|2|30|$C = 2$ and $M \leq 1$|
|3|35|$C = 2$ and $M \leq 5$|

# Example 1

`ktlon.in`
```
1
3 4
6 8 3 7 7 6
1 2 3 4 5 3
1 5 3 4 5 2
1 5 3 4 5 2
```

`ktlon.out`
```
1
```

## Explanation

The task $1$ is solved. The first event is won by team $F$ because there is a player who scored more points ($8$) than the points won by each team $R$ player ($7$, $7$, $6$). The second event is won by team $R$ because there are two players who scored more points ($4$ and $5$) than the points scored by each team $F$ player ($1$, $2$, $3$). The third event ended in a draw because no player on either team scored a number of points strictly greater than all the scores achieved by the players of the other team. The fourth event also ended in a draw, as all players achieved exactly the same scores as in the third event. The answer is $1$ because team $R$ won one event.

# Example 2

`ktlon.in`
```
2
3 3
8 8 5 7 7 7
1 2 3 3 5 3
4 1 2 6 5 1
```

`ktlon.out`
```
7
```

## Explanation

The task $2$ is solved. Team $F$ wins the first event and receives $2$ stars ($M = 2$, $(8 + 8) - (7 + 7) = 2$).
Team $R$ wins the second event and receives $2$ stars ($M = 1$, $5 - 3 = 2$). Team $R$ wins the third event and receives $5$ stars ($M = 2$, $(6 + 5) - (4 + 2) = 5$). In total, team $F$ received $2$ stars while team $R$ received $7$ stars. The competition is won by team $R$ with $7$ stars.

