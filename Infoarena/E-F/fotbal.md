# Football

In a football championship, $n$ teams will play in a group such that each team plays against all the others. The number of rounds will be $n–1$ if $n$ is even, otherwise $n$, for odd $n$. For a victory, a team receives 3 points, for a draw 1 point, and if a team loses, it receives no points. In case of equal points, the direct result matters, and if the two teams had a draw, the goal difference (difference between the goals scored and the goals conceded) matters. In case of equal goal difference, the number of goals scored matters. If two teams are still tied, the winner is decided by a coin toss. If there are more than two teams tied in points, a separate table is created with their results and the above rules are applied. If order cannot be decided even by this process, it is decided by a coin toss. Knowing the match results, determine the ranking, and in the case of teams tied in points with other teams, the best and worst position they could be in.

## Input data

The first line of the input file `fotbal.in` contains a natural number $n$, representing the number of teams in the group. Then follows $n–1$ (for even $n$), or $n$ (for odd $n$) groups of $\left\lfloor\frac{n}{2}\right\rfloor$ lines, which describe the unfolding of the rounds. Each line contains two natural numbers, representing two teams by their order numbers (indicating a confrontation between the two teams), followed by two numbers representing the number of goals scored by the two teams. The numbers are separated by a space.

## Output data

In the output file `fotbal.out` $n$ lines will be written. On each line there will be two natural numbers, separated by a space, representing the best and worst position the respective team can be in. The $i$-th line will describe the situation of the $i$-th team.

## Constraints and clarifications

$2 \leq n \leq 5$  
The scheduling of the matches is guaranteed to be correct, meaning each team will play against all other teams exactly once.  
The number of goals scored by a team in a match will not exceed 10.

## Example

`fotbal.in`
```
2
2 1 1 0
```

`fotbal.out`
```
1 1
1 1
```

## Explanation

We have two teams, so we will have a single match. In this match, the second team wins 1 to 0, so it is the winner of the championship.