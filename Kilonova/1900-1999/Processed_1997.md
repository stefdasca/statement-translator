
# Task

There are $N$ ships on the sea. The shore is curiously perfectly straight and is represented by the Ox axis of the coordinate system. The $N$ ships are represented by pairs of coordinates $(V_{x_i}, V_{y_i})$, where $V_{y_i}$ is strictly positive (the sea is above the Ox axis). On the shore, there are $M$ lighthouses, given by their coordinates $F_{x_i}$ (being exactly at the boundary between the sea and the land, their $y$ is always $0$). The $M$ lighthouses are strange because they can only illuminate to the left. Thus, the illuminated area of each lighthouse $i$ is bounded by a quarter circle with a radius $F_{r_i}$. More precisely, a ship is illuminated by a certain lighthouse if it is to the left of the lighthouse (its $x$ is smaller) and the distance from the lighthouse to the ship is **less than or equal to** the value $F_{r_i}$ associated with the respective lighthouse.
For each lighthouse, a strictly positive natural number $F_{n_i}$ is also given. For reasons hard to understand, the harbor master wants each lighthouse $i$ to illuminate at least $F_{n_i}$ ships (a ship can be illuminated by multiple lighthouses). He wants to minimize energy consumption and wants to find out the minimum radius required for each lighthouse to illuminate the required number of ships.

Determine for each lighthouse the value of $F_{r_i}$ which represents the minimum radius necessary for the lighthouse to illuminate at least $F_{n_i}$ ships.

# Input Data

The first line of the file `sea.in` contains two integers $N$ and $M$ separated by a space, representing the number of ships and the number of lighthouses, respectively. Each of the following $N$ lines contains a pair of real numbers separated by a space $V_{x_i}$ and $V_{y_i}$ (ship coordinates). Each of the following $M$ lines contains a pair of numbers separated by a space, one real $F_{x_i}$ and one integer $F_{n_i}$ (horizontal coordinates and numbers associated with the lighthouses).

# Output Data

The file `sea.out` will contain $M$ lines, each line containing a real number, given with $4$ decimal places: line $i$ contains the minimum radius necessary for lighthouse $i$ to illuminate $F_{n_i}$ ships.

# Constraints and clarifications

* $1 \leq N \leq 400$
* $1 \leq M \leq 100\ 000$
* $0 < y, r < 100\ 000$
* $-100\ 000 < x < 100\ 000$
* $1 \leq F_{n_i} \leq N$
* In the input file, lighthouses are sorted in ascending order by their $x$ coordinates.
* There will not be two ships, or a lighthouse and a ship with the same $x$. However, there can be two or more lighthouses with the same $x$, in which case they will be next to each other in the input file (obviously since they are sorted by $x$). The order in which lighthouses with the same $x$ appear in the input file is not defined. There may even be two identical lighthouses.
* The real numbers in the input file will have a maximum of $4$ decimal places.
* The result will be checked with a precision of $0.001$ (the result will be considered correct if the absolute value of the difference between the correct result and the one provided by the contestant does not exceed $0.001$).
* There is always a solution (for each lighthouse $i$ there will always be at least $F_{n_i}$ ships to its left).

# Example

`sea.in`
```
3 5
-0.5 0.5
-2 5
3 4
-1 1
0 1
0 2
0 1
5 1
```

`sea.out`
```
5.0990
0.7071
5.3852
0.7071
4.4721
```
