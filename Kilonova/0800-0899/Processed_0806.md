~[cri.png|align=right|width=23em]

The ant has built a grain depot on a rectangular area and partitioned it into $N \cdot M$ identical square-shaped rooms, arranged $M$ along the $Ox$ direction and $N$ along the $Oy$ direction. From each room, it is possible to enter any adjacent room (a room that has a common wall with it).

In each room, identified by its coordinates, as in the drawing below where $N = 5$ and $M = 4$, the ant has stored a quantity of grains. For example, in the room with coordinates $(i, j)$, the quantity $C_{IJ}$ of grains is stored.

Both the entrance and the exit from the depot can only be made through the four rooms in the corners of the depot, namely those with coordinates $(1, 1), (1, M), (N, 1)$, and $(N, M)$ which communicate with the outside.

To ensure air circulation in the depot, the ant installed a ventilation system in the room with coordinates $(X, Y)$.

Seeing how many grains the ant has for winter, its neighbor, the lazy grasshopper Cri, decided to steal some of them.

Cri thought to enter the depot through the ventilation system in the room with coordinates $(X, Y)$ and exit through one of the four rooms in the corners of the depot which communicate with the outside.

He studied the depot plan and divided the rooms into four zones:

* The first zone, numbered $1$, contains all the rooms with coordinates $(i, j)$ where $1 \leq i \leq X$ and $1 \leq j \leq Y$, with the exit through the room with coordinates $(1, 1)$.
* The second zone, numbered $2$, contains all the rooms with coordinates $(i, j)$ where $1 \leq i \leq X$ and $Y \leq j \leq M$, with the exit through the room with coordinates $(1, M)$.
* The third zone, numbered $3$, contains all the rooms with coordinates $(i, j)$ where $X \leq i \leq N$ and $1 \leq j \leq Y$, with the exit through the room with coordinates $(N, 1)$.
* The fourth zone, numbered $4$, contains all the rooms with coordinates $(i, j)$ where $X \leq i \leq N$ and $Y \leq j \leq M$, with the exit through the room with coordinates $(N, M)$.

Cri will enter only one of the four zones and will steal the grains only from the rooms contained in the chosen zone. To avoid triggering the ant's alarm, he will need to pass through each room in the zone at most once, steal the entire quantity of grains from it, and exit the depot through the room communicating with the outside corresponding to the chosen zone.

Cri will need to choose the zone he will enter so that the total quantity $T$ of stolen grains is maximum, and the number $K$ of rooms he will pass through is minimal.

# Task

Write a program that determines the natural numbers $Z, T$, and $K$, where $Z$ represents the number of the zone Cri should choose to maximize the total quantity $T$ of stolen grains, and the number $K$ of rooms he will pass through is minimal.

# Input data

The input file `cri.in` contains on the first line the four nonzero natural numbers $N \ M \ X \ Y$, separated by a space, as described in the statement. On each of the next $N$ lines, there are $M$ nonzero natural numbers, separated by a space, representing the quantity of grains $C_{IJ}$ stored in the room with coordinates $(i, j)$ for $1 \leq i \leq N$ and $1 \leq j \leq M$.

# Output data

The output file `cri.out` will contain, on a single line, the three natural numbers $Z \ T \ K$ determined by the program, separated by a space, in this order.

# Constraints and clarifications

* $3 \leq N \leq 500$;
* $3 \leq M \leq 500$;
* $2 \leq X \leq N$;
* $2 \leq Y \leq M$;
* $1 \leq C_{IJ} \leq 8000$;
* If there are zones for which the same maximum total quantity $T$ of grains is obtained and the same minimal number $K$ of rooms is passed through, the zone numbered with the smallest number will be chosen.
* 20% of the score will be awarded for the correct determination of the number $Z$, 40% of the score for the correct determination of the number $T$, and 40% of the score for the correct determination of the number $K$.

# Example

`cri.in`
```
5 4 2 3
1 2 3 33
5 4 3 9
2 13 4 15
1 2 3 3
1 5 2 6
```

`cri.out`
```
2 45 3
```

## Explanation

The starting room has coordinates $(2, 3)$, and $N = 5$ and $M = 4$.  
Zone $1$ contains the rooms with coordinates: $(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)$. The maximum quantity of grains Cri can steal is $18$ passing through $6$ rooms.  
Zone $2$ contains the rooms with coordinates: $(1, 3), (1, 4), (2, 3), (2, 4)$. The maximum quantity of grains Cri can steal is 45 passing through 3 rooms.  
Zone $3$ contains the rooms with coordinates: $(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3), (5, 1), (5, 2), (5, 3)$. The maximum quantity of grains Cri can steal is $45$ passing through $12$ rooms.  
Zone $4$ contains the rooms with coordinates: $(2, 3), (2, 4), (3, 3), (3, 4), (4, 3), (4, 4), (5, 3), (5, 4)$. The maximum quantity of grains Cri can steal is $43$ passing through $7$ rooms.  
Thus, Cri will enter zone $Z = 2$, steal the maximum quantity of grains $T = 45$ passing through the minimum number $K = 3$ of rooms.