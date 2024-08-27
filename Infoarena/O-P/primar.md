# Mayor

Dubluveu was recently elected mayor in Popricani. To secure structural funds for the commune's development, the newly elected mayor must quickly appoint local councilors. Because during the electoral campaign he promised the people of Popricani that he would not make any discriminations (unlike the previous mayor), he must adhere to the following rules: The Local Council should have $N$ employees (one employee from each house, out of the $N$ in the commune) both men and women should be hired the total discrimination value should be minimal. We can consider the commune as a Cartesian plane, where the houses are represented by points, and the streets are represented by lines parallel to the coordinate axes, on which there is at least one house (see figure). Discrimination on such a street is equal to the absolute difference between the number of men and the number of women chosen for the Local Council. Total discrimination is the sum of the discriminations on each street. The red lines represent the streets, while the blue lines connect houses that are not on the same street. For example, houses $1$, $2$, $3$ and $4$ are on the same street. Similarly, houses $5$, $6$ and $7$ are on the same street. However, houses $1$ and $5$ are on different streets as the line passing through points $1$ and $5$ is not parallel to either $OX$ or $OY$. To understand the drawing better, we can say that two houses are on the same street if and only if they have the same x-coordinate or the same y-coordinate.

## Task

As the campaign manager of Mayor Dubluveu, you need to determine a selection of the $N$ councilors that respects the promises made to the people of Popricani and has a minimal total discrimination.

## Input data

The first line of the input file $$primar.in$$ contains the number $N$.  
The next $N$ lines contain the coordinates of the houses.

## Output data

In the output file $$primar.out$$, you will print, on the first line, the minimum obtained discrimination value, and on the second line, a sequence of $N$ numbers from the set $\{0, 1\}$. Thus, the $i$-th number will represent your choice for the $i$-th house from the input file. ($0$ - you have appointed a man from house $i$, $1$ - you have appointed a woman from house $i$)

## Constraints and clarifications

$1 \leq N \leq 131072$  
the coordinates of the houses are integers whose values do not exceed, in absolute value, $2000000000$  
if a street has only one house, then regardless of the choice made, the discrimination on that street will be $0$.  
at least one man and one woman live in each house  
there are no two houses at the same coordinate  
you will receive $40\%$ of the points for correctly determining the minimum discrimination  
and $100\%$ if you correctly solve the entire task

## Example

$$primar.in$$
```
5
0 0
0 1
1 0
1 1
1 2
```

$$primar.out$$
```
1
1 0 0 1 0
```

## Explanation

From the houses $2$, $3$, and $5$ you will choose a man each, and from houses $1$ and $4$ you will choose a woman each. On streets $1$, $2$, and $4$, the difference between the number of men (blue points) and the number of women (red points) is $0$. On street $3$, the difference is $1$. The total discrimination value is $1$, being the minimum possible in this example. If you consider the street parallel to $OX$ that passes through the coordinate point $(1,2)$, it can be observed that this street does not pass through any other point given in the input file. Therefore, the discrimination on street $5$ will be $0$. Even if you were to choose a woman from that house, the discrimination on street $5$ would still remain $0$, but the discrimination on street $3$ would increase, thus increasing the total discrimination as well.