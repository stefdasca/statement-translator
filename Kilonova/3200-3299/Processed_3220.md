
# Task

Given an array $a$ of length $N$, you need to handle $Q$ operations. These operations are of two types, coded as follows:
* `0 st dr x`: $a[i] = \min(a[i], x)$ for $st \leq i \leq dr$;
* `1 st dr`: display $\\sum\\limits_{i=st}^{dr} a[i]$.

# Input data

The first line contains the numbers $N$ and $Q$. The second line contains the array $a$ (indexed from $1$). On the following $Q$ lines, there is one operation per line.

# Output data

The responses to the operations of type `1`, each on a separate line.

# Constraints and clarifications

* $1 \leq N, Q \leq 2\cdot10^{5}$
* $0 \leq a[i], x \leq 10^9$
* $1 \leq st \leq dr \leq N$
* It is recommended to use the following line of code at the beginning of the `main` function to reduce the time allocated to reading input data: `cin.tie(0)->sync_with_stdio(0);`.

# Example

`stdin`
```
3 2
1 2 3
0 1 3 1
1 1 3
```

`stdout`
```
3
```

## Explanation

After the first operation, the array becomes $[1,1,1]$. The sum of indices from $1$ to $3$ is $3$.
