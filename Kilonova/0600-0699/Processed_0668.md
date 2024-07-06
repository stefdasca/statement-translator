```markdown
Stefan is a big football fan and he's also interested in various statistics related to his favorite sport. Today he read about some past football competitions which involved group stage events and he's now stuck with trying to solve this problem:

Given the final results of a round robin round (each team plays against each team twice), help Stefan find whether there is a unique way of assigning the results for each match such that we end up having the final standings given in the input. Since the data can be faulty, there can also be a chance of having invalid group stages, so you will also have to help Stefan find them out.

In order to make this easier for you, Stefan sorted the teams in decreasing order of points gained, and if two or more teams have the same number of points, they are ordered in decreasing order of wins. This is also true for the groups which are not valid. Furthermore, he doesn't care about the permutations of the teams in the standings, so you can assume that the first team gets the first place, the second team gets the second place and so on. 

In short, you have to print one of the three following strings:

Unique, if the group results are valid and there is only one way of distributing the results in order to end up getting the final table from the input.

Not unique, if the group results are valid and there is more than one way of distributing the results in order to end up getting the final table from the input.

Invalid, if the group results are not valid. 

Since Stefan is ambitious, he wants you to find the results for $t$ such final tables. 

# Input

The first line contains $t$, the number of test cases.

On the first line of the input for each test you will have $n$, the number of teams playing.

On the next $n$ lines you will have $3$ integers, representing the number of wins, the number of draws and the number of losses the team got. The integers are *NOT* separated by spaces. 


# Output

The output file will contain $t$ lines, each of them containing the answer corresponding to that test case.

# Constraints

* $1 \leq t \leq 10^5$
* $2 \leq n \leq 4$
* For tests worth $10$ points, $n = 2$
* For tests worth $20$ more points, $2 \leq n \leq 3$
* For tests worth $10$ more points, $1 \leq t \leq 10$
* For tests worth $10$ more points, there are only valid group tables.

# Example

`stdin`
```
2
4
600
402
204
006
4
402
402
402
006
```

`stdout`
```
Unique
Not unique
```

## Explanation

For the first testcase, the results are unique because we can uniquely determine that the first team won all the games against all other teams, the second team won all the games except for the ones lost against the first team and the third team won all the games against the fourth team.

For the second testcase, while we can uniquely determine that the fourth team lost twice against each other team, there are at least two ways of assigning game results such that each of the first three teams won twice and lost twice against the other two teams.
```