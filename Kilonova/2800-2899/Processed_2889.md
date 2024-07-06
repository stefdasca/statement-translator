Andi is a mischievous boy! Tired after the national exam, he took the Lăptika chocolate without declaring this in writing. Now the whole committee is on his trail! The campus is composed of $N$ buildings, numbered from $1$ to $N$, and between them, there are $M$ direct, bidirectional roads of a certain cost. $K$ of those buildings represent examination centers from which the committee will start searching for Andi. The distance between two buildings, $A$ and $B$, is defined as the minimum sum of the costs of the roads necessary to reach building $B$ starting from building $A$.

# Task 

Knowing the layout of the campus, help Rara find the building that is the farthest from any examination center, so he can save his younger friend.

# Input data

The input file `laptika.in` contains:
* The first line contains the natural numbers $N$, $M$, and $K$, separated by a space;
* The second line contains the indices of the $K$ examination centers, distinct numbers, separated by a space;
* The next $M$ lines each contain $3$ numbers in the form $\{\ A, B, C \ \}$, which represent a direct road between nodes $A$ and $B$ with a cost of $C$.

# Output data 

The first line of the output file `laptika.out` will contain the index of the farthest building from any examination center and the minimum distance to it, separated by a space.

# Constraints and clarifications 

* $2 \leq N \leq 100 \ 000$;
* $N-1 \leq M \leq min(N \cdot (N-1)/2, \ 500 \ 000)$;
* $1 \leq K \leq N$;
* $1 \leq A, B \leq N, \ A\neq B, \ 1 \leq C \leq 1 \ 000$;
* The campus is well designed, it is possible to reach any building from any other building;
* If there are multiple convenient buildings, display the one with the smallest index;
* There may be more than one direct road between $2$ buildings.

| # | Score  | Constraints                                                            |
|---|--------|------------------------------------------------------------------------|
| 1 | 10     | $K=1, C=1$, for any triplet $\{\ A, B, C \ \}$                          |
| 2 | 20     | $C=1$, for any triplet $\{\ A, B, C \ \}$                               |
| 3 | 20     | $K=1$                                                                   |
| 4 | 20     | $N \leq 1 \ 000$                                                        |
| 5 | 30     | No additional constraints                                               |

# Example

`laptika.in`
```
10 13 4
2 5 6 8
2 1 8
2 4 5
2 7 2
1 4 13
1 6 2
1 7 4
7 5 5
5 8 1
5 10 8
6 3 3
6 9 10
6 8 2
8 9 8
```

`laptika.out`
```
9 8
```

# Explanation 

Both building 9 and building 10 are the farthest and have a distance of 8 from the nearest examination center (8 from 8, respectively 5). Since 9 is smaller than 10, it will be the displayed number. 

~[graf.png]