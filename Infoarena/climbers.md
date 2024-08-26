## Task

A mountain can be represented as a broken line that starts and ends at sea level (altitude $0$) and has strictly positive altitudes between the two ends (these are called interior altitudes). Alice starts climbing the mountain from one end, while Bob climbs it from the other. They can move along the mountain, forward or backward, but the two must be at the same altitude (between them). The effort made by Alice on a route is the absolute sum of the change in altitude. More precisely, if Alice's route starts at $h_1 = 0$, changes direction at altitudes $h_2$, $h_3$, $\dots$, $h_{p-1}$, and ends at $h_p$, then the effort is $|h_2 - h_1| + |h_3 - h_2| + \dots + |h_p - h_{p-1}|$ (Bob will exert the same effort).

## Input data

The mountain is encoded as an array of $N$ integers representing the segment endpoints' altitudes. The first line of the input file `climbers.in` contains $N$. The second line contains the $N$ numbers. It is guaranteed that $h_1 = h_n = 0$.

## Output data

In the output file `climbers.out`, print a single integer: the minimal effort required (by Alice) for Alice and Bob to meet. If the two cannot meet, print NO.

## Constraints

$3 \leq N \leq 5\,000$

Interior altitudes are between $1$ and $1\,000\,000$.

For $25\%$ of the score, all interior altitudes are distinct.

For $30\%$ of the score, $N \times H < 45\,000$, where $H$ is the maximum altitude.

## Example

`climbers.in`

```
5
0 4 2 7 0
```

`climbers.out`

```
11
```

## Explanations

In the first example, Alice starts from the left end, while Bob starts from the right end. Alice and Bob move towards each other until the altitude $4$. Then, Alice moves forward to the altitude $2$, while Bob moves backward. Finally, the two move towards each other until they meet at the altitude $7$. The effort made is $|4-0| + |2-4| + |7-2| = 4 + 2 + 5 = 11$.