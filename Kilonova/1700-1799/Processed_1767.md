The young queen bee has decided to leave the hive and start her own family of bees, which is not an easy task. She, along with her bees, must move from flower to flower until they reach the edge of the plantation. The plantation has a rectangular shape with $N$ rows (numbered from $1$ to $N$) and $M$ columns (numbered from $1$ to $M$). There is a flower at each point. Flowers are coded with $0$ or $1$, those coded with $0$ can only be occupied by the queen, while those with value $1$ can only be occupied by a bee. The swarm of bees starts from the left edge of the plantation (column $1$) and must reach the right edge (column $M$). At each step, all the bees (including the queen) must be on consecutive positions in the same column. At the next step, they can move only to the next column, still on neighboring positions (they can change order if needed). The effort required to move from one column to another is equal to the difference between the first row occupied by a member of the bee swarm (queen or bee) in the previous step and the first row occupied by a member of the bee swarm (queen or bee) after moving.

# Task

Determine the maximum number of members of the bee swarm (queen + bees) that can leave the hive to traverse the entire plantation to form a new family. Also determine the minimum total effort with which the queen can traverse the plantation with the maximum number of determined bees.

# Input data

The first line of the input file `albine.in` contains two natural numbers $N$ and $M$ separated by a space, representing the number of rows and the number of columns of the plantation.
The next $N$ lines contain $M$ numbers from the set $\\{0, 1\\}$, separated by a space, representing the codes of the flowers on each row of the plantation.

# Output data

The first line of the output file `albine.out` contains $2$ natural numbers separated by a space, representing the maximum number of members of the bee family (queen + bees) that can traverse the plantation (including the queen) and the minimum crossing cost of the plantation.

# Constraints and clarifications

* $1 \\leq N, M \\leq 1\ \\000$;
* For $50\\%$ of tests $1 \\leq N, M \\leq 300$;
* A bee swarm consists of a queen and $0$ or more bees.
* It is guaranteed that a path exists.
* The queen can traverse the plantation alone.
* For correctly solving only the first requirement, $30\\%$ of the score is awarded.

# Example

`albine.in`
```
5 3
0 1 0
0 0 1
1 1 0
1 1 1
0 0 0
```

`albine.out`
```
3 0
```

## Explanation

Another possible way (not the only one) to cross the plantation would have been for the group of $3$ bees to settle on the first column starting at position $3$, on the second column starting at position $1$, and on the third column starting at position $2$. In this case, the total cost would have been $3$.