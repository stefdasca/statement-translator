Sure, here is the translated content:

---

The $N^2$ wizards from the Unseen University have their offices in a square matrix with a side equal to $N$. In each cell $(i, j)$ of the matrix $(0 \leq i, j \leq N - 1)$, there is a wizard's office. Next, we will identify the wizards by the coordinates of their office. The wizards are in a permanent conflict because each one wants to occupy the position of Archchancellor of the university. This conflict takes place over $T$ days (numbered from $1$ to $T$).

On each day $z \\ (1 \leq z \leq T)$, each wizard $(i, j)$ has an attack power $P(z, i, j)$. A wizard $(i, j)$ attacks all the other $N^2 - 1$ wizards, and the power with which the wizard $(i, j)$ attacks a wizard $(p, q)$ on day $z$ is $PA(z, i, j, p, q) = P(z, i, j) - dist(i, j, p, q)$. $dist(i, j, p, q)$ represents the distance between the wizards $(i, j)$ and $(p, q)$, defined as $|i - p| + |j - q|$. The effect of the attacks felt by a wizard $(p, q)$ on day z is $Pmax(z, p, q) = max \\{PA(z, i, j, p, q) | (i, j) \neq (p, q)$ and $0 \leq i, j \leq N - 1 \\}$.

The attack power of a wizard $(i, j)$ on day $z+1$ will be: $P(z+1, i, j) = z + 1 + ((P(z, i, j) + z \cdot Pmax(z, i, j))$ modulo $Q)$.

# Task

Let $S$ be the sum of the values $P(T+1, i, j), (0 \leq i,j \leq N-1)$. Determine the value ($S$ modulo $Q$).

# Input data

The first line of the input file `v2d.in` contains the natural numbers $N$, $T$ and $Q$, separated by a space. The next $N$ lines contain the attack power values of the wizards at the beginning of day $1$. Each of these lines contains $N$ natural numbers, separated by spaces. The $C$-th number $(1 \leq C \leq N)$ on the $L$-th $(1 \leq L \leq N)$ of these lines represents the value $P(1, L - 1, C - 1)$.

# Output data

The output file `v2d.out` will contain the sum of the values $P(T + 1, i, j)$, $(0 \leq i, j \leq N - 1)$, modulo $Q$.

# Constraints and clarifications

* $2 \leq N \leq 500$
* $1 \leq T \leq 50$
* $2 \leq Q \leq 30000$
* $1 \leq P(1, i, j) \leq Q + T$

# Example 1

`v2d.in`
```
3 10 10
1 2 3
4 5 6
7 8 9
```

`v2d.out`
```
2
```

# Example 2

`v2d.in`
```
5 50 30000
1000 900 800 700 30050
900 800 700 600 1000
800 700 600 1000 900
700 600 1000 900 800
600 1000 900 800 700
```

`v2d.out`
```
24385
```

---

I have preserved the mathematical values, variable names, general syntax, structure, and format, as well as the custom image format exactly as specified.