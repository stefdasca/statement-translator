## Lock

The devil's lock is an old Chinese toy. It consists of metal rings mounted on a wooden rod such that the rod of one ring passes through the next ring. When the lock is closed, the rods are locked in an oval-shaped wooden support. The lock must be opened, meaning the rings need to be detached from this oval support (taken off). The rings are numbered from left to right with numbers from $1$ to $N$. In one step, a single ring can be freed or placed back, following these rules: The first ring can be freed or placed back at any time. Each ring, numbered $i > 1$, can be freed or placed back if and only if the ring numbered $i-1$ is caught in the oval support (it is up) and all rings numbered less than $i-1$ are freed (they are down). The lock is opened if all rings are freed (they are down).

## Task

Determine the minimum number of steps needed to open the lock and specify these steps! A step consists of freeing a single ring or placing a single ring back.

## Input data

The input file `lacat.in` contains on the first line a natural number $N$, representing the number of rings.

## Output data

The output file `lacat.out` will contain on the first line a natural number, representing the minimum number of steps needed to open the lock. Starting from the second line, the following lines of the output file will describe the steps that lead to the lock opening: Corresponding to the freeing of the $i$-th ring, the file will contain the letter $'J'$, followed by $i$. Corresponding to placing back the $i$-th ring, the file will contain the letter $'S'$, followed by $i$.

## Constraints and clarifications

$2 < N \leq 22$

## Example

`lacat.in`

```
3
```

`lacat.out`

```
5
J1
J3
S1
J2
J1
```

## Explanation

$Down$ $1$ (the first ring can be freed anytime)

$Down$ $3$ (ring $3$ can be freed because $1$ is down and $2$ is up)

$Up$ $1$ (the first ring can be placed up anytime; we need it up to free ring $2$)

$Down$ $2$ (now ring $2$ can be freed)

$Down$ $1$ (we can also free ring $1$)