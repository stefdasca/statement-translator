## Task

In a forest, there is a community of squirrels living in trees. Two of these squirrels have thought of starting a small business. They want to open a chain of $K$ venues where squirrels from nearby trees can meet for a snack. The two "business squirrels" have $M$ potential locations in mind as possible places to set up their venues. Such a venue can serve all orders within its action range, a circular area with radius $R$, centered at the location of the venue. It is known that squirrels are very fond of acorns and nuts, so the residents of nearby trees will be considered certain clients. The forest has $N$ trees. For each tree, its location is known, as well as the number of squirrels that live in it. To start the business, exactly $K$ of the $M$ possible locations must be chosen such that the total number of certain squirrel clients is as large as possible. Write a program to determine the maximum number of certain clients.

## Input data

The first line of the file `veve.in` contains two integers $K$ and $R$, separated by a space, representing the number of venues the squirrels want to open and the radius of action of each venue.

The second line contains a natural number $M$, representing the number of possible locations for venues.

Each of the next $M$ lines contains two integers $X$ $Y$, separated by a space, representing the coordinates of a location (abscissa and ordinate).

The next line contains a natural number $N$, representing the number of trees with squirrels.

Each of the next $N$ lines contains information about a tree in the form of 3 integers separated by a space $X$ $Y$ $V$, meaning that at the coordinate point $X$ $Y$ there is a tree in which $V$ squirrels live.

## Output data

The output file `veve.out` will contain a single line that will print the maximum number of certain clients.

## Constraints and clarifications

$1 \leq K \leq 10$

$1 \leq R \leq 500$

$K \leq M \leq 20$

$-1000 \leq X, Y \leq 1000$

$1 \leq N, V \leq 100$

A tree is within the action radius of a venue if the distance from the tree to the venue is less than or equal to $R$

## Examples

`veve.in`
```
2 2
3
1 0
4 0
7 0
4
0 0 1
3 0 7
5 0 9
8 0 1
```
`veve.out`
```
18
```

`veve.in`
```
2 2
3
-2 0
0 1
3 0
8
-3 1 1
-3 0 1
-3 -1 1
-2 -1 1
0 0 3
0 2 1
2 1 3
4 0 2
```
`veve.out`
```
12
```