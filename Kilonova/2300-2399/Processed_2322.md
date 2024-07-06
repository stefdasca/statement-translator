Certainly! Here is the translated statement:

## Task

Given $N$ points on the OX axis, numbered from $1$ to $N$. Each point $i$ is at coordinate $x_i$ and has a weight $w_i$. We want to place on the OX axis a closed interval of length $L$, so that the maximum of the weighted distances from the points to the interval is minimized (this value is called the *mini-max distance*). The distance from a point $i$ to an interval $[a, a+L]$ is defined as follows:

* $0$, if $a \leq x_i \leq a+L$
* $w_i \cdot (a - x_i)$, if $x_i < a$
* $w_i \cdot (x_i - (a+L))$, if $x_i > a + L$

The coordinates and weights of each point are generated according to the following algorithm (where $x_1 = 0$ and $w_1, A, B, C_1$, and $D$ are given in the input file):

```pascal
C = C1
for i = 2 to N do
    x[i] = x[i-1] + 1 + (((x[i-1] \cdot i) xor A) modulo B)
   if (2 \cdot i <= N) then
      k = 1
   else
      k = -1
   w[i] = maxim(1, w[i-1] + k \cdot (1 + (((w[i-1] \cdot (i + C)) xor (D \cdot i)) modulo D)))
   C = 1 + ((((C \cdot C) modulo D) \cdot i) modulo D)
```

## Task

Determine the mini-max distance, as well as the left end of the interval for which this distance is obtained.

## Input data

The first line of the input file `center.in` contains the integers $N$ and $L$. The second line contains the integer $w_1$. The third line contains the integers $A, B, C_1$, and $D$. The numbers on the same line are separated by a space.

## Output data

The first line of the output file `center.out` will contain the mini-max distance for the generated set of points, and the second line will contain the left end of the interval of length $L$ for which this distance is obtained. Print the left end with as many decimals as possible (at least $8$).

## Constraints and clarifications

* $1 \leq N \leq 1\ 000\ 000$;
* $0 \leq L \leq 100\ 000\ 000$
* $1 \leq w_1, A, B, C_1, D \leq 100$
* No specific property of the generation algorithm needs to be found to help you solve the problem (however, if you find such a property, you can use it).
* You receive the points corresponding to a test if for both requirements the absolute difference between the correct result and the printed one is at most $0.01$.

## Example

`center.in`
```
4 2
2
1 2 3 4
```

`center.out`
```
2.667
1.33333333
```

## Explanation

The coordinates of the $4$ points are: $0, 2, 4, 6$. The weights of the $4$ points are: $2, 5, 2, 1$. The mini-max distance is $2.667$ and it is obtained for the interval $[1.333, 3.333]$ (having length $L=2$). The distances from the $4$ points to the interval are: $2.667, 0, 1.333, 2.667$.