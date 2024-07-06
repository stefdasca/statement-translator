*Stellar Date 3210:*

The captain of the USS Enterprise, Jean-Luc Picard, is on an important mission in the Beta Quadrant of the galaxy.

He must travel as quickly as possible from the planet Vulcan to the planet Qo'noS, but due to certain restrictions for this mission, Jean-Luc Picard will not be able to instantly reach his destination using the ship's warp drive, but will have to travel normally from sector to sector.

The galaxy map is represented in the form of a two-dimensional table of size $N \times N$, where each cell represents a sector of the galaxy. The coordinates of the sector where the planet Vulcan is located are $(x_s, y_s)$, and the coordinates of the sector where the planet Qo'noS is located are $(x_f, y_f)$.

The USS Enterprise can move in one unit of time from one sector to any of the adjacent sectors, either on the same row or same column. Additionally, the ship can remain stationary for an indefinite period in any sector. The ship can only be in a sector that is not currently posing any danger.

Because no adventure is devoid of dangers, Jean-Luc Picard’s path is scattered with *pulsars*, very dangerous cosmic objects that launch gravitational waves at fixed time intervals in their vicinity, which could destroy the USS Enterprise.

A pulsar $P_i$ is characterized by four variables $(x_i, y_i, r_i, t_i)$, where $(x_i, y_i)$ represents the coordinates of the sector where the pulsar is located, $r_i$ represents the pulsar's range, and $t_i$ represents the state the pulsar is in at the starting moment of the ship's journey.

A pulsar $P_i$ periodically goes through a number of $r_i$ states from 0 to $r_i - 1$. When it is in state $t$, it affects all sectors at a Manhattan distance less than or equal to $t$ from the sector where it is located. If the pulsar at a certain time is in state $t$, at the next moment it will be in state $(t+1) \% r_i$.

An example of the functioning of a pulsar with a range of $r = 4$, over $6$ units of time, starting with $t = 0$ is as follows:

~[exemplu1.png]

# Task

Your task is to help Jean-Luc Picard by answering one of the following questions knowing the galaxy map:
1) What is the maximum number of galaxy sectors $S_{max}$ affected at any moment by at least one pulsar.
2) What is the minimum time $T_{min}$ Jean-Luc Picard needs to reach the planet Qo'noS.

# Input data
From the file `pulsar.in` the following will be read:
* The first line will contain three numbers $C$, $N$, and $P$ separated by spaces, representing the task to be solved, the size of the galaxy, and the number of pulsars in the galaxy
* The next $P$ lines will contain four numbers separated by space $x_i$, $y_i$, $r_i$, $t_i$, representing the description of the pulsar $P_i$
* The penultimate line will contain two numbers separated by a space representing the coordinates of the Vulcan planet sector $x_s$ and $y_s$
* The last line will contain two numbers separated by a space representing the coordinates of the Qo'noS planet sector $x_f$ and $y_f$

# Output data
In the file `pulsar.out` only one number will be printed depending on the task:
* If $C = 1$, then the number $S_{max}$ will be printed
* If $C = 2$, then the number $T_{min}$ will be printed

# Constraints and clarifications
* The Manhattan distance between two coordinates $(x_1, y_1)$ and $(x_2, y_2)$ is defined as: $|x_1 - x_2| + |y_1 - y_2|$
* The ship will not be able to leave the galaxy map at any time
* Pulsar waves can leave the galaxy map, but those sectors are not of interest for our problem
* It is guaranteed that at the moment of departure, the ship is not in danger
* It is guaranteed that there is a solution
* There may be multiple pulsars in the same sector
* $C \in \{1, 2\}$
* $3 \leq N \leq 500$
* $1 \leq P \leq 15\ 000$
* $0 \leq t_i \lt r_i \leq 6 \ \forall \ 1 \leq i \leq P$
* $1 \leq x_s, y_s, x_f, y_f \leq N$
* $1 \leq x_i, y_i \leq N \ \forall \ 1 \leq i \leq P$

## Subtask 1 (19 points)
* $C = 1$
  
## Subtask 2 (22 points)
* $C = 2$
* $r_i = 1 \ \forall \ 1 \leq i \leq P$
  
## Subtask 3 (9 points)
* $C = 2$
* $N \leq 7$
* $r_i \leq 3 \ \forall \ 1 \leq i \leq P$
  
## Subtask 4 (13 points)
* $C = 2$
* $t_i = 0 \ \forall \ 1 \leq i \leq P$
  
## Subtask 5 (37 points)
* $C = 2$

# Example 1
`pulsar.in`
```
1 5 4
3 1 2 1
1 5 3 1
5 3 2 0
3 4 2 1
1 1
5 5
```
`pulsar.out`
```
14
```

# Example 2
`pulsar.in`
```
2 5 4
3 1 2 1
1 5 3 1
5 3 2 0
3 4 2 1
1 1
5 5
```
`pulsar.out`
```
9
```

# Explanation
Below, the path taken by the USS Enterprise can be observed. The ship is illustrated in blue, the affected areas by the pulsars in red, and the Qo'noS planet in green:

~[exemplu2.png]

For the first example, it is observed that there will never be a moment in time when the pulsars will occupy more than $14$ sectors.

In the above figure, a possible path of duration $9$ is presented. This time is also minimal for the given example.