
# Statement

Miguel, the new mayor, needs help to optimally place the city hall. He can choose between $N$ buildings that are connected with $N - 1$ one-way roads. If we do not consider the orientation of the roads, all buildings are connected to each other. Also, each road has an associated coefficient $G$, the number of daily users.

The city hall should be accessible from any other building, but this might not always be possible. Thus, Miguel is willing to reverse the direction of some roads. Being a good mayor who cares about the citizens, he wants to reverse the roads in such a way that a minimum number of people are affected by the changes.

Miguel wants you to tell him the minimum number of people affected and the minimum index of a building for which this minimum number is obtained.

# Input data

The input contains a natural number $N$ (the number of buildings) and $N - 1$ triplets of natural numbers $X, Y, C$ indicating that there is a one-way road between buildings $X$ and $Y$, used by $C$ people.

# Output data

Print, separated by a space, the minimum number of people affected and the smallest index of a building for which this minimum number can be obtained.

# Constraints and clarifications

* $2 \leq N \leq 100\ 000$
* The buildings are indexed from $1$ to $N$
* $1 \leq X, Y \leq N$
* $0 \leq C \leq 1\ 000\ 000$

# Example

`stdin`
```
9
2 3 2
6 3 1
5 2 0
5 7 4
5 8 3
8 4 2
9 5 3
1 7 1
```

`stdout`
```
6 4
```

# Explanation

This is the representation of the example:

~[miguel-and-the-city-hall.png]

Choosing building 4 to be the city hall results in the minimum number of people being affected: those who use the roads $5 \to 7$ and $2 \to 3$.
