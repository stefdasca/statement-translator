Tibi is a math enthusiast and a talented artist. During school, he learned to work with intervals of numbers, which he visually represents on drafts using colored and stylized segments in different ways for a better understanding of the problem he is solving. After finishing his math homework, his drafts are filled with various types of segments, each representing a closed interval between the numbers in the solved problems. One day, he looked at his drafts and thought of a problem he invites you to solve:

# Task
Given a number $n$ of different segments. Each segment $1 \leq i \leq n$ is defined by its type ($tip_i$), starting point ($st_i$), and endpoint ($dr_i$). The segment includes all points in the interval $[st_i , dr_i]$, inclusive, and satisfies the condition $tip_i \leq k$, where $k$ is the total number of different types. Two segments are considered connected if they have at least one common point and are of different types. They belong to the same group if they are directly connected or through a sequence of directly connected segments. Your task is to determine the number of segment groups formed on each of Tibi's drafts.

# Input data
The input file `segmente.in` contains on the first line a natural number $t$ representing the number of test cases (drafts). Each case has the following structure:
- The first line of a test case contains two integers $n$ and $k$.
- The next $n$ lines contain a triplet of the form ($tip_i, st_i, dr_i$), defining the $i$-th segment of the test case, where $1 \leq i \leq n$.

# Output data
For each of the test cases, $t$, print in the output file `segmente.out` the number of groups that the segments form in that case on a separate line.

# Constraints and clarifications
- $1 \leq t \leq 1\ 000$
- $1 \leq n \leq 200\ 000$
- $1 \leq k \leq 1\ 000$
- $1 \leq tip_i \leq 1\ 000$ and $0 \leq st_i \leq dr_i \leq 10^9$ for any $i$ from $1$ to $n$.
- It is guaranteed that the sum of the values of $n$ across all test cases (denoted by $ \sum{n}$) does not exceed $200\ 000$ (all of Tibi's drafts do not have more than $200\ 000$ segments).

| # | Points | Constraints |
|---|--------|------------------------------|
| 1 | 4      | $k = 1$, $ \sum{n} \leq 5\ 000$ |
| 2 | 6      | $k = 1$, $ \sum{n} \gt 5\ 000$  |
| 3 | 8      | $k = n$, $ \sum{n} \leq 5\ 000$ |
| 4 | 12     | $k = n$, $ \sum{n} \gt 5\ 000$  |
| 5 | 16     | $k = 2$, $ \sum{n} \leq 5\ 000$ |
| 6 | 24     | $k = 2$, $ \sum{n} \gt 5\ 000$  |
| 7 | 12     | $3 \leq k \leq 1\ 000$, $ \sum{n} \leq 5\ 000$ |
| 8 | 18     | $3 \leq k \leq 1\ 000$, $ \sum{n} \gt 5\ 000$  |

# Example
`segmente.in`
```
3
6 3
1 2 5
2 4 9
1 7 12
1 11 15
3 14 18
3 17 20
4 4
1 1 4
3 2 7
4 5 7
2 8 10
7 2
2 3 8
1 13 13
1 1 4
2 5 7
1 8 11
1 10 13
2 12 14
```
`segmente.out`
```
3
2
3
```

## Explanation
In this case, the following connections are formed:
- Segment $1$, $[2, 5]$, is directly connected with segment $2$, $[4, 9]$ because they are of different types and intersect in the interval $[4, 5]$ (they have at least one common point).
- Segment $2$, $[4, 9]$, is directly connected with segment $3$, $[7, 12]$ because they are of different types and intersect in the interval $[7, 9]$ (they have at least one common point).
- Segment $3$ and segment $4$ have a non-empty intersection, however, they are of the same type so they are not directly connected.
- The rest of the segments have no common intersection with segments $1$, $2$, and $3$, thus segments $1$, $2$, and $3$ are part of the same group.
- Segment $4$, $[11, 15]$, is directly connected with segment $5$, $[14, 18]$ because they are of different types and intersect in the interval $[14, 15]$ (they have at least one common point).
- Segment $4$ and segment $5$ have a non-empty intersection, however, they are of the same type so they are not directly connected.
- The remaining segments do not have a common intersection with segments $4$ and $5$, thus segments $4$ and $5$ are part of the same group.
- Segment $6$ is not connected with any other segment, thus it forms a group by itself.

Thus, a total of $3$ groups are formed.

~[img.png|width=47em]