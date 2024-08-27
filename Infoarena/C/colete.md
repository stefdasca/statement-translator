## Task

In the pasture of wonders, there are $N$ children, with child $i$ having a house at the coordinate point (in meters). Each child has a parcel, with mysterious content, which they want to transport to the main road, which is the $OX$ axis, where the post office truck will come and pick it up. To make these transports, each child has a drone with the following characteristics:
$v \rightarrow$ the speed at which it flies ($v$ is expressed in the number of seconds required to cover a meter)
$h \rightarrow$ the height at which it must fly so as not to break, it can only move along the axes. Due to strong wind, it can only move downwards, i.e., to a lower $y$ coordinate. Thus, it can only move in the directions SOUTH, EAST, and WEST
$d \rightarrow$ because the drone is remote-controlled, it cannot move to a distance on the $OX$ axis from the house greater than $d$
Each child wants to find out the minimum time required to transport their parcel to the main road. Because the children are good friends with each other, to transport their parcel, a child has two options:
either they transport the parcel with their drone to the main road, or they transport it with their drone to another child, who will personally handle the parcel and transport it to the main road using the same method described so far (either they will transport it with their drone to the main road, or take it with their drone to another child who will do the same thing). The time required to transfer the parcel from one drone to another is negligible, but note that the drone must be raised to a certain level and then lowered to level $0$ when it reaches another child's house so that the transfer from one drone to another can be made (as mentioned, with negligible time).

## Input data

The input file `colete.in` contains on the first line the number $N$. The following $N$ lines each contain $5$ numbers $x, y, v, h, d$ with the meanings from the statement.

## Output data

The output file `colete.out` must contain $N$ lines, the $i$-th line representing the minimum time for child $i$ to transport their parcel to the main road.

## Constraints and clarifications

$1 \leq N \leq 50000$ 

$1 \leq x, y, v, h, d \leq 10$ 

$8$

The $y$ coordinates are distinct, two by two.

## Example

`colete.in colete.out` 
```
4
3 5 5 2 1
1 4 1 1 2
4 2 1 1 2
5 3 6 1 3
```

`44
6
4
28`