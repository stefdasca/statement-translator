Octa and Goon have invented a new game.

# Task

Two sequences of natural numbers $A$ and $B$ of length $N$ and $M$ respectively are given. For each $i$ from $1$ to $N$, you must state how many values $j$, where $1 \leq j \leq M$, exist such that the sequence formed from the first $i$ elements of $A$, followed by the first $j$ elements of $B$, contains a majority element. Specifically, the sequence $[A_1, A_2, A_3, \dots, A_i, B_1, B_2, B_3, \dots, B_j]$ must contain a majority element.

We say that a sequence $x_1, x_2, \dots, x_k$ contains a majority element if there exists a value $V$ such that $V$ appears at least $\lfloor \frac{K}{2} \rfloor + 1$ times in the sequence $x$.

# Input data

The first line contains the numbers $N, M$.

The second line contains $N$ natural numbers, representing the array $A$.

The third line contains $M$ natural numbers, representing the array $B$.

# Output data

The first line will print $N$ numbers. The $i$-th number is the answer for the prefix of length $i$ from the array $A$.

# Constraints and clarifications

$\textcolor{red}{Warning!}$ Due to the large number of input and output data, we recommend adding the following lines of code at the beginning of the `main()` function.

```c++
ios_base::sync_with_stdio(false);
cin.tie(0);
cout.tie(0);
```

* $1 \leq N, M \leq 300\, 000$
* $1 \leq A_i, B_i \leq N + M$

|#|Score|Constraints|
|-|-|--------|
|1|11|$N, M \leq 300$|
|2|17|$N, M \leq 3\, 000$|
|3|29|There are at most $300$ distinct values in $A$ and $B$ combined|
|4|18|Any element appears at most $2\, 500$ times in total in $A$ and $B$|
|5|25|No other constraints|

# Example

`stdin`
```
7 10
2 2 1 3 1 1 1
1 2 3 3 3 1 1 1 2 1
```

`stdout`
```
1 3 1 0 0 1 4 
```

## Explanation

For $i = 1$, the only $j$ that works is $j = 2$. For $i = 1$ and $j = 2$, the resulting sequence is $[2, 1, 2]$, where $2$ is the majority element. However, for $i = 1$ and $j = 1$, the resulting sequence is $[2, 1]$, where neither $1$ nor $2$ are majority elements because they only appear once, whereas they should appear twice.