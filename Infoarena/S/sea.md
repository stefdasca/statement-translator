## Task

On the sea, there are $N$ ships. The shore is curiously perfectly straight and is represented by the $Ox$ axis of the coordinate system. The $N$ ships are represented by pairs of coordinates $(V_{xi}, V_{yi})$, where $V_{yi}$ is strictly positive (the sea is above the $Ox$ axis). On the shore, there are $M$ lighthouses, given by their coordinates $F_{xi}$ (being exactly at the border between sea and land, their $y$ is always $0$). The $M$ lighthouses are strange because they can only light to the left. Thus, the area lit by each lighthouse $i$ is defined by a quarter circle with a radius $F_{ri}$. More precisely, a ship is lit by a specific lighthouse if it is to the left of the lighthouse (its $x$ is smaller) and the distance from the lighthouse to the ship is less than or equal to the value $F_{ri}$ associated with that lighthouse. For each lighthouse, a strictly positive natural number $F_{ni}$ is also given. For reasons hard to understand, the port manager wants each lighthouse $i$ to light at least $F_{ni}$ ships (a ship can be lit by multiple lighthouses). He wants minimal energy consumption and wants to find for each lighthouse the minimum radius needed to light the required number of ships. Determine for each lighthouse the value $F_{ri}$, which represents the minimum necessary radius for the lighthouse to light at least $F_{ni}$ ships.

## Input data

The first line of the `sea.in` file contains two integers $N$ and $M$ separated by a space, representing the number of ships and the number of lighthouses, respectively. Each of the following $N$ lines contains a pair of real numbers separated by a space $V_{xi}$ and $V_{yi}$ (the coordinates of the ships). Each of the following $M$ lines contains a pair of numbers separated by a space, one real $F_{xi}$ and one integer $F_{ni}$ (the horizontal coordinates and the numbers associated with the lighthouses).

## Output data

The `sea.out` file will contain $M$ lines, each line containing a real number given to 4 decimal places: line $i$ will contain the minimum radius necessary for lighthouse $i$ to light $F_{ni}$ ships.

## Constraints and clarifications

$1 \leq N \leq 400$

$1 \leq M \leq 100\ 000$

$0 < y, r < 100\ 000$

$-100\ 000 < x < 100\ 000$

$1 \leq F_{ni} \leq N$

In the input file, lighthouses are sorted in increasing order by their $x$ coordinates.

There will be no two ships, or a lighthouse and a ship with the same $x$. 

However, there might be two or more lighthouses with the same $x$, in which case they will be next to each other in the input file (obviously since they are sorted by $x$). The order in which lighthouses with the same $x$ appear in the input file is not defined. There might even be two identical lighthouses.

The real numbers in the input file will have at most 4 decimal places.

Numbers must be displayed in the output with EXACTLY 4 decimal places.

The result will be checked with a precision of $0.001$ (the result will be considered correct if the absolute difference between the correct result and the one provided by the contestant does not exceed $0.001$).

There is always a solution (for each lighthouse $i$ there will always be at least $F_{ni}$ ships to its left).

## Example

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