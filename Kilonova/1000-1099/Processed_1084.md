```markdown
Consider an even natural number $N$ and the increasing ordered array $X$ formed from the first $N$ non-zero natural numbers: $X_1=1$, $X_2=2$, $\dots$, $X_N=N$.

The positions of the numbers in the array can only be modified according to rule $A$, as follows:

* if $X_1$ is an odd number, then $X_1$ is swapped with $X_2$, $X_3$ with $X_4$, $\dots$, $X_{N-1}$ with $X_N$;
* if $X_1$ is even, then $X_2$ is swapped with $X_3$, $X_4$ with $X_5$, $\dots$, $X_{N-2}$ with $X_{N-1}$, and $X_N$ with $X_1$.

By applying rule $A$ $R$ times, the array $X$ is transformed into an "A-sorted" array.

Given the natural numbers $N$, $R$, $K$, and $T$, write a program to determine:

1. The number located at position $K$ in the "A-sorted" array obtained by applying rule “A” to array $X$ $R$ times.
2. The predecessor and successor of the number $T$ in the "A-sorted" array.

# Input data

The input file `asort.in` contains on the first line a natural number $P$; the number $P$ can only have the value $1$ or $2$. The second line contains four natural numbers $N$, $R$, $K$, and $T$, in the given order, separated by a space.

# Output data

* If the value of $P$ is $1$, then only Task $1$ will be solved. In this case, the file `asort.out` will contain on the first line a natural number representing the number at position $K$ in the "A-sorted" array.
* If the value of $P$ is $2$, then only Task $2$ will be solved. In this case, the file `asort.out` will contain on the first line two natural numbers, separated by a single space, representing, in this order, the predecessor and the successor of the number $T$.

# Constraints and clarifications

* $6 \leq N \leq 10^9$, $N$ is even.
* $1 \leq R \leq 10^9$.
* $1 \leq K, T \leq N$
* If the number $T$ is located at position $1$ in the sorted array, then its predecessor is the number at position $N$. If the number $T$ is located at position $N$ in the sorted array, then its successor is the number at position $1$.
* Correct solving of Task $1$ is awarded $50\%$ of the score, and correct solving of Task $2$ is awarded $50\%$ of the score.
* For tests worth $15$ points from both tasks, with a total of $30$ points, $N \leq 1000$ and $R \leq 1000$.

# Example 1

`asort.in`
```
1
6 2 3 4 
```

`asort.out`
```
1
```

## Explanation

Task $1$ is solved. $N=6$, $R=2$, $K=3$ and $T=4$

* The initial array $X$ is `1 2 3 4 5 6`.
* After the first application of rule $"A”$, the array is `2 1 4 3 6 5`.
* After the second application of rule “A”, the sorted array is `5 4 1 6 3 2`.
* In the "A-sorted" array, the value at position $K=3$ is `1`.

# Example 2

`asort.in`
```
2
6 2 3 4 
```

`asort.out`
```
5 1
```

## Explanation

Task $2$ is solved. $N=6$, $R=2$, $K=3$ and $T=4$

* The initial array $X$ is `1 2 3 4 5 6`.
* After the first application of rule $"A”$, the array is `2 1 4 3 6 5`.
* After the second application of rule “A”, the sorted array is `5 4 1 6 3 2`.
* In the "A-sorted" array, the predecessor of the number $T=4$ is `5`, and the successor is `1`.
```