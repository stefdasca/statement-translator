# H

Gigel has $N$ vertical segments, numbered from $1$ to $N$. A segment $K$ is characterized by the values $X_K$, $Yjos_K$, and $Ysus_K$. The coordinates of the bottom end of segment $K$ are $(X_K, Yjos_K)$, and the coordinates of the top end are $(X_K, Ysus_K)$. Gigel wants to choose two of these segments and "cut" them in such a way that both have the same value for $Yjos$ and $Ysus$. 

Assuming that the chosen segments are $A$ and $B$, the new value of $Yjos$ for each of the two segments will be $max\{Yjos_A, Yjos_B\}$, and the new value of $Ysus$ for each of the two segments will be $min\{Ysus_A, Ysus_B\}$. Let's denote by $YJ$ the value $max\{Yjos_A, Yjos_B\}$ and by $YS$ the value $min\{Ysus_A, Ysus_B\}$. 

If the relationship $YJ \leq YS$ is not true, then the pair of segments $(A, B)$ is not valid (and Gigel would never choose an invalid pair). For a valid pair of segments $(A, B)$, after the "cutting" operation, he will connect the segments with a horizontal segment to form a figure that closely resembles the letter "H". The horizontal segment will be drawn between the coordinates $(X_A, Y)$ and $(X_B, Y)$, with $YJ \leq Y \leq YS$ (the exact value of the $Y$ coordinate of the drawn segment is not important). 

After obtaining the letter "H", Gigel calculates its "length". The length of the letter "H" is defined as the sum of the $3$ sides of the letter: $2(Y_S - Y_J) + |X_B - X_A|$. Help Gigel choose a valid pair of segments for which the length of the obtained letter $H$ is maximum.

## Input data

The first line of the input file `h.in` contains the integer $N$, representing the number of vertical segments. Each of the next $N$ lines contains $3$ integers separated by a space: $X$, $Yjos$, $Ysus$ (with the significance mentioned earlier). The $K$-th line of these $N$ lines contains the values characterizing the $K$-th segment.

## Output data

The output file `h.out` will contain an integer representing the maximum length of a letter $H$ that Gigel can draw according to the mentioned procedure.

## Constraints and clarifications

$1 \leq N \leq 65535$

For each segment:

$0 \leq X, Yjos, Ysus \leq 100\ 000\ 000$

$Yjos \leq Ysus$

There will be at least one valid pair of segments.

## Example

`h.in`
```
2
0 0 10
5 5 20
```

`h.out`
```
15
```