## Psychtraining

Although the national soccer team qualified for Euro 2016, the fans are not very satisfied with the team's performance. The coach has been replaced, after an intense scouting campaign, by Marius Dumitran, who will manage the team from London. Marius realized that many of the national team's problems stem from the players' psychology. Today Marius wants to resolve the rivalries within the team. He numbered the players in the extended squad from $1$ to $N$. He also noted the $M$ rivalries within the team. He wants to organize a number of matches during the training sessions so that any $2$ players who are rivals play against each other at some point. In each match, he will divide all players into exactly $2$ teams, not necessarily equal, and one of them could be empty. Marius doesn't have time to organize the matches now, but he will buy you a certain alcoholic drink if you do it for him. Since the players have gained weight due to the same alcoholic drink, they should not play too many matches. More precisely, your solution will score on the test only if the number of matches is at most $10$.

## Input data

The input file `psychtraining.in` will contain on its first line the numbers $N$ and $M$, representing the number of players in Romania's extended squad and the number of rivalry relationships among them. It will be followed by $M$ lines, each containing a pair of numbers $X$ $Y$, indicating that player number $X$ and player number $Y$ have a fierce rivalry.

## Output data

The output file `psychtraining.out` will contain on its first line the number $MATCHES$. This is the number of matches played in your solution, and it must be at most $10$. The next $MATCHES$ lines will contain a string of length $N$ with characters from the set $\{'a', 'b'\}$. If the position $i$ of the string contains the character $a$, then the $i$-th player will be in the first team, otherwise, they will be in the second team. The order of the teams is irrelevant, i.e., the strings `aba` and `bab` are identical.

## Constraints and clarifications

$1 \leq N \leq 500$

$1 \leq M \leq N * (N - 1) / 2$

## Example

`psychtraining.in`

```
3 2
1 2
1 3
```

`psychtraining.out`

```
2
aab
aba
```

## Explanation

There are rivalries between players $1$ and $3$, and between $1$ and $2$. We notice that there is a solution with a single match played, between the teams $\{1\}$ and $\{2, 3\}$ (coded by the string "abb" or "baa"). However, the solution in the example is also correct since the number of matches is less than or equal to $10$.