> â€œWhen it feels like living's harder than dying  
For me giving up's way harder than tryingâ€

Stifon owns $N$ plots of land cultivated with corn, connected by $N-1$ bidirectional roads, ensuring that it is possible to travel from one plot to another via exactly one road. Stifon can position himself on a plot numbered $D$ and select another plot $W$, $W < D$ with $dist(D, W) \leq P$, and collect corn from the plots on the path from $D$ to $W$. We observe that for a plot $D$ there are several plots $W$ that meet the imposed criteria. Therefore, Stifon notes $Fss(D)$ as the total sum of the corn on each path $(D, W)$ with $W < D$ and $dist(D, W) \leq P$.

# Task

Now Stifon is very undecided about which plot to start harvesting from, so he asks what is the total sum if he started from any plot, more precisely the value $\\displaystyle \\sum_{i=1}^{N} Fss(i)$ mod $10^9 + 7$.

# Input data

The first line contains two numbers $N$ and $P$. The second line contains an array $V$ with $N$ elements representing the amount of corn in each plot. The next $N-1$ lines contain 2 numbers $u_i$ and $v_i$ indicating that there is a road between plots $u_i$ and $v_i$.

# Output data

The first line contains the requested value, $\\displaystyle \\sum_{i=1}^{N} Fss(i)$ mod $10^9 + 7$.

# Constraints and clarifications
~[cucuruz.png]
* $P \leq N \leq 10^5$.
* $V[i] \leq 10^9 \quad (1 \leq i \leq N)$.
* $dist(D,W)$ = the minimum number of roads on a path from D to W.

| # | Score | Constraints | 
| - | ----- | ------------ |
| 1 | 5 | $N \leq 6$ |
| 2 | 10 | $N \leq 10$ |
| 3 | 5 | $N \leq 100$ |
| 4 | 10 | $N \leq 10^4$ |
| 5 | 20 | $N \leq 5 \, 0000, P \leq 100$  |
| 6 | 10 | $P = 2$|
| 7 | 40 | Without additional constraints |

# Example 1

`stdin`
```
3 2
10 5 9 
2 1
1 3
```

`stdout`
```
58
```

## Explanation
~[g1.png]
For $D$ = 2 we can choose $W = 1$ with $Fss(2) = V[1] + V[2] = 10 + 5 = 15$.  
For $D$ = 3 we can choose either $W = 1$ or $W = 2$, $Fss(3) = V[1] + V[3] + V[1] + V[2] + V[3] = 43$.  
$Fss(1) + Fss(2) + Fss(3) = 0 + 15 + 43 = 58$.

# Example 2

`stdin`
```
10 3
679062366 599100597 187934521 236893327 61406391 912961000 46426980 729873627 889249584 650085534 
2 1
7 9
5 7
1 3
8 7
4 2
4 9
10 3
6 7
```

`stdout`
```
396699172
```

## Explanation
I don't know, boss, count them yourself!