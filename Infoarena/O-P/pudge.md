## Task

Pudge is positioned at the point $(X,Y)$ on a plane and has a hook of width $D$ $(D$ is even$)$. He can throw the hook to any point $(X_0, 0)$, $0 \le X_0 \le X$ integer; the time for the hook to reach the $Ox$ axis is equal to the length of the segment formed by Pudge's position and the point where he throws the hook. On the $Ox$ axis, there are several enemies, each enemy is at position $P_i$ and has a constant speed $V_i$ per unit of time (all enemies move on the $Ox$ axis towards $+\infty$). If Pudge throws the hook to the point $X_0$, it will catch all enemies who are in the interval $[X_0 - \frac{D}{2}, X_0 + \frac{D}{2}]$ at the moment the hook reaches the $Ox$ axis. Calculate the maximum number of enemies that Pudge can catch with a single throw of the hook.

## Input data

The input file `pudge.in` contains on the first line $X$, $Y$, $D$, and $N$, which represent the number of enemies. There are $N$ lines, each having 2 numbers $P_i$, the initial position of the enemy, and $V_i$, the speed of the enemy.

## Output data

In the output file `pudge.out`, print the maximum number of enemies that Pudge can catch.

## Constraints and clarifications

$1 \le N \le 100000$

$0 \le X, Y, D \le 10^8$, integers

$0 \le P_i \le 10^8$ integer,

$0 \le V_i \le 10$ integer, for each enemy.

$0 \le X_0 \le X$

Pudge throws the hook at time $0$.

For 20% of the score, $V_i = 0$ for all enemies and $0 \le X, Y, D, P_i \le 10^6$.

For another 20% of the score, $1 \le N \le 1000$ and $0 \le X, Y, D, P_i \le 1000$.

For another 40% of the score, $0 \le X, Y, D, P_i \le 10^6$.

For another 20% of the score, the initial constraints.

## Example

`pudge.in`

```
10 2 4 5
12 1
2 2
7 0
4 1
3 4
```

`pudge.out`

```
3
```

## Explanation

For the first example: Pudge can throw the hook to the point $8$ to catch $3$ enemies. The hook will reach the $Ox$ axis at point $8$ at time $\dots$.