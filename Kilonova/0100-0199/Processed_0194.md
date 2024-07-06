On the ground near the town of Gheorgheni, all the children have gathered and want to organize a rather special game. The children were numbered from $1$ to $N$ and we know who each child's friends are.

A *team* is a maximal group of children with the property that for any children $P$ and $Q$ in the team, there exists a sequence of children $C_1, \dots, C_k$ such that $P=C_1$, $Q=C_k$, and for any $1 \leq i < k$, $C_i$ is friends with $C_{i+1}$.

Each team will receive a *code*, equal to the smallest ordinal number of a child from the respective team.

We want to find out who the *vulnerable children* are, that is, those children who, if removed, would break their team into two or more teams.

# Task
Write a program to identify all the teams formed according to the rules above, as well as the vulnerable children.

# Input data
The input file `pamant.in` contains:
- The first line contains two natural numbers $N$ and $M$ representing the number of children and the number of friendship relations, respectively;
- The next $M$ lines contain two distinct natural numbers $x$ and $y$, meaning $x$ and $y$ are the ordinal numbers of two children in a friendship relation.

# Output data
* The first line of the output file `pamant.out` contains a single natural value $A$, representing the number of teams.
* The second line contains $A$ natural numbers separated by a space representing the team codes, in ascending order.
* The third line contains a natural value $B$ representing the number of vulnerable children.
* The fourth line contains $B$ natural values, separated by a space, representing the ordinal numbers, written in ascending order, of the vulnerable children.

# Constraints and clarifications
* $1 \leq N \leq 100\ 000$
* $1 \leq M \leq 200\ 000$
* $40\%$ of the score is awarded for the correctness of the first two lines of the output file and $60\%$ for the other two lines.
* Friendship relations are reciprocal: if $x$ is friends with $y$, then $y$ is friends with $x$.
* If $x$ is friends with $y$ and $y$ is friends with $z$ it does not mean that $x$ is friends with $z$.
* For $30\%$ of the tests $N \leq 1\ 000$.

# Example

`pamant.in`
```
10 7
1 2
2 8
4 6
3 5
3 10
5 10
5 7
```

`pamant.out`
```
4
1 3 4 9
2
2 5
```

Explanation
---

There are $4$ teams, namely:
- the first team: $(1,2,8)$
- the second team: $(3,5,7,10)$
- the third team: $(4,6)$
- the fourth team: $(9)$

There are two special children, namely $2$ and $5$.