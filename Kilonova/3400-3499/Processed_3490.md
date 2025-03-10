# Task

We define $M(X,N)$ as the set containing all numbers $d$ from $1$ to $N$, which have the property that $\text{gcd}(d,X) > 1$, where $\text{gcd}(a,b)$ is the greatest common divisor of the numbers $a$ and $b$.

The commission has chosen a number $X$ and a number $N$, and has provided you with the set $P = M(X,N)$, with the purpose of helping you find these two numbers. However, there are multiple pairs $(X,N)$ for which the set $M(X,N)$ is the given set, so you must find the minimum value of $X$ for which there exists an $N$ such that $M(X,N) = P$. Let's denote this minimum value of $X$ with $X_{\min}$. Among all the values of $N$ for which $M(X_{\min}, N) = P$, you will have to find the maximum one (let this be $N_{\max}$).

# Input data

The first line contains an integer $K$, representing the number of numbers in $P$. The next line contains $K$ integers, representing the set $P$.

# Output data

The first line must contain two integers, $X_{\min}$ and $N_{\max}$.

# Constraints and clarifications

* $1 \leq K \leq N \leq 1\ 000\ 000$ - keep in mind that **this $N$ is the one by the commission; the $N$ you need to find ($N_{\max}$) can be greater than $1\ 000\ 000$**
* $1 \leq X \leq 1\ 000\ 000\ 000$
* $1 \leq i \leq N$, if $i \in P$
* **The given numbers are not necessarily sorted.**
* For $40$ points, $X_{\min}, K \leq 1\ 000$.
* For each test, you receive:
  * $0\%$ of the score if neither of the displayed numbers is correct or if you did not display exactly 2 numbers.
  * $50\%$ of the score if exactly one of the displayed numbers is correct.
  * $100\%$ of the score if both numbers are correct.

# Example

`stdin`
```
7
8 6 3 10 9 2 4
```

`stdout`
```
6 11
```

## Explanation

The commission chose $X = 12$ and $N = 10$, but $X_{\min} = 6$ and $N_{\max} = 11$.

If $X_{\min}$ would be $1$, $2$, $4$ or $5$, then $\text{gcd}(X_{\min},3)$ would be $1$, which cannot happen. If $X_{\min}$ would be $3$, then $\text{gcd}(X_{\min},2)$ would be $1$, which cannot happen.

If $N_{\max}$ would be $12$ or greater, $\text{gcd}(12, X_{\min}) = \text{gcd}(12, 6) = 6 > 1$, so we would have $12 \in P$, which means $12 \in \{2, 3, 4, 6, 8, 9, 10\}$, impossible.

Thus, $X_{\min} = 6$ and $N_{\max} = 11$.