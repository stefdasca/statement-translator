```markdown
The Galactic Empire had to abandon the well-known spacecraft due to increasingly strict pollution regulations. The administration is now required to develop a network of transplanetary tunnels through which inhabitants will travel.
The Empire consists of $N$ planets, represented as points in space. The cost of forming a transplanetary tunnel between two planets $A$ and $B$ is:
$TunnelCost[A, B] = min(|x_A - x_B|, |y_A - y_B|, |z_A - z_B|)$, where $(x_A, y_A, z_A)$ are the 3D coordinates of planet $A$ and $(x_B, y_B, z_B)$ are the 3D coordinates of planet $B$. 

# Task

The Empire has to build exactly $N-1$ tunnels to completely connect all the planets. Due to rebels, the Galactic Empire’s administration no longer has as much money as it used to and needs to use it as efficiently as possible. Find the smallest possible cost to successfully complete this project.
\
**Note:** The planets occupy distinct positions in space.

# Input data

The input contains the natural number $N$, the number of planets, on the first line.
The next $N$ lines each contain a triplet of integer values $x_k \\ y_k \\ z_k$, representing the coordinates of the planets.

# Output data

Print the minimum cost of the tunnel network on the first line.

# Constraints and clarifications

- $ 1 \\le N \\le 10^5$.
- $ -10^9 \\le x_k, y_k, z_k \\le 10^9$.
- For tests worth 50 points, $N \\le 1000$.

# Example 1

`stdin`
```
2
1 5 10
7 8 2
```

`stdout`
```
3
```

# Example 2

`stdin`
```
3
-1 -1 -1
5 5 5
10 10 10
```

`stdout`
```
11
```

# Example 3

`stdin`
```
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
```

`stdout`
```
4
```
```