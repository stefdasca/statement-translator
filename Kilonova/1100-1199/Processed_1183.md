In a mountainous area, there is a desire to open a network of cable cars. The cable car stations can be established on any of the $N$ peaks of the mountainous region. The peaks are given in order from left to right and numbered from $1$ to $N$, each peak $i$ being specified by the coordinate $X_i$ on the OX axis and by the height $H_i$.

Exactly $K$ cable car stations will be established. Cable car station $i$ will be connected with stations $i-1$ and $i+1$; station $1$ will be connected only with station $2$, and station $K$ only with station $K-1$. Station $1$ will obligatorily be placed on peak $1$, and station $K$ on peak $N$.

The aim is for the cable car network to ensure a connection between peak $1$ and peak $N$. Moreover, the total length of the cables used for connection should be minimized. The length of the cable used to connect two stations is equal to the distance between them. Additionally, a cable connecting two consecutive stations cannot have a length greater than a fixed length $L$.

An additional restriction is introduced by the terrain shapes. Thus, peaks $i$ and $j$ ($i < j$) cannot be directly connected if there is a peak $v$ ($i < v < j$) such that the straight segment that would unite peaks $i$ and $j$ does not pass above peak $v$. In the case where the three peaks are collinear, all three are considered as stations, even if the distance between peaks $i$ and $j$ is less than $L$.

# Task

Given the placement of the $N$ peaks of the mountain chain, determine a way to place the $K$ cable car stations so that the total length of the cables used for connection is minimized, with the above restrictions. It is guaranteed that, in all given tests for evaluation, the connection will be possible.

# Input data

The first line of the `munte.in` file contains three integers $N$, $K$, and $L$ separated by spaces, with the above-mentioned meanings. The next $N$ lines contain the coordinates of the peaks; line $i+1$ contains the coordinates of peak $i$, $X_i$ and $H_i$, separated by a space.

# Output data

In the `munte.out` file, you will display:
- on the first line the minimum total length of the cables, rounded to the nearest integer (for any integer $Q$, $Q.5$ is rounded to $Q+1$);
- on the second line $K$ distinct numbers between $1$ and $N$, sorted in ascending order, the numbers of the peaks where cable car stations will be established. If there are multiple variants, display any one of them.

# Constraints and clarifications

* $2 \leq N \leq 100$
* $2 \leq K \leq 30$ and $K \leq N$
* $0 \leq L, X_i, H_i \leq 100\ 000$ and $X_i < X_{i+1}$

# Example

`munte.in`
```
7 5 11
0 16
4 3
6 8
7 4
12 16
13 16
14 16
```

`munte.out`
```
22
1 3 5 6 7
```

## Explanation

- Drawing a cable directly between peaks $1$ and $5$ would have violated the restriction regarding the maximum length of a cable; moreover, a solution with $2$ cable car stations instead of $3$ would be invalid (even for large values of $L$).
- To illustrate the restriction introduced by the terrain shapes, note that peaks $1$ and $4$ could not be directly connected due to the height of peak $3$. Similarly, peaks $5$ and $7$ could not be directly connected due to the height of peak $6$.