## Task

On the island of Lian Yu, there are $N$ settlements, numbered from $1$ to $N$, connected by $M$ bidirectional roads. On this island, the notorious Slade Wilson cultivates the most dangerous drug and also the most dangerous weapon, Mirakuru. A.R.G.U.S has discovered this operation and wants to send $K$ teams of soldiers to investigate and obtain essential information. However, this task is not that simple, and therefore, A.R.G.U.S has hired you three to determine the minimum cost to send $K$ teams of soldiers to the island given the following conditions:
- Due to the structure of the island, in each settlement $i$, a maximum of one team of soldiers can be dropped by planes at a cost of $cost_i$.
- After landing, the teams need to meet in one settlement to continue the plan.
- Due to the sudden intervention of the squad and the aerial support, the soldiers will be able to eliminate all of Slade Wilson's mercenaries present in the settlements where they land.
- As soon as the soldiers land, an alarm will be raised throughout the island, and all the mercenaries will take as much Mirakuru as possible and gather in one of the settlements to protect it (and most likely, if the soldiers go through this settlement, they will be killed, which is totally unacceptable). Therefore, the teams must be placed in such settlements that, in any of the remaining ones where Slade Wilson's mercenaries gather, the soldiers can meet in a settlement without passing through the one chosen by Slade Wilson and his team.

## Input data

The input file `lianyu.in` contains on the first line three natural numbers $N$ (the number of settlements), $M$ (the number of roads), and $K$ (the number of teams that need to be sent). The next line contains $N$ natural numbers separated by spaces, the $i$-th being $cost_i$. On the next $M$ lines, there are two natural numbers $x$ and $y$ indicating that there is a bidirectional road between settlements $x$ and $y$.

## Output data

The output file `lianyu.out` will contain a single natural number representing the minimum cost to send $K$ teams to the island with the above constraints.

## Constraints and clarifications

$1 \leq K \leq N \leq 3000$

$1 \leq M \leq 5000$

$1 \leq cost_i \leq 10^5$

It is possible to reach any settlement from any other by traveling on the $M$ roads.

Between any two settlements, there is at most one road, and there is no road from a settlement to itself.

## Example

`lianyu.in`

```
5 5 2
2 4 1 4 1
1 2
2 3
3 4
1 4
4 5
```

`lianyu.out`

```
3
```

## Explanation

Teams are sent to settlements $1$ and $3$. A better cost could be obtained by sending teams to settlements $3$ and $5$, but if the mercenaries gather in settlement $4$, then the team in settlement $5$ would no longer be able to meet the one in settlement $3$.