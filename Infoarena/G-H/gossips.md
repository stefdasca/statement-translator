## Task

Poli is in her first year at college. Even though she went to one of the best universities, she quickly realized that all her colleagues were divided into $N$ groups of friends, with the main purpose of these groups being to spread gossip. Poli knows that each group $i$ is composed of one or more subgroups so that any subgroup can be part of only one group. Let's assume that group $i$ learns a piece of gossip about group $j$: then all of $i$'s subgroups (and subgroups' subgroups, etc.) and all the groups that $i$ is a part of know the gossip about group $j$. Moreover, all these groups know the gossip about every group that $j$ is part of (but know nothing about $j$'s subgroups, as those members may not be involved in the gossip). Since Poli is friends with all her colleagues, she knows when gossip occurs (i.e., when a group $i$ learns a piece of gossip about a group $j$). Now, she wants to answer questions in the form: "Does group $i$ know a piece of gossip about group $j$?" quickly. Unfortunately, Poli's college is quite large, so you need to help her.

## Input data

The first line of the `gossips.in` file contains three numbers $N$ – the number of groups, $M$ – the number of relationships between groups, and $Q$ – the number of queries. The next $M$ lines contain the form $a$ $b$ indicating that group $b$ is part of group $a$. The following $Q$ lines each contain three numbers: $s$ – the type of query and $x$ $y$ – two groups. If $s$ is $1$ then you need to respond with `"YES"` if group $x$ knows at least one piece of gossip about group $y$ or `"NO"` otherwise. If $s$ is $2$ then group $x$ has just learned a piece of gossip about group $y$.

## Output data

The `gossips.out` file must contain multiple lines, one for each query of type $1$, each line being `"YES"` or `"NO"` (without quotes).

## Constraints and clarifications

$1 \leq N, Q \leq 100\ 000$

$1 \leq M < N$

$1 \leq x, y \leq N$

if a group $i$ knows a piece of gossip about a group $j$, it doesn't mean that $j$ knows a piece of gossip about $i$

## Example

`gossips.in`
```
9 7 7
6 1
6 2
7 6
7 3
8 4
8 5
9 7
2 6 4
2 8 6
1 2 4
1 2 5
1 4 7
1 8 1
1 5 9
```

`gossips.out`
```
YES
NO
YES
NO
YES
```