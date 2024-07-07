# Statement
Ducks are majestic and highly intelligent beings, but, like all beings, they are not perfect. They find it very difficult to recognize each other.

The Kingdom of PinkLand has a square shape and is divided into $N \times N$ provinces. Each province is governed by a noble whose power is given by the number of ducks in his province. We denote the power of the province at coordinates $(i, j)$ by ${P_i}_j$.

The kingdom is ruled by King Duckie, who has come up with an ingenious way to be more recognizable to the other ducks; he wears a pink cloak. Unfortunately, one day, while he was walking through the forests around the kingdom and lying on the grass, his cloak turned green. He has a spare cloak at his palace, which is located in the plot at coordinates $(N, N)$, but to get there, he has to pass through other provinces. He can travel north, south, east, or west at each step provided that he does not leave the kingdom. He can pass through a province only if his power is strictly greater than the power of the noble in that province. The power of a province is equal to the number of ducks in that province. **More seriously!** For unknown reasons, the power of each province increases as the king moves! Specifically, at time $t$, the power of the province at coordinates $(i, j)$ will be ${P_i}_j + t \times {Q_i}_j$. The king's movement is done within one unit of time, and the initial time moment is $t_0 = 0$. Since his initial power is $0$, he seeks the help of King Vilci from the Kingdom of Duckopolis to send him some ducks to accompany him to the palace so he can pass through the provinces. King Vilci agrees but, due to the path to Duckie being guarded by the famous duck hunter Chertes, he wants to risk as few lives as possible to help his friend. Help Vilci determine the smallest number of ducks that need to be sent.

A duck sent by Vilci has a power of $1$.

# Task
Given the natural numbers $T$, $N$, and $T$ matrices of $N$ rows and $N$ columns each representing the number of ducks in each province of the Kingdom of PinkLand, display the minimum number of ducks that need to be sent.

# Input Data
In the file $ducks.in$, the number $T$ is provided, representing the number of tests. For each test, the first line contains the natural number $N$, and the following $N$ lines contain $N$ natural numbers each, representing the initial power of a province, the array ${P_i}_j$. The next $N$ lines contain $N$ natural numbers each, representing the power increase of each province, the array ${Q_i}_j$.

# Output Data
In the file $ducks.out$, print $T$ natural numbers $X$, each on a separate line, where the natural number $X$ on the $i$-th line is the minimum number of ducks that Vilci will send to help his friend Duckie on the $i$-th test.

# Constraints and Clarifications
* $1 \leq T \leq 10$
* $1 \leq N \leq 500$
* $1 \leq {P_i}_j \leq 10^{9}$, $1 \leq i \leq N$, $1 \leq j \leq N$, where ${P_i}_j$ represents the power of the noble in the province at row $i$ and column $j$.
* $1 \leq {Q_i}_j \leq 10^{9}$, $1 \leq i \leq N$, $1 \leq j \leq N$, where ${Q_i}_j$ represents the power increase of the noble in the province at row $i$ and column $j$.
* **King Duckie can pass through a province if at the time when he enters the province his power is strictly greater than the power of the noble.**
* For tests worth $30p$, we have $1 \leq {P_i}_j, {Q_i}_j \leq 100$
* King Duckie starts from the province in the corner (1, 1)

# Example
`ducks.in`
```
1
6
0 36 79 85 87 82
26 46 55 39 74 19
89 73 65 31 36 18
99 39 8 17 47 58
6 44 80 29 73 90
54 40 79 57 19 11
0 36 79 85 87 82
26 46 55 39 74 19
89 73 65 31 36 18
99 39 8 17 47 58
6 44 80 29 73 90
54 40 79 57 19 11
```
`ducks.out`
```
514
