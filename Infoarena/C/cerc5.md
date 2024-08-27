# Cerc5

Ionel is at gym class. The children are lined up in a row and have distinct numbers from the interval $[1, N]$ printed on their shirts. Ionel proposes they participate in two games. In the first game, because Ionel likes order, he thinks about determining the minimum number of colleagues he would need to remove from the row so that the remaining ones have their shirt numbers in increasing order. After the removal, $M$ children remain in the row. In the second game, the $N$ children rearrange themselves such that their shirt numbers are in order, and they sit in a circle, facing the interior of the circle. The child with number $1$ sits on a spot marked with red, the child with number $2$ is to his right, and so on. Each child numbered $i$ has to his right the child numbered $i + 1$, except for the child numbered $N$ who has to his right the child numbered $1$. The game proceeds as follows: In stage $i$, the child standing on the red-marked spot will switch places $p_i$ times with the child to his right, $p_i$ being the $i$-th element from the prime numbers sequence.

## Task

Given the number $N$ of children and the numbers on their shirts in the row they were initially arranged in, determine:
For the first game, the number $M$ of children that remain so that their shirt numbers are in strictly increasing order.
For the second game, who will be the neighbors to the right and to the left of the child with number $1$ after $k$ stages of the game.

## Input data

In the file `cerc5.in`, the first line contains three natural numbers separated by spaces: $p$ – the number of the game $(1$ or $2)$, $N$ – the number of children $K$ – the number of stages of the second game. The next line contains $N$ non-zero natural numbers, distinct from each other, separated by spaces, representing the numbers on the children's shirts, in the order they are initially lined up.

## Output data

If the value of $p$ is $1$, only task $1$ will be solved. In this case, the output file `cerc5.out` will contain a natural number $M$ representing the number of remaining children.
If the value of $p$ is $2$, only task $2$ will be solved. In this case, the output file `cerc5.out` will contain two natural numbers, representing, in this order, the neighbor to the right and the neighbor to the left of the child with number $1$ after the $K$ stages.

## Constraints and clarifications

$3 \leq N \leq 100000$

$1 \leq K \leq 50000$

## Example

`cerc5.in`
```
1 5 3
1 3 2 4 5
```
`cerc5.out`
```
4
```

`cerc5.in`
```
2 5 3
1 2 3 4 5
```
`cerc5.out`
```
3 5
```

## Explanation

### Example 1

After playing the first game, $4$ children remain in the row.

### Example 2

Initially, the children are arranged in the order $1, 2, 3, 4, 5$. Player $1$ is on the red spot. In stage $1$, player $1$ switches places twice with the one on his right, and thus the children will be in the order $2, 3, 1, 4, 5$. After the first stage, player $2$ reaches the red spot. In stage $2$, player number $2$ switches places $3$ times with the player to his right, and the order becomes: $3, 1, 4, 2, 5$. In stage $3$, player number $3$ switches places $5$ times with the player to his right and the order becomes: $3, 4, 2, 5, 1$. Finally, player number $1$ has to his right player number $3$ and to his left player number $5$.