Bazar

While walking through the bazaar in Istanbul, Marcel came across the following problem at the cow trading department.

## Task

You are given a grassy field, a $xOy$ coordinate system, and two bulls, Ollu and Bollu, who are connected by an extendable and sharp wire. They are initially located at the point $(0, 0)$. Both can move at the same speed only in the North and East directions. As they walk, the wire connecting them cuts the grass they encounter. They move in such a way as to cut as much grass as possible using the wire. There are also $N$ points where you can place a tulip. The bulls will set their path in such a way as to visit all the tulips you have planted. To avoid confusion, you need to choose the points where you place the tulips so that they are all visitable in a single traversal of the field, considering the restriction of the bulls' movement only to the North and East. I forgot to mention: Ollu and Bollu are the smartest bulls, they quickly realize when you are trying to fool them. For this reason, you cannot place fewer tulips than the maximum number of tulips you could plant in the most favorable selection of points - otherwise, you would greatly irritate Ollu and Bollu. For all the correct ways in which you could choose the set of points where to place tulips, Bisisica (a kind of Miorita, only more stubborn) calculates the amount of grass that the bulls will cut with their wire if they aim to visit the chosen tulips. In the end, she adds up all these numbers and calls their sum by her name. What is the remainder when dividing her number by $10^9 + 7$?

## Input data

The input file `bazar.in` contains on the first line the number $N$ of points. On the next $N$ lines, there are two natural numbers greater than zero and less than or equal to $10^9$, describing the coordinates of the points where a tulip can be placed.

## Output data

In the output file `bazar.out`, print the remainder of Bisisica's number when divided by $10^9 + 7$.

## Constraints

$1 \leq N \leq 200,000$ 

For $4$% of the score, $N \leq 7$ 

For $9$% of the score, $N \leq 16$ 

For $23$% of the score, $N \leq 1,000$ 

For $44$% of the score, the points in the input are relatively uniformly distributed in the plane

The points given in the input are distinct pairwise

Formally, a correct way to choose the set of points to place tulips corresponds to a maximum cardinality subset of the set of $N$ given points, such that there is an ordering of the chosen points in such a way that the coordinates $X$, and respectively $Y$, are simultaneously in non-decreasing order. Note: a maximum cardinality subset means something different from a maximal subset!

## Example

`bazar.in` 
```
9
5 3
9 6
7 7
2 2
6 4
3 1
10 8
6 3
8 5
```

`bazar.out`
```
24
```

## Explanation

The maximum number of tulips that can be planted to be visitable in a single traversal is $7$. There are two ways to choose $7$ points with the required property. The first possible route: $(0, 0) - (3, 1) - (5, 3) - (6, 3) - (6, 4) - (8, 5) - (9, 6) - (10, 8)$ The second possible route: $(0, 0) - (2, 2) - (5, 3) - (6, 3) - (6, 4) - (8, 5) - (9, 6) - (10, 8)$ Because the bulls will move to cut as much grass as possible, a possible tour for the first route is as follows: Initially, Ollu and Bollu are located at the point $(0, 0)$. Ollu moves northward, and Bollu moves eastward. When Ollu reaches the point $(0, 1)$, Bollu is at point $(1, 0)$, as they have the same speed. If Ollu continues to move northward, he won't be able to reach the tulip at point $(3, 1)$, as he can only move north or east. So he changes direction, moving eastward until he reaches the tulip. Bollu, however, when he reaches the point $(3, 0)$, must head north, otherwise, he would not reach the first tulip. The two meet at point $(3, 1)$, enjoy the tulip, and continue their journey in a similar manner to the tulip at point $(5, 3)$. Practically, the area of grass cut up to the first tulip is that of the rectangle with corners at $(0, 0)$ and $(3, 1)$. Similarly, the bulls will cut the grass in the rectangles $(3, 1) - (5, 3)$, $(5, 3) - (6, 3)$, $(6, 3) - (6, 4)$, $(6, 4) - (8, 5)$, $(8, 5) - (9, 6)$, $(9, 6) - (10, 8)$, resulting in a total area of $12$. In the second route, the areas of the visited rectangles are, in order, $4 + 3 + 0 + 0 + 2 + 1 + 2 = 12$. Bisisica sums the areas obtained for all the correct paths, so $Bisisica = 12 + 12 = 24$. In the `bazar.out` file, you must print the remainder when this number is divided by $10^9 + 7$. According to the remainder theorem, $24 = 1000000007 \cdot 0 + 24$, so the remainder is $24$.