## Task

Lulu is very passionate about little dragons. He will play with his new friend, the little dragon $Smaug$. The two are in a matrix of dimensions $N \times M$. At the top-left corner of the matrix lies the house $(1, 1)$, and at the bottom-right corner of the matrix lies the house $(N, M)$. The goal of the little dragon is to catch $Lulu$, and Lulu's goal is to escape, his only escape being to reach any house on line $N$, before $Smaug$. It is known that the two friends are allowed to move in the 4 directions $(N, S, E, W)$, and both play optimally. Given the positions of the two friends in the matrix, your mission is to predict the winner of the game. In case $Lulu$ arrives at a house at the same time as $Smaug$, it is considered that the little dragon wins the game, even if that house is on the last line. In other words, $Lulu$ wins the game only if he reaches the last line of the matrix without being caught by $Smaug$. Both take one move per second, at the same time. The little dragon makes its move only after $Lulu$ finishes his move, in the same second.

## Input data

The input file `dragonas.in` contains $T$ on the first line, representing the number of tests. For each test, there will be two lines. The first line contains two natural numbers $N$ and $M$ and the second line contains 4 natural numbers $l_1$, $c_1$, $l_2$, $c_2$, representing the position of $Lulu$ in the matrix, and of $Smaug$ respectively.

## Output data

The output file `dragonas.out` contains $T$ lines. On each line $i$ the response for test $i$ will be found: `Lulu`, if $Lulu$ is the winner, or `Smaug` otherwise.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N, M \leq 1000$

$1 \leq l_1, l_2 \leq N$

$1 \leq c_1, c_2 \leq M$

The starting positions of the two friends do not coincide.

Lulu is a boy! You don't have to worry about Lulu's safety, Smaug is a good-hearted little dragon.

## Example

`dragonas.in`:
```
4 
4 4 3 3 4 1 
5 10 2 3 5 1 
4 4 4 2 4 3 
3 3 4 2 2 3 
```

`dragonas.out`:
```
Lulu 
Smaug 
Lulu 
Smaug 
```

## Explanation

In the first test, $Lulu$ takes a step, goes down to house $(4, 3)$. $Smaug$ heads towards house $(4, 2)$, but does not reach him.

In the second test, $Lulu$ cannot reach line $5$ without being caught by $Smaug$.

In the third test, $Lulu$ is already on the last line.

In the fourth test, $Lulu$ cannot go down to the $3$rd line unless he reaches it at the same time as $Smaug$, so $Smaug$ wins.