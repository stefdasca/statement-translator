Zăhărel wants to go on a trip together with $K$ of his $N$ friends (numbered from $1$ to $N$). Of course, he cannot take any group of $K$ friends with him, because the presence of certain friends is conditioned by the presence of others. Being a good connoisseur of social interactions within his group of friends, Zăhărel made a list of all $M$ existing dependencies in his group: pairs of numbers $i \\ j$ meaning that friend number $i$ will come on the trip, only if friend number $j$ also comes. We will call such a relationship a **direct dependency**.

We will further say that two friends $i$, $j$ are in **indirect dependency** if they are in direct dependency or if there is a sequence of $T \geq 1$ numbers $v_1, v_2, \dots, v_T$, so that $i$ depends directly on $v_1$, $v_p$ depends directly on $v_{p+1}$ (for $1 \leq p < T$), and $v_T$ depends directly on $j$.

Upon careful analysis of the $M$ relationships, Zăhărel observed an interesting property within his group: for any three distinct friends numbered $i$, $j$, $k$, if $i$ depends indirectly on $j$ and $i$ depends indirectly on $k$, then $j$ depends indirectly on $k$, or $k$ depends indirectly on $j$, or both.

# Task

Write a program that determines in how many ways Zăhărel can choose $K$ out of his $N$ friends to go on a trip, taking into account the $M$ dependency relationships.

# Input data

The input file `dep.in` will contain on the first line the numbers $N, M, K$. The next $M$ lines will contain pairs of numbers $i \\ j$ representing direct dependencies. 

# Output data

The output file `dep.out` will contain on the first line a single number representing in how many ways Zăhărel can choose $K$ of his $N$ friends. The result will be displayed modulo $666 \ 013$.

# Constraints and clarifications

* $1 \leq K \leq N \leq 256$
* $0 \leq M \leq \frac{N \cdot (N-1)}{2}$
* For $20\%$ of the tests $N \leq 25$
* For $40\%$ of the tests there will be no cyclic indirect dependencies ($i$ depends indirectly on $i$)

# Example

`dep.in`
```
5 8 3
1 2
2 1
1 3
2 3
4 5
5 4
4 3
5 3
```

`dep.out`
```
2
```

## Explanation

Zăhărel can go on the trip either with friends $1 \ 2 \ 3$ or with friends $3 \ 4 \ 5$.

~[dep.png]