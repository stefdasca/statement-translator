# Colors

Mara received a new set of watercolors as a gift. To her surprise, she noticed that when combining the colors $G$ and $V$, an unusual result is obtained. She tried all possible combinations and observed that: if she pours $V$ over $V$, she gets $G$; if she pours $G$ over $G$, she gets $V$; if she pours $G$ over $V$, she gets $V$; if she pours $V$ over $G$, she gets $G$. Curious, Mara conducted the following experiment: she placed just $V$ and $G$ colors randomly in $n$ adjacent boxes and started mixing them. To avoid getting dirty, she always pours one box over the nearest non-empty box to its left. The experiment ends when all the paint has accumulated in the first box on the left. Each way of gathering all the paint in the first box on the left can be characterized by $n-1$ operations of the form $[i,j]$, with $1 \leq i \leq j \leq n$, meaning: the box $j$ was poured into box $i$. Two ways are considered identical if they use the same operations even if these were not performed in the same order. For example, if in $4$ boxes we have the colors: $VVGV$, the sequence of operations $[1,2][3,4][1,3]$ indicates the succession of operations: pour box $2$ over box $1$ (box $2$ becomes empty), then box $4$ over box $3$ (box $4$ becomes empty), and finally box $3$ over box $1$. This way is identical to the one defined by the sequence of operations $[3,4][1,2][1,3]$.

## Task
Given the number $n$, and the $n$ colors in the boxes, determine the number of ways Mara can combine the colors from the $n$ boxes to finally obtain the color $V$, modulo $666013$.

## Input data

The input file `colors.in` contains on the first line the natural number $n$, and on the second line, a sequence of $n$ letters from the set $\{'V', 'G'\}$ not separated by spaces (representing, in order, the colors found in the $n$ boxes).

## Output data

The output file `colors.out` will contain on the first line a natural value representing the number of ways Mara can combine the colors from the $n$ boxes to finally obtain the color $V$, modulo $666013$.

## Constraints and clarifications

$1 \leq n \leq 1000000$

## Example

Input `colors.in`: 
```
4
VVGV
```

Output `colors.out`: 
```
2
```

## Explanation

There are $6$ ways of combining the colors from the $4$ boxes, defined by the sequences: 
$[1,2][1,3][1,4]$ for $VVGV$ $\rightarrow$ $G$-$GV$ $\rightarrow$ $V$--$V$ $\rightarrow$ $G$---
$[1,2][3,4][1,3]$ for $VVGV$ $\rightarrow$ $G$-$GV$ $\rightarrow$ $G$-$G$- $\rightarrow$ $V$---
$[2,3][1,2][1,4]$ for $VVGV$ $\rightarrow$ $VV$-$V$ $\rightarrow$ $G$--$V$ $\rightarrow$ $G$---
$[2,3][2,4][1,2]$ for $VVGV$ $\rightarrow$ $VV$-$V$ $\rightarrow$ $VG$-- $\rightarrow$ $V$---
$[3,4][1,2][1,3]$ for $VVGV$ $\rightarrow$ $VVG -$ $\rightarrow$ $G$-$G$- $\rightarrow$ $V$---
$[3,4][2,3][1,2]$ for $VVGV$ $\rightarrow$ $VVG -$ $\rightarrow$ $VV$-- $\rightarrow$ $G$---

It can be observed that options $2$ and $5$ perform the same operations in a different order, so they are not considered distinct variants. We have $5$ distinct variants of combining the colors: $1$, $2$, $3$, $4$, and $6$. For two of these variants ($2$ and $4$), the final color obtained is $V$. The answer is $2$.