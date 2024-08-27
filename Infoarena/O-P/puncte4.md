# Points4

Bulbuka is a very diligent student. During math classes, she draws points in some squares on a notebook page and then surrounds them with a rectangle of size $N*M$ $(N \leq M)$ drawn along the printed lines on the page. One day, she noticed that some of the rectangles she drew had a special property: all squares of size $N*N$ included in the rectangle had the same number of points (let's call it $P$) drawn inside. After class, the teacher called her to ask what she was drawing so interestingly during the class. Bulbuka enthusiastically explained her discovery, and the teacher proposed a special task: for three given values $N$, $M$ and $P$, to determine how many ways there are to draw the points. Bulbuka immediately accepted but, since she doesn't know how to write very large numbers, she decided to present the answer modulo $1000000007$ $(10^9 + 7)$. Once at home, she discovered that the problem is more difficult than she initially thought and that she would need many notebooks to write down all the possible solutions. Therefore, she asks for your help.

## Task

Given $N$, $M$ and $P$, display the required result modulo $1000000007$ $(10^9 + 7)$.

## Input data

The first line of the file `puncte4.in` contains the three numbers $N$, $M$ and $P$, separated by a space.

## Output data

The file `puncte4.out` will contain on the first line a single number representing the required result.

## Constraints and clarifications

$2 \leq N \leq 100$

$N \leq M \leq 10^{18}$

$0 \leq P \leq N^2$

For $40 \%$ of the tests $N < 9$

## Example

`puncte4.in`

```
3 4 1
```

`puncte4.out`

```
15
```

## Explanation

The gray area represents the area contained by both squares of size $3 \times 3$. We can place the point either in the gray area $(6 possibilities)$, or in both white areas $(3 \times 3 = 9 possibilities)$.

`puncte4.in`

```
3 4 2
```

`puncte4.out`

```
78
```