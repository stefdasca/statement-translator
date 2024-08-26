## Task

Cezara is located at the center of the Cartesian coordinate system (at the point $0, 0$) and has a pistol with special bullets. Using this pistol, she aims to destroy all $N$ segments parallel to the $Oy$ axis located to her left and right. She can orient the pistol at any angle between $0$ and $360$ and can fire a bullet in that direction. The bullet will pass through all segments it can touch and destroy them instantly. Since the bullets are expensive, she plans to use as few bullets as possible.

## Input data

The input file `rays.in` contains on the first line the number $N$ with the meaning given above. On the next $N$ lines follow three numbers $x$ $y_1$ $y_2$, $(x, y_1)$ and $(x, y_2)$ representing the endpoints of the segment parallel to the $Oy$ axis.

## Output data

The first line of the output file `rays.out` contains a single number $MIN$ representing the minimum number of shots required to destroy all the segments.

## Constraints

$1 \leq N \leq 200\ 000$

All coordinates are integers, and their absolute value is less than or equal to $10^9$

There will be no segment located on the $Oy$ axis

## Example

`rays.in`
```
6
-3 0 2
-4 2 4
3 1 -2
3 2 6
4 -1 -5
5 -8 3
```

`rays.out`
```
3
```

## Explanation

In the figure, the segments are represented in blue and the red arrows represent the direction in which the bullets were fired.