> Now we can devour gods, TOGETHER!

Gimi found a new game, famous for its high difficulty. The game consists of $N$ rooms, numbered from $1$ to $N$. Each room $i$ contains a monster whose power is a natural number $P_i$. Gimi passes, in order, through all the rooms. In each room, he can choose to fight the monster or not.

Gimi starts with a sword of durability $S$. He defeats a monster only if its power is less than or equal to the sword's durability. After the fight, the sword's durability decreases by the monster's power. For example, if Gimi has a sword of durability $10$ and fights a monster with power $4$, then the sword's durability will decrease to $6$.

Keeping up with his reputation, Gimi wants to fight exactly **3 monsters** of increasing power. In other words, if Gimi defeats a monster with power $x$, he will continue to fight only monsters with power strictly greater than $x$.

# Task
Gimi wonders in how many ways he can choose **3 monsters** to fight. Two sets of 3 monsters are considered different if there is at least one monster in the first set which does not belong to the second set.

Formally, find the number of triples $i < j < k$ for which $P_i < P_j < P_k$ and $P_i + P_j + P_k \\leq S$.

# Input data
The input file contains the first line two natural numbers $N$ and $S$, representing the number of rooms in the game and the initial durability of Gimi's sword, and the second line contains $N$ natural numbers $P_i$ separated by a space, representing the powers of the $N$ monsters.

# Output data
The output file will contain a single number representing the total number of ways Gimi can choose the monsters.

# Constraints and clarifications
- $1 \\leq N \\leq 10\\ 000$.
- $1 \\leq P_i, S \\leq 1\\ 000\\ 000\\ 000$, for any $1 \\leq i \\leq N$.

|#|Points|Constraints|
|-|-|--------|
|1|11|$1 \\leq N \\leq 100$|
|2|27|$1 \\leq N \\leq 2\\ 000$|
|3|62|No other constraints|

# Examples
`bossfight.in`
```
5 9
1 2 3 4 3
```
`bossfight.out`
```
5
```
The triples of positions are: $(1,2,3)$, $(1,2,4)$, $(1,2,5)$, $(1,3,4)$, $(2,3,4)$.
An example of an incorrect triple is $(1,4,5)$, because the power of the monster in room $4$ is greater than the power of the monster in room $5$.

\
`bossfight.in`
```
8 16
4 2 1 6 5 7 9 8
```
`bossfight.out`
```
13
```
The triples of positions are: $(1,5,6)$, $(2,4,6)$, $(2,4,8)$, $(2,5,6)$, $(2,5,7)$, $(2,5,8)$, $(3,4,6)$, $(3,4,7)$, $(3,4,8)$, $(3,5,6)$, $(3,5,7)$, $(3,5,8)$, $(3,6,8)$.
