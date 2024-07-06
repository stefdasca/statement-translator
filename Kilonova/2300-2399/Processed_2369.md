# Statement

Nargy and Fumeanu have gone to the mountains. They have a map of the mountain, which identifies $N$ mountain huts (numbered with distinct numbers between $1$ and $N$), located at different altitudes (hut $i$ is situated at altitude $H_i$). These huts are connected by $M$ trails. A trail connects two distinct huts and can only be traversed in one direction: from the hut situated at a lower altitude to the hut located at a higher altitude.

At one point, the two got separated, and each reached a different hut, but fortunately, each had a copy of the map. They called each other and set a meeting spot at the hut located at the **minimum** altitude among those huts they can both reach (remember, they can only go up).

To avoid such situations in the future, the two decided to determine the meeting place regardless of which huts they are in. They will write down these results on a piece of paper for each pair $i \\ j \\ (1 \\leq i < j \\leq N)$, the pairs being considered in lexicographical order. If for a certain pair there is no such meeting hut, they will write the number $0$.

# Task

Write a program to determine all this information for the two, given the mountain map.

# Input data

The input file `casute.in` contains on the first line the natural numbers $N$ and $M$ separated by spaces. The next line will contain $N$ natural numbers separated by spaces representing the altitudes of the huts, in order from $1$ to $N$. The following $M$ lines will contain two natural numbers $i \\ j$ separated by spaces, representing a trail from hut $i$ to hut $j$ (it is guaranteed that $H_i < H_j$).

# Output data

The $\frac{N \times (N - 1)}{2}$ values that the two will write on the paper can be considered as digits of a number written in base $N + 1$. The output file `casute.out` will contain on the first line the remainder of the division of that number converted to base $10$ by the number $666013$.

# Constraints and clarifications

* $1 \leq N \leq 3\ 000$;
* $1 \leq M \leq 30\ 000$;
* The altitudes of the $N$ huts are distinct integers in the interval $[1, 10^9]$
* A pair of numbers $(a\ b)$ is considered lexicographically smaller than another pair of numbers $(c\ d)$ if $a < c$ or $a = c$ and $b < d$.

# Example

`casute.in`
```
5 7
1 2 3 4 5
1 3
2 3
1 4
2 4
2 5
4 5
3 5
```

`casute.out`
```
24052
```

## Explanation

$(1\ 2) \rightarrow 3$  
$(1\ 3) \rightarrow 3$  
$(1\ 4) \rightarrow 4$  
$(1\ 5) \rightarrow 5$  
$(2\ 3) \rightarrow 3$  
$(2\ 4) \rightarrow 4$  
$(2\ 5) \rightarrow 5$  
$(3\ 4) \rightarrow 5$  
$(3\ 5) \rightarrow 5$  
$(4\ 5) \rightarrow 5$  
$3345345555_{(6)} = 36654767_{(10)} = 24052 \ (mod \ 666013)$