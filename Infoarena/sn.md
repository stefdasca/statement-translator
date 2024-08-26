# National Security

Since he has been defeated too many times at the 'Grid Game' by the President, the Prime Minister is planning a coup. Fortunately, Doubleveue was informed in time of the Prime Minister's intentions and plans to organize a solid defense. The Presidential Palace is strategically placed, and it can only be reached by a single road of length $L$ kilometers. At its edge, Doubleveue calls for the placement, in $N$ fixed locations, of exactly one of the following two types of devices: ground-to-ground missile launchers and ground-to-air missile launchers. If a device (regardless of type) is placed at location $i$, it will be able to destroy any form of life within the interval $[a_i , b_i]$. To ensure that the Prime Minister cannot reach him, Doubleveue wants every point on the road to be guarded by both types of devices.

## Task

As the Secretary General of the Supreme Defense Council, you must organize the placement of one type of missile launcher in each of the $N$ locations. If there are multiple solutions, any of them can be displayed.

## Input data

The input file `sn.in` will contain two numbers $L$ and $N$ on the first line. The next $N$ lines each contain two numbers $a_i , b_i$, with the meaning that a device placed at location $i$ will be able to destroy any form of life within the interval $[a_i , b_i]$.

## Output data

The output file `sn.out` will contain $N$ lines. The line $i$ will contain the type of missile launcher placed in that location (print $0$ if a ground-to-ground missile launcher is placed in $i$, respectively $1$ in the other case). It is guaranteed that for the test data there will always be a solution.

## Constraints and clarifications

$1 \leq N, L \leq 1\,000\,000$

$1 \leq a_i \leq b_i \leq L$

- The intervals will be given in increasing order of $a_i$ and, in case of equality, in increasing order of $b_i$.
- Each point is contained in at least two intervals from the input file.
- Only one type of missile launcher can be placed in a location.

## Example

`sn.in`
```
7 4
1 3
1 5
3 7
5 7
```

`sn.out`
```
1
0
1
0
```