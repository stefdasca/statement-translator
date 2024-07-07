
Over a small river that flows into a large river, in a town in the heart of the mountains, there are $N$ stones, numbered from $1$ to $N$. A group of children often avoid the easy way, so they have to jump over the $N$ stones to reach the other side.

For each of these stones, its height is known, denoted as $h[i]$. The friends can choose to jump certain stones to minimize the effort needed to cross the river. Formally, from the stone with index $i$, they can reach all stones numbered with indices $i + 1,\ i + 2\ ..\ min(N, i + K)$. The effort needed to jump from stone $i$ to stone $j$ is given by the formula $[\sqrt[3]{abs(h[i] - h[j])}] + C$, where $C$ is a constant.

# Task

Calculate the minimum effort to reach from the first stone to the last.

# Input data

The first line of the file `rau.in` contains three natural numbers $N,\ K,\ C$.

The second line of the input file contains the numbers $h[i]$, for $i$ from $1$ to $N$.

# Output data

The output file `rau.out` will contain the calculated minimum effort.

Constraints and clarifications
-----------------------
* $1 \le K < N \le 5\ *\ 10^{4},\ 1 \le C \le 10^{4}$
* $1 \le h[i] \le 4\ *\ 10^{5}$
* For the calculation of the cube root, you can use $cbrt(double)$ from the $cmath$ library in $C++$
* For $15\%$ of tests, $N\ \le\ 1000$
* For other $25\%$ of tests, $N\ *\ max(h[i]) \le 10^{7}$ and $K\ =\ N\ -\ 1$

# Example
`rau.in`
```
5 2 1        
4 12 37 10 10
```
`rau.out`
```
6
```

Explanation
---
The path is: 4 -> 12 -> 10 -> 10.                                           

The cost to reach 12 is $[\sqrt[3]{8}] + 1 = 3$

The cost to reach 10 is $[\sqrt[3]{2}] + 1 = 2$

The cost to reach the last 10 is $[\sqrt[3]{0}] + 1 = 1$

The path 4 -> 37 -> 10 would be, 4 + 4 = 8
