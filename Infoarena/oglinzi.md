## Task

Consider a 2D coordinate system. At the origin, there is a laser emitting a light beam at $45$ degrees (see example). The $Ox$ axis is a mirror, so the light beam will be reflected if it hits the $Ox$ axis. Additionally, there are $N$ horizontal mirrors. Mirror $i$ is characterized by $3$ parameters: $l_i$, $r_i$, and $h_i$, being geometrically a segment between $ (l_i, h_i)$ and $ (r_i, h_i)$. If the light beam hits a mirror, it will be reflected. The mirrors work on both sides. Moreover, the intervals $[l_i, r_i]$ are disjoint and are given in increasing order $ (l_1 < r_1 < l_2 < r_2 < \dots < l_n < r_n)$. After all the mirrors, at $x = L > r_n$, there is a screen of height $H$. Geometrically, this is a segment between $(L, 0)$ and $(L, H)$. You want the light beam to reach the screen. To achieve this, you can perform multiple operations. An operation consists of moving a mirror vertically by one position (from $h_i$ to $h_i -1$ or $h_i +1$). The task is to find the minimum number of operations needed for the light beam to reach the screen. If this cannot be achieved, you should output Imposibil.

## Input data

The input file `oglinzi.in` will contain on the first line the number of tests $T$. This is followed by the descriptions of the $T$ tests. On the first line of each test, there will be the integers $N$, $L$, and $H$. This will be followed by $N$ lines, with line $i$ containing the $3$ integers that describe mirror $i$: $l_i$, $r_i$, and $h_i$.

## Output data

In the output file `oglinzi.out` print $T$ lines with the answers for the $T$ tests.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N \leq 200$

$1 \leq h_i, H \leq 400$

$0 \leq l_1 < r_1 < l_2 < r_2 < \dots < l_n < r_n < L \leq 400$

A screen at height $1$ cannot be moved downwards.

If the light beam hits a mirror at one of its corners, it will be reflected (see example).

Also, if the light beam hits the screen at its top end, it is considered that it has reached the screen.

## Example

`oglinzi.in`
```
2
3 15 1
4 6 5
7 8 4
10 11 5
1 10 1
1 2 1
2
```

`oglinzi.out`
```
2
Imposibil
```

## Explanation

For the first test, the optimal solution is moving mirror $2$ one position down and mirror $3$ one position up, according to the image. Thus, the optimal cost is $2$. For the second test, the light beam will never reach the screen, regardless of how we move the only existing mirror.