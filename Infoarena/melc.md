## Task

The tests for this problem are not well constructed to correctly differentiate between inefficient or incorrect solutions. Enter here if you want to help us improve the quality of the tests for this problem! In Romania, all snails are lazy. Let's take the snail Gigel, for example. He has to visit $N$ friends who are located at distinct coordinates in the plane. But since Gigel is too lazy, he doesn't want to leave his house. However, he said that he would go visit his friends if someone can show him the right path to follow. Gigel would be willing to leave his house, visit all his friends, and return back home. Between the houses of two friends, between his house and a friend's house, or between a friend's house and his own, Gigel travels in a straight line segment that connects them. Thus, his path consists of a succession of $N+1$ segments. Gigel wants any two segments within his path not to intersect (except, at most, at their endpoints). Find a suitable path for Gigel.

## Input data

The first line of the input file `melc.in` will contain 2 real numbers, separated by a space: $X$ and $Y$, representing the coordinates of Gigel's house. The second line contains the integer $N$, representing the number of friends Gigel has to visit. The next $N$ lines each contain 3 numbers, separated by a space: $X$, $Y$, and $ID$. $ID$ will be an integer, representing the identifier of one of Gigel's friends. $X$ and $Y$ are 2 real numbers, representing the coordinates of the house of the friend identified by the value of $ID$.

## Output data

In the output file `melc.out` you will print $N+2$ lines: the identifiers of the friends whose houses Gigel will visit, in the order he visits them. Start with Gigel's identifier (which is the number $0$), continue with the identifier of the first friend he visits, and so on. End again with Gigel's identifier. If there is no solution, print only the number $-1$.

## Constraints and clarifications

$2 \leq N \leq 1\ 000$

$-200\ 000 \leq$ coordinates $X$ and $Y$ of any point $\leq 200\ 000$

Coordinates of points are given with a precision of at most 3 decimals.

The identifiers of Gigel's friends are distinct integers, ranging from $1$ to $N$.

Any three friends (including Gigel) do not have their houses on the same straight line.

## Example

`melc.in`

`0 0`
`3`
`3 3 1`
`6 0 2`
`6 2 3`

`melc.out`

`0`
`1`
`3`
`2`
`0`