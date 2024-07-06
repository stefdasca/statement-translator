~[medalion1.png|align=right]
Rapunzel, the beautiful princess with long, blonde, and magical hair, is preparing for her wedding with the legendary Flynn Rider. For this event, he will gift the princess a unique medallion that she will wear on her wedding day.
~[medalion2.png|align=right]
The order for the creation of the medallion is taken by a renowned jeweler of the kingdom who receives from Flynn $k$ boxes (numbered from $1$ to $k$), each box containing many crystals, identical in value. Thus, all the crystals in the first box have the value $1$, all the crystals in the second box have the value $2$, and so on, so that all the crystals in the last box have the value $k$. The jeweler will mount the crystals on a square-shaped gold plate with $n$ rows of crystals, with each row having $n$ crystals placed side by side. He takes one crystal from each box in order, in the order: $1$, $2$, $3$, $\dots$, $k$, $1$, $2$, $3$, $\dots$, $k$, $1$, $2$, $3$, $\dots$ and places them on the gold plate in the form of a **spiral**. The spiral starts from the center of the medallion where the first crystal is mounted. The second crystal is mounted to the right of the first, and the next crystal, below, on the next row. The mounting of crystals continues on the same row, moving to the left, then up until the row above the row where the first crystal is mounted. This continues in the same manner, respecting the rule of constructing the spiral: right, down, left, up, and so on.
~[medalion3.png|align=right]
For example, for $k = 5$, crystals are mounted on the medallion as shown in the adjacent drawing.

# Task

1. Knowing that the jeweler completes $n$ ($n$ odd natural number) rows with crystals on the gold plate, determine the maximum sum of the values of all crystals located on a row of the medallion.
2. Determine the value of the crystal mounted exactly $p$ rows above the first crystal mounted on the medallion and placed on the same column as this one.

# Input data

The input file `medalion.in` contains on the first line the natural numbers $k$, $n$, $p$ (in this order), with the meanings mentioned above. The values $k$, $n$, $p$ are separated by a space.

# Output data

The output file `medalion.out` contains on the first line a natural number, representing the number determined according to task $a$, and on the second line a natural number, determined according to task $b$.

# Constraints and clarifications

* $2 \leq k \leq 20$
* $3 \leq n \leq 301$
* $1 \leq p \leq 500\ 000$
* the number of crystals in each box is large enough for constructing the medallion;
* for a correct resolution of task $1$, $40\%$ of the score of each test is awarded, and for a correct resolution of task $2$, $60\%$ of the score of each test is awarded.

# Example

`medalion.in`
```
5 3 4
```

`medalion.out`
```
12
2
```

## Explanation

~[medalion4.png|align=right]
$1.$ After mounting $3$ rows of crystals, the configuration obtained is: The sums of the values of the crystals on these rows are:
$2 + 3 + 4 = 9$
$1 + 1 + 2 = 4$
$5 + 4 + 3 = 12$
The largest sum is $12$.
$2.$ The crystal located $4$ rows above the center of the medallion, marked in the adjacent drawing, has the value $2$.