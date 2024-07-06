## Task

Victor and Radu are brothers. Their mother brought them $n$ football stickers, each sticker having a code printed on its back, a number between $10$ and $999999$. The brothers, wanting as many stickers as possible to stick in their own album, started arguing. Their mother proposes the following way of dividing the stickers: she arranges the $n$ stickers in a line, face down, and each brother, in turn, will take the first available sticker, as well as all stickers that contain two digits that are equal to the two largest digits, not necessarily distinct, from the first sticker taken at that turn. The stickers are available from left to right. Being the youngest, Victor will go first, then the children take stickers alternately until there are no more stickers. At the end, each child counts how many stickers they have in total.

## Task

Given the number $n$ of stickers brought by their mother and the numbers on them in the order they are placed on the table, determine:

1. The two largest digits, not necessarily distinct, on the last sticker on the table before the contest starts.
2. The brother who wins the contest and how many stickers they have.

## Input data

The input file `album.in` contains on the first line a digit $c$ which can only be $1$ or $2$. The second line contains $n$ representing the number of stickers. The third line contains $n$ natural numbers separated by spaces, representing the numbers on the stickers.

## Output data

If the value of $c$ is $1$, only point $1$ from the task will be solved. In this case, the output file `album.out` will contain on the first line, in ascending order, the requested digits.

If the value of $c$ is $2$, only point $2$ from the task will be solved. In this case, the output file `album.out` will contain on the first line the letter $V$ if Victor has more stickers, the letter $R$ if Radu has more stickers, or the letters $V$ and $R$ separated by exactly one space if both have the same number of stickers. The second line will contain the number of stickers of the one who has the most or the number of stickers owned by each in case they have the same number of stickers.

## Constraints and clarifications

* $n$ is a natural number, $3 \leq n \leq 800\ 000$.
* Solving point $1$ from the task earns $40$ points, and solving point $2$ earns $50$ points.
* An additional $10$ points are awarded by default.
* For point $2$, it is guaranteed that for $50\%$ of the tests, $n \leq 100$.
* The numbers on the stickers are natural numbers between $10$ and $999\ 999$.

## Example 1

`album.in`
```
1
7
291 11 992 456 71 13 121
```

`album.out`
```
1 2
```

## Explanation

The task is $1$. On the last sticker on the table is the number $121$, which has the largest two digits $1$ and $2$.

## Example 2

`album.in`
```
2
7
234 122 334 199 463 221 231
```

`album.out`
```
V
4
```

## Explanation

The task is $2$. Victor starts the contest and takes the stickers $234$ (with $3$ and $4$ as the largest two digits), $334$ and $463$. The stickers left on the table are $122 \ 199 \ 221 \ 231$. Then Radu continues, taking the stickers with numbers $122$ (with the largest two digits $2$ and $2$) and $221$. The stickers left are $199$ and $231$. Victor then takes the sticker with the number $199$, and then Radu takes the sticker with the number $231$. Victor wins with $4$ stickers, Radu having only three.