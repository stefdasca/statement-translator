---

An undercover agent has a map marking $N$ military objectives. He is initially located at the objective numbered $1$ (his own military base) and must reach the objective numbered $N$ (the enemy's military base). To achieve this, he will use the existing roads, each road connecting 2 distinct objectives. Since the mission is secret, the agent will move at night; therefore, he needs a flashlight. For this, he has to choose between $K$ types of flashlights – a flashlight of type $W$ ($1 \leq W \leq K$) has batteries that allow a consumption of $W$ watts; after consuming these watts, the flashlight no longer illuminates. Fortunately, some of the objectives are friendly military bases, so once he gets there, he can fully recharge his flashlight's batteries. The agent has to ensure that before moving on a road between two objectives, the amount of watts he can still consume is greater than or equal to the amount of watts required for that road.

Given the roads between objectives and, for each road, the duration needed to traverse the road and the number of watts consumed by the flashlight, determine the type of flashlight with the smallest number such that the travel duration is minimized (among all types of flashlights with which the minimum time to reach the destination can be achieved, the flashlight with the lowest consumption is of interest).

# Input data
The first line of the file `lanterna.in` contains the integers $N$ and $K$, separated by a space. The following line contains $N$ integers from the set $\{0,1\}$. If the $i$-th number is $1$, it means that the objective numbered $i$ is a friendly military base (i.e., the agent can recharge the flashlight's batteries if he reaches this objective); if the number is $0$, the agent will not be able to recharge the batteries. The first number in line is $1$, and the last one is $0$. The third line of the file contains the number $M$ of roads between objectives. Each of the next $M$ lines contains 4 integers separated by spaces: $a\ b\ T\ W$, signifying that there is a bidirectional road between objectives $a$ and $b$ ($a ≠ b$), which can be traversed in time $T$ with a consumption of $W$ watts.

# Output data
The file `lanterna.out` will contain two integers, separated by a space: $T_{min}$ and $W_{min}$. $T_{min}$ represents the minimum possible duration of the travel from objective $1$ to objective $N$, and $W_{min}$ represents the type of flashlight with the smallest number for which this time is achieved.

# Constraints and clarifications
* $2 \leq N \leq 50$
* $1 \leq K \leq 1\ 000$
* $1 \leq M \leq N(N-1)/2$
* Between two different objectives, there can exist at most one direct road.
* For each road, the travel duration is an integer between $1$ and $100$, and the number of watts consumed is an integer between $0$ and $1\ 000$.
* It is guaranteed that there is at least one type of flashlight for which the travel is possible.
* The score for a test will be awarded as follows:
  * 30% if $T_{min}$ is determined correctly
  * 100% if both $T_{min}$ and $W_{min}$ are determined correctly

# Example

`lanterna.in`
```
7 10
1 0 1 0 0 0 0
7
1 2 10 3
1 4 5 5
2 3 10 3
4 3 15 1
3 6 4 3
6 5 2 2
5 7 1 0
```

`lanterna.out`
```
27 6
```

