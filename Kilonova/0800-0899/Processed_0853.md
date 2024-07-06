# Hard Disk

A hard disk is a device used for data storage. Data is stored on a magnetic surface arranged on round metallic platters. On a platter, data is organized into **tracks** and **sectors**, and the area at the intersection of a track and a sector is called a **cluster**.

A cluster can have two states: **free**, if it does not contain data, or **occupied**, when it contains data.

A platter is called **defragmented** if all occupied clusters on each track are arranged in consecutive order. Defragmentation is achieved by moving some occupied clusters and aims to reduce data access time. Moving a cluster means transferring data from an occupied cluster to a free cluster on the same track.

~[defrag.png|width=90em|align=center]

# Task
Given the number of tracks $P$ and sectors $S$ of a platter, the number and position of the occupied clusters, write a program that determines:
1. the number of tracks that have all clusters free;
2. the **minimum** number of cluster moves, for each track, needed to make the platter defragmented.

# Input data
The input file `defrag.in` contains on the first line a natural number $V$ whose value can only be $1$ or $2$.
The second line of the input file contains two natural numbers $P$ and $S$, separated by a space, as described in the statement.
The third line contains a natural number $C$ representing the total number of occupied clusters on the platter, and each of the following $C$ lines contains a pair of values $p_i$ and $s_i$, $1 \\leq i \\leq C$, separated by a space, representing the track and sector where each occupied cluster is located.

# Output data
The output file is `defrag.out`.
If the value of $V$ is $1$, then the output file will contain on the first line a natural number representing the number of tracks that have all clusters free.
If the value of $V$ is $2$, then the output file will contain on the first line $P$ natural numbers labeled $M_i$, $1 \\leq i \\leq P$, separated by a single space, where $M_i$ represents the minimum number of cluster moves, among those on track $i$, needed to make the occupied clusters on track $i$ arranged in consecutive order.

# Constraints and clarifications
- $1 \\leq P \\leq 100$
- $1 \\leq S \\leq 360$
- $1 \\leq C \\leq P \\cdot S$
- The tracks are numbered from $1$ to $P$ starting with the outermost track.
- The sectors are numbered from $1$ to $S$ clockwise starting with sector $1$.
- If a track has all clusters free, then the required value for the second task is $0$.
- $20\%$ of the tests will have the value $V = 1$, and $80\%$ of the tests will have the value $V = 2$.

# Example 1
`defrag.in`
```
1
4 8
10
1 1
1 3
1 5
1 7
4 5
4 1
4 6
4 8
2 2
2 4
```
`defrag.out`
```
1
```
## Explanation
The data corresponds to the previous figures. $V = 1$, so **ONLY** the first task is solved.
- The number of tracks is $P = 4$, the number of sectors is $S = 8$.
- The total number of occupied clusters is $C = 10$ (the ones marked in black).
- On the first track there are $4$ occupied clusters in sectors $1$, $3$, $5$, and $7$. 
- On the second track there are $2$ occupied clusters in sectors $2$ and $4$.
- On the third track, there are no occupied clusters.
- On the fourth track there are $4$ occupied clusters in sectors $1$, $5$, $6$, and $8$.
Only one track has all clusters free, track number $3$, so the required value is $1$.

# Example 2
`defrag.in`
```
2
4 8
10
1 1
1 3
1 5
1 7
4 5
4 1
4 6
4 8
2 2
2 4
```
`defrag.out`
```
2 1 0 1
```
## Explanation
The data corresponds to the previous figures. $V = 2$, so **ONLY** the second task is solved.
- On the first track, a minimum of two cluster moves are needed for all occupied clusters to be in consecutive order, so the required value is $2$.
- On the second track, a single cluster move is sufficient for all occupied clusters to be in consecutive order, so the required value is $1$.
- On the third track, there are no occupied clusters, so the required value is $0$.
- On the fourth track, a single cluster move is sufficient for all occupied clusters to be in consecutive order, so the required value is $1$.