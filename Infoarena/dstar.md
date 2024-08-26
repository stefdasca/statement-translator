# Drawing Stars

In this problem, we will draw a star. We start with a supporting circle. Let's assume we draw a vertical ray from the center upwards, then one downwards, then horizontal rays at 90 degrees to the first ones, then oblique rays at 45 degrees$\dots$ and so on. At each step, we draw a ray that partitions the arc of the maximum angle into two arcs of equal angles. Through this simple process, we can draw stars that become "increasingly symmetrical." Thus, we can extend the process for any initial set of rays.

## Input data

The first line of the `dstar.in` file contains the number $R$ of rays, followed by the number $P$ of partitions required until the star looks acceptably symmetrical. The next line contains the angles $u$ between each ray and the previous ray. For simplicity, the first angle is angle $0$ and corresponds to the imaginary ray upwards. Each value occupies at most 10 characters. The values on a row are separated by a single space.

## Output data

The `dstar.out` file contains a single line with the largest angle of an arc, after the process has been applied $P$ times on the (incomplete) star with the $R$ rays given by the angles $u$.

## Constraints and clarifications

$1 \leq R$ , $P \leq 100\ 000$. 
$0.0 \leq \text{sum of the angles} < 360.0$. 
The solutions may have an error of $\pm 0.000001$.

## Examples

`dstar.in` `dstar.out` 
```
1 1
0
180.000000
```
```
2 2
0.00 90.000
135.000000
```

## Explanations

In the first example, the star initially contains only one ray (the first $1$) upwards (angle of $0$ degrees). Then we make a single partition (the second $1$) with a ray at an angle of $180$ degrees. Two arcs are formed, each of $180$ degrees. In the second example, the star initially contains two rays (the first $2$), located at $0$ and $90$ degrees to the (imaginary) upwards ray. We make two partitions (the second $2$). The first partition is made in the arc of $270$ degrees, and the second in one of the arcs of $135$ degrees. The arc of the maximum angle will have $135$ degrees.