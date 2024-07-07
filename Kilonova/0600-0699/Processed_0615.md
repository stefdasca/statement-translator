~[dirijor.jpeg|align=right|width=30%]
Conductors always travel from one part of the world to another, needing to visit many concert halls. Specifically, the great conductor Scuțescu is in the land of Euphonia and has to conduct multiple concerts.

The land is linear, being a sequence of $N + 1$ towns, where each road between two adjacent towns has a ticket price (in euphoric marks) for bus tickets. We denote the price of the ticket that the conductor has to pay to travel from town $i$ to $i + 1$ or vice versa by $A_i$.

The conductor is initially in town $1$ and follows to perform $P$ concerts. Because he likes to travel from one end of the world to the other, he has scheduled all his concerts in towns $1$ and $N + 1$ as follows: the first concert is in town $N + 1$, the second concert is in town $1$, the third concert is in town $N + 1$, the fourth concert is in town $1$, and so on. The concerts have to be performed in order.

For every trip from $1$ to $N + 1$ or vice versa, a stopover is made (i.e., from $1$ to $x$ to $N + 1$ or from $N + 1$ to $x$ to $1$, where $1 < x < N + 1$). The price of a stopover is the maximum price among all the bus tickets used on that route that haven't been bought yet. In other words, for a stopover, the maximum value from the traversed subarray is paid, and that maximum value is replaced with $0$, and when the conductor makes a trip from the town from which he departs to the stopover, or from the stopover to the town where he has to perform a concert, he is not allowed to travel for free.

For example, for the array $A$ of costs $2, 5, 6, 3, 4, 9, 12, 7$, if we make a stopover in town $4$, we would have to pay $\max(2, 5, 6) + \max(3, 4, 9, 12, 7)$, i.e., 18 euphoric marks, and the array will transform into $2, 5, 0, 3, 4, 9, 0, 7$.

# Task

Determine the minimum cost the conductor can pay to perform all the $P$ concerts.

# Input data

The first line contains the numbers $N$ and $P$. The second line contains $N$ natural numbers, representing the elements of the array $A$.

# Output data

Print the minimum cost that the conductor has to pay to make his journey.

# Constraints and clarifications
* $1 \leq 2 \cdot P \leq N \leq 5\ 000$
* $\sum_{i = 1}^{i \leq N} A_i \leq 2\ 000\ 000\ 000$
* All values in $A$ are distinct.

## Subtask 1 (6 points)
* $1 \leq N \leq 15$
## Subtask 2 (9 points)
* $1 \leq N \leq 250$, $1 \leq P \leq 15$
## Subtask 3 (17 points)
* $1 \leq N \leq 250$
## Subtask 4 (17 points)
* $1 \leq N \leq 3\ 000$
## Subtask 5 (51 points)
* Without additional restrictions

# Example
`stdin`
```
9 4
4 5 8 6 3 2 7 1 9
```
`stdout`
```
41
