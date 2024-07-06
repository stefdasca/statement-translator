Here's the translated competitive programming problem statement in English:

---

An alpinist wants to climb the highest possible peak in the Carpathian Mountains. Unfortunately, he is scared to climb from one rock to the adjacent one if the altitude difference exceeds $100$ meters. However, he descends without fear from one rock to the adjacent one, regardless of the altitude difference.

The alpinist has the map of the mountain he wants to climb. The map is encoded as a grid where the cells indicate the altitudes of the points (the heights of the rocks) on the map, given in meters relative to sea level. The climber can start from any cell on the map with altitude $0$ (at sea level) and can take a step only to a terrain portion corresponding to an adjacent cell on the map, vertically or horizontally, with the condition that he is not scared.

# Task

The alpinist seeks your help to find the shortest route he should take to climb to the highest possible peak.

# Input data

The first line of the input file `alpinist.in` contains two integers, $M$ and $N$, representing the dimensions of the grid corresponding to the map. On the next $M$ lines, there are $N$ natural numbers, separated by a space, representing the values associated with the grid encoding the map (line by line).

# Output data

The first line of the output file `alpinist.out` contains $I$, a natural number representing the maximum height the alpinist can reach; The second line contains $X_P$, $Y_P$, $X_D$, $Y_D$, four non-zero natural numbers, separated by a space, representing the coordinates of the cell from which the alpinist starts and the coordinates of the cell with the maximum height he can reach; By the coordinates of the cell, we understand the line and column number where the cell is located in the grid; The next line contains $L$, a natural number representing the length of the route; the length of a route is defined as being equal to the number of cells traversed by the alpinist; The next line contains $L$ characters, separated by a space, representing the direction in which the alpinist moves at each step $i$; the characters can be: `N` – corresponding to a movement up, `S` – corresponding to a movement down, `W` – corresponding to a movement to the left, `E` – corresponding to a movement to the right.

# Constraints and clarifications

* $2 \leq M,N \leq 100$
* $0 \leq v_i \leq 1 \ 000$
* if there are multiple routes of the minimum length, only one will be written in the file.

# Example

`alpinist.in`
```
3 5
0 101 2 14 100
50 149 149 250 200
0 100 10 400 10
```

`alpinist.out`
```
250
1 1 2 4
8
S E E N E E S W
```

---