## Task

A plot of land is divided into $N \times M$ parcels. On this plot, a number $P$ of trees have been planted in parcels with known coordinates, each in a certain calendar year. For each tree, the values $A_i, X_i, Y_i$ are known, with $1 \leq i \leq P$, where $A_i$ is the year tree $i$ was planted, and $X_i$ and $Y_i$ are the coordinates of the parcel where it was planted. It is known that each tree increases its height by $K$ times each year. Thus, in the year it was planted, the tree has a height of $1$, in the second year $k$, in the third $k^2$ etc.

We define a region as a rectangular land area with sides parallel to those of the land, specified by the top-left and bottom-right parcels: $( X_s , Y_s ), ( X_d , Y_d )$. A region is considered "beautiful" if for each height $H$, there is an even number of trees with that height. In the year $2015$ the owner discovered an ingenious method to add new trees of any height. Using this method, he is interested in sequentially "beautifying" $Q$ regions of the surface during that year. Trees can be added only to the bottom-right parcel of the regions of interest, and a minimum number of trees will be planted. Once the region becomes beautiful, the planted trees remain in the respective parcel.

## Input data

The first line of the input file `parcele2.in` will contain $T$, representing the number of tests. Within a test, the first line will contain the numbers $N , M$ and $K$, representing the dimensions of the land and the growth factor of the trees in a year. On the next line follows the number $P$, representing the number of trees initially planted on the parcel. On each of the next $P$ lines, there are three integers: $A_i, X_i, Y_i$. On the next line is the number $Q$, representing the number of queries. On each of the $Q$ lines, there are four integers, representing the top-left and bottom-right corners of a region that the owner wishes to "beautify".

## Output data

The output file `parcele2.out` contains for each test $Q_i$ lines, $1 \leq i \leq T$. On each line, print a number $C$, representing the number of trees that the owner needs to plant, followed by a sequence of heights $H$, meaning that he plants one tree of each specified height. As these can be very large numbers, print them modulo $666013$. The heights can be printed in any order.

## Constraints
$$
1 \leq T \leq 10
$$
$$
1955 \leq A_i \leq 2015
$$
$$
1 \leq N, M \leq 1000
$$
$$
1 \leq X_i \leq N \text{ and } 1 \leq Y_i \leq M
$$
$$
1 \leq K \leq 100
$$
$$
1 \leq P  \\
1 \leq Q \\
P + Q \leq 2000
$$

## Example

`parcele2.in` 
```
1
3 4 3
4
2013 1 2
2013 1 2
2011 2 2
2014 1 3
3
1 1 2 3
2 2 3 4
1 2 2 4
```

`parcele2.out`
```
2 81 3
1 3
0
```

## Explanation

At the beginning, there are four trees planted on the land as shown in the adjacent figure: The owner wants to know which trees need to be planted in the region $((1,1), (2,3))$ to make this region beautiful. He plants one tree of height $81$ and one of height $3$ on the parcel $(2,3)$. Next, he wants to "beautify" the region $((2,2), (3,4))$ and will plant one tree on parcel $(3,4)$, of height $3$. Finally, to "beautify" the region $((1,2), (2,4))$, he does not need to plant any trees.