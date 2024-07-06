We are at a certain point in the national football championship. Some matches have been played, others are yet to be played. The number of points accumulated by each team before the remaining matches is known. It is also known that a match can end in a draw, in which case each team receives one point, or with the victory of one of the teams, in which case that team receives three points, and the other zero points.

# Task

We need to answer two types of questions:
1. Which teams would be in the first place if all remaining matches ended in a draw? A team is in the first place if it has the maximum number of points.
2. Which teams depend solely on their results to become champions? A team becomes a champion (wins the championship) if it finishes with a number of points strictly greater than any other team. We say that a team depends solely on its results to become a champion if it becomes a champion by winning all the matches it still has to play, regardless of the results of the other matches.

# Input data

The input file `campionat.in` contains on the first line a number $T$, representing the type of question ($1$ or $2$). The second line contains a number $N$ representing the number of teams in the championship (we consider that the teams are labeled with distinct numbers from $1$ to $N$). The third line contains $N$ natural numbers separated by a space, the $i$-th number representing the score of the $i$-th team. The fourth line contains a number $D$, representing the number of remaining matches. On each of the next $D$ lines are two distinct numbers $i, j$, ranging between $1$ and $N$, meaning that teams $i$ and $j$ have a remaining match to play.

# Output data

The output file `campionat.out` will contain one single line.

If $T = 1$, the line will contain the labels of the teams that finish in the first place, in case all remaining matches end in a draw.
If $T = 2$, the line will contain the labels of the teams that depend solely on their results to become champions. If no team can become a champion depending only on its own results, the output file will only contain the number $0$.
For both $T = 1$ and $T = 2$, the labels of the teams will be written in ascending order, separated by a space.

# Constraints and clarifications

* $2 \leq N \leq 1\ 000$;
* $1 \leq D \leq 500\ 000$;
* The initial scores of the teams are natural numbers at most equal to $1\ 000$.
* The rules of the championship are more peculiar; you do not need to question whether it is possible for the teams to have the given scores following the matches already played (we assume that up to this point the federation has awarded various bonuses and penalties).
* If among the remaining matches to be played there is one that appears multiple times (either in the form $(i, j)$ or $(j, i)$), it will be played only once.
* The scheduling of the matches was made in a disorderly manner, so it is possible that some teams still have to play more matches than others, and some even have no remaining matches to play.
* For tests worth $22$ points, $T = 1$.
* For other tests worth $9$ points, $T = 2$ and each team has to play exactly $2$ matches with other teams.
* For other tests worth $8$ points, $T = 2$ and each team has to play one match with every other team.
* For other tests worth $10$ points, $T = 2$ and there is one single team that plays one match with every other team, the other teams having no remaining matches to play.

# Example 1

`campionat.in`
```
1
4
2 3 2 1
3
1 3
1 2
3 1
```

`campionat.out`
```
1 2
```

## Explanation

Team $2$ has only one match to play against team $1$, and the second match will be played between teams $1$ and $3$ (even if the pair $1 \ 3$ appears twice in the list, it is only one match).
The two matches will end in a draw, and thus the final scores of the teams will be: $4 \ 4 \ 3 \ 1$. Therefore, teams $1$ and $2$ end up in the first place.

# Example 2

`campionat.in`
```
2
4
1 3 2 1
3
1 3
1 2
3 1
```

`campionat.out`
```
1 2
```

## Explanation

Team $1$ becomes champion if it wins both matches, no other team being able to match or surpass it in points.
Also, team $2$ becomes champion if it defeats team $1$ in the remaining match, regardless of the result of the other match. Team $3$, even if it wins the match against team $1$, does not depend solely on its result because team $2$ would surpass it in points if it also won the match it still has to play.