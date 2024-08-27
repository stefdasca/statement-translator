# Fence

A team of $K$ workers has been hired to paint a fence consisting of $N$ planks numbered from $1$ to $N$, from left to right. Each worker $i$ $(1 \leq i \leq K)$ stands in front of plank $S_i$ and can paint only a compact interval (i.e., the list of job numbers within the interval are consecutive) having at most $L_i$ planks, an interval that must include plank $S_i$. For each painted plank, the worker is paid the amount $P_i$. For efficiency reasons, any $2$ workers from the team must paint disjoint intervals of planks (i.e., any plank of the fence can be painted by at most one team member). Being the team leader, you want to determine for each team member the interval of planks they will have to paint, so that the total earnings are maximized. The total earnings are equal to the sum of earnings made by each team member. The amount earned by each worker is equal to the number of planks they painted multiplied by $P_i$ (for worker number $i$).

## Task

Write a program that determines the maximum earnings obtained by the $K$ workers.

## Input Data

The input file `gard.in` contains:
```
gard.in
Meaning
N K
L_1 P_1 S_1
L_2 P_2 S_2
$\dots$
L_K P_K S_K
```

$N$ - the number of planks;

$K$ - the number of workers;

$L_i$ - the maximum number of planks that can be painted by worker number $i$;

$P_i$ - the amount received by worker $i$ for each painted plank; 

$S_i$ - the plank in front of which worker $i$ is standing.

## Output Data

In the output file `gard.out` you will print the maximum earnings obtained by the entire team of workers.

## Constraints and clarifications

$1 \leq N \leq 16\ 000$
 
$1 \leq K \leq 100$

$1 \leq P_i \leq 10\ 000$

$1 \leq L_i, S_i \leq N$

All numbers $S_i$ will be distinct.

Not all $N$ planks of the fence need to be painted.

It is allowed for one or more team members to not paint any planks, in which case the plank in front of which they initially stood can be painted, possibly, by another worker.

## Example

`gard.in`

```
8 4
3 2 2
3 2 3
3 3 5
1 1 7
```

`gard.out`

```
17
```

## Explanation

Worker 1 paints the interval of planks $[1, 2]$;

worker 2 paints the interval of planks $[3, 4]$;

worker 3 paints the interval of planks $[5, 7]$;

worker 4 does not paint any plank.