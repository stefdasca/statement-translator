Given $n$ pairs of natural numbers. A pair consists of the number $T$, which indicates the type of the pair, and a number $x$.

# Task

* If $T$ is prime, add the number $x$ to a sum $S$.
* If $T$ is not prime and $T > 1$, subtract the number $x$ from the sum $S$.
* If $T$ is $0$, output the sum $S$.
* If $T$ is $1$, output the largest number from the Fibonacci sequence less than or equal to $x$.
The Fibonacci sequence has the property that $f_x = f_{x-1} + f_{x-2}$, ∀ $x \ge 2$, $f_0 = 1$, $f_1 = 1$.

# Input data

The file `fiboprim.in` contains $n$. Then, $n$ pairs of numbers $T$ and $x$ are read, with their meaning as described in the task.

# Output data

The file `fiboprim.out` will contain $S$ each time $T = 0$, or the largest number in the Fibonacci sequence less than $x$ when $T = 1$.

# Constraints and clarifications

* $0 \le T \le 10^6$;
* $1 \le n \le 10^6$;
* $1 \le S \le 2 \cdot 10^{10}$;
* $1 \le x \le 2 \cdot 10^4$.

| # | Score | Constraints                                       |
|---|---------|--------------------------------------------------|
| 1 | 30      | $1 \le n \le 10^3$ and $0 \le T \le 10^3$ and $T \neq 1$          |
| 2 | 30      | $1 \le n \le 10^3$ and $0 \le T \le 2 \cdot 10^3$ and $T \neq 1$ |
| 3 | 20      | $1 \le n \le 10^3$ and $T \neq 1$                          |
| 4 | 20      | $T = 1$                                          |

# Example 1

`fiboprim.in`
```
5
13 5
2 4
0 10
4 4
0 1
```

`fiboprim.out`
```
9
5
```

# Example 2

`fiboprim.in`
```
3
1 11
1 9
1 21
```

`fiboprim.out`
```
8
8
21
