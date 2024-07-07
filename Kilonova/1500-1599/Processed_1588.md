
The last cold season was one with a lot of snow in the mountainous area, therefore the sports goods store in the Semenic ski resort had large sales, especially of ski boots (special boots for skiing). Now, being the end of the season, the store employees note that they have $N$ empty boxes left in which the sold pairs of ski boots were packed. These boxes are in the shape of a rectangular parallelepiped where the top face is the lid. The lid and (of course) the face opposite the lid are square in shape, and the height is arbitrary, depending on the ski boots model. In some boxes, the lid is present; in others, the lid is missing.

These boxes need to be handed over to a recycling company, but until the recycling truck arrives in Semenic, the boxes need to be stored. Therefore, one of the store employees is tasked with stacking the boxes on top of each other in the form of a tower. The employee takes the boxes in the order they are found in the store and places them one on top of the other. To ensure some stability of the tower, he arranges them so that the axes that join the center of the lid with the center of the opposite face of each box are collinear. The boxes fall one by one from a sufficiently high height, with the lateral faces perpendicular to the floor and parallel to those of the boxes already placed, until they meet one of these boxes or the floor. Regarding the placement of the boxes that have the lid missing, the employee places them either with the gap formed by the missing lid upwards or downwards.

# Task

Given $N$ (the number of boxes in the store), the order in which the boxes are stacked in the tower, and for each box, the side of the lid, the height of the box, and whether it has a lid or, if the lid is missing, if the box is placed with the gap upwards or downwards, determine:

* the height of the resulting tower;
* the number of boxes whose lateral faces are visible if the tower is viewed from the side.

# Input data

The first line of the input file `schi.in` contains the number $C$, which can be $1$ or $2$ and represents the task that must be solved.

The second line contains the natural number $N$, representing the number of boxes that are stacked in the tower.

Each of the following $N$ lines contains three values $L$, $H$, and $M$, separated by a space. The values on line $i + 2 (1 \leq i \leq N)$ represent information regarding the $i$-th box added to the tower, namely:

* $L$ – the side of the box's lid;
* $H$ – the height of the box;
* $M$ – a value equal to $0$, $1$, or $2$, with the following meaning:
    * $M = 0$ – the box has the lid missing and is placed with the gap downwards;
    * $M = 1$ – the box has a lid;
    * $M = 2$ – the box has the lid missing and is placed with the gap upwards.

# Output data

If $C$ is $1$, the output file `schi.out` will contain on the first line the answer for task $1$ (the height of the formed tower). If $C$ is $2$, the output file `schi.out` will contain on the first line the answer for task $2$ (the number of boxes whose lateral faces are visible if the tower is viewed from the side).

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$.
* The dimensions of the boxes are natural numbers in the range $[1, 1\ 000\ 000\ 000]$.
* The sides of the box lids are distinct two by two.
* The thickness of the walls that form the faces of the boxes (including the lid) is negligible.
* The construction of the tower takes place on a flat floor of infinite dimensions.

| # | Score | Constraints          |
| - | ------- | ------------------- |
| 1 | 12      | $C = 1$ and $N \leq 2\ 000$ |
| 2 | 12      | $C = 2$ and $N \leq 2\ 000$      |
| 3 | 8      | $C = 1$ and there are no boxes placed with the gap upwards      |
| 4 | 8      | $C = 2$ and there are no boxes placed with the gap upwards      |
| 5 | 8      | $C = 1$ and there are no boxes placed with the gap downwards      |
| 6 | 8      | $C = 2$ and there are no boxes placed with the gap downwards      |
| 7 | 22      | $C = 1$      |
| 8 | 22      | $C = 2$      |

# Example 1

`schi.in`
```
1
5
20 3 2
3 7 1
9 1 1
11 5 1
12 6 0
```

`schi.out`
```
13
```

## Explanation

The height of the box tower is $13$.

# Example 2

`schi.in`
```
2
5
20 3 2
3 7 1
9 1 1
11 5 1
12 6 0
```

`schi.out`
```
3
```

## Explanation

When viewed from the side, $3$ boxes are visible, namely those with lids of sides $20$, $3$, and $12$.

~[schi.jpg|align=left]
