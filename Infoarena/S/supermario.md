## Task

Fighting turtles is a tough job even for Super Mario, the hero of this problem. How about giving him a helping hand? Super Mario has to face the terrible army of Koopa Troopas turtles. The army is made up of $N$ turtles numbered from $1$ to $N$, arranged from left to right on the $Ox$ axis of our $2D$ game (the turtle with the order number $1$ is the leftmost, and the turtle with the order number $N$ is the rightmost). Super Mario's mission is to destroy all the $N$ turtles on the platform. Super Mario can jump on any chosen turtle among the $N$. Out of fear, the turtle will hide in its shell, and Super Mario will be able to use it as a weapon to destroy the other turtles. Each turtle $i$ has a power equal to $P[i]$. If Super Mario jumps on turtle $i$ and chooses to push it to the right, this turtle will destroy all the turtles to its right until it encounters the first turtle whose power is strictly greater than turtle $i$. Similarly, if Super Mario jumps on turtle $i$ and chooses to push it to the left, it will destroy all the turtles to its left until it encounters the first turtle whose power is strictly greater than turtle $i$.

In other words: 

Super Mario jumps on turtle $i$ and pushes it to the right. Let $k$ $(i < k)$ be the smallest number such that $P[i] < P[k]$. All turtles $j$ $(i < j < k)$ will be destroyed, including turtle $i$. If there is no $k$ in the array with this property, the turtle will destroy all the turtles to its right, including itself.

Super Mario jumps on turtle $i$ and pushes it to the left. Let $k$ $(k < i)$ be the largest number such that $P[i] < P[k]$. All turtles $j$ $(k < j < i)$ will be destroyed, including turtle $i$. If there is no $k$ in the array with this property, the turtle will destroy all the turtles to its left, including itself.

Given $N$ and an array of natural numbers $P[i]$, determine the minimum number of turtles Super Mario needs to jump on and push, in any direction he wants, to destroy all $N$ turtles.

## Input data

The input file `supermario.in` contains a natural number $N$ on the first line. The second line contains $N$ natural numbers $P[i]$, with the meaning described in the statement.

## Output data

The output file `supermario.out` will contain a single natural number, representing the minimum number of turtles Super Mario needs to jump on to destroy them all.

## Constraints

$1 \leq N \leq 10^5$

$1 \leq P[i] \leq 10^9$

The powers of the turtles are guaranteed to be pairwise distinct.

## Example

`supermario.in`
```
13
1 2 4 3 15 14 13 12 11 10 9 8 7
```

`supermario.out`
```
2
```

`supermario.in`
```
1
123456
```

`supermario.out`
```
1
```

## Explanation

For the first example:

Initial array of turtles: $1 \ 2 \ 4 \ 3 \ 15 \ 14 \ 13 \ 12 \ 11 \ 10 \ 9 \ 8 \ 7$

Super Mario will jump on the turtle with power $14$ and push it to the right. Thus, the array of turtles becomes: $1 \ 2 \ 4 \ 3 \ 15$

Now, Super Mario will jump on the turtle with power $15$ and push it to the left. All turtles will be destroyed.

For the second example: Super Mario will jump on the only turtle in the array and push it either to the right or to the left.