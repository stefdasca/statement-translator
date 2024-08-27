Flowers5

After a numbness that lasted more than $3$ months, Mother Nature realized that spring was just around the corner, and the flowers with which she soon had to fill the fields were not yet ready. Before winter began, she worked to combine hues to create colorful flowers, and now she has a room full of disks of various colors, waiting to be assembled into vibrant flowers, either as centers or petals. To form a flower, Mother Nature chooses a center of any color and at least $K$ petals. At the same time, she does not wish to disrupt the natural order of things and will never use two different colors of petals for the same flower. However, she does allow flowers with petals and centers of the same color. Because time is short and Mother Nature has more important things to do than sit around assembling flowers, she calls on all her friends for help and wants to give each of them something to work on. For this, she has an array $D$ of $N$ numbers, where the number at position $i$ in the array represents the number of disks of color $i$ she has prepared. Then, Mother Nature asks $M$ questions of the form $x$ $y$, through which she wants to find out the maximum number of flowers that can be formed using only disks of colors in the interval $[x, y]$ from the array $D$.

## Input data

The first line of the file `flori5.in` will contain $2$ natural numbers, $N$ and $K$, separated by space, with the meaning given in the statement. On the next line, there will be $N$ natural numbers (the elements of the array $D$). The next line of the file will contain the number $M$ and will be followed by $M$ lines containing pairs of integers $x$ and $y$, with the meaning given in the statement.

## Output data

In the file `flori5.out`, there will be printed, on separate lines, $M$ natural numbers, representing the answer to each of the $M$ questions.

## Constraints and clarifications

$1 \leq N \leq 10^5$

$1 \leq D[i] \leq 10^9$, $Ɐ$ $i = 1,N$

$1 \leq M \leq 10^5$

$1 \leq K \leq 1000$

$1 \leq x \leq y \leq N$

## Example

`flori5.in` 
```
4 4
4 2 1 10
2
1 3
1 4
```

`flori5.out`
```
1
3
```

## Explanation

For the first question, Mother Nature can choose a single flower with petals of color $1$ and the center of color $2$ or $3$. For the second question, we can form $3$ flowers:
```
3
4 4 4
```
An alternative: for the second flower, we use fewer petals, ultimately keeping two flowers unused of color $4$.