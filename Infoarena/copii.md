# Children

Laura went on a trip with $N$ children. There are friendship relations between some children, but the friendship relation is not necessarily reciprocal. Laura wants to organize a game for the children to get to know each other better. For the game to run smoothly, she needs to divide the children into multiple teams, at least two. We call the set of friends of a team the set consisting of the children who are considered friends by at least one of the members of that team. Laura has to divide the children in such a way that for each team, the set of friends of that team contains at least one child from each of the other teams.

## Task

Knowing the friendship relations between the children, determine how many ways Laura can form the teams for the game.

## Input data

The input file `copii.in` contains on the first line the natural number $N$. The following $N$ lines contain $N$ characters from the set $\{'0', '1'\}$. The $j$-th character $(1 \leq j \leq N)$ on line $i+1$ $(1 \leq i \leq N)$ in the file is '1' if the $i$-th child considers the $j$-th child a friend, and '0' otherwise.

## Output data

The output file `copii.out` contains a single natural number representing the number of ways Laura can divide the children into teams.

## Constraints and clarifications

$1 \leq N \leq 10$

The $i$-th character on line $i$ $(1 \leq i \leq N)$ will always be '0'.

## Example

`copii.in` `copii.out` 
```
3
010
101
110
3
```
```
2
01
10
1
```

## Explanation

For the first example, there are 3 ways to split the children into teams: $(1, 2)$ $(3)$; $(1, 3)$ $(2)$; $(1)$ $(2, 3)$.

For the second example, the only correct way to divide the children into teams is $(1)$ $(2)$.