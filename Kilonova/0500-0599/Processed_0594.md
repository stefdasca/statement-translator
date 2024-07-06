~[vaporeon.png|align=right|width=30%]

Blanche, the leader of Team Mystic, has been captured by Team Lacheta! She was taken to a base of the team that contains $N$ obstacles numbered from $1$ to $N$, each obstacle $i$ having a resistance $R[i]$. Initially, Blanche is placed in front of the $x$-th obstacle. Trying to escape, she releases Vaporeon, who destroys the $x$-th obstacle and gains attack power $A$ equal to $R[x]$.

To escape, Vaporeon must destroy all the remaining obstacles. At a moment in time when Vaporeon has destroyed all obstacles in the interval $[x, y]$, he can execute exactly one of the movements:
1. **Hydro Pump** on obstacle $x-1$, if $x-1 \geq 1$ and $R[x-1] \leq A$.
2. **Hydro Pump** on obstacle $y+1$, if $y+1 \leq N$ and $R[y+1] \leq A$.
3. **Work Up**, which increases the attack power $A$ to the **minimum** value between $R[x-1]$ and $R[y+1]$.
If only one of the obstacles exists, the attack power increases to the value of its resistance.

A **Hydro Pump** move requires effort $1$, while a **Work Up** move requires effort $K$. We denote by $E[x]$ the effort needed to escape starting from the $x$-th obstacle. $E[x]$ is equal to the minimum sum of efforts needed to destroy all $N$ obstacles, if Vaporeon started from the $x$-th obstacle.

Team Lacheta anticipated this strategy, so they study different arrangements of the obstacles, as well as different initial positions to place Blanche. They will give you the number of obstacles $N$, the effort $K$ needed for a **Work Up** move, and the resistances of the $N$ obstacles. Then, they will ask you to perform the following operations:
1. Swap two adjacent obstacles $x$ and $x + 1$.
2. For two indices $x$ and $y$, state the sum $E[x] + E[x+1] + ... + E[y]$ for the current arrangement of obstacles.

# Task
Your program will need to implement the following functions:
```cpp
int initialize(int N, int K, int* R);
```

This function is called once at the start of the program execution. The parameters $N$ and $K$ represent the number of obstacles and the effort needed for a **Work Up** move, respectively. The parameter $R$ is an array of length $N$, **indexed from 0**, with the element at position $i$ representing the resistance of the obstacle $i + 1$.

```cpp
void exchange(int x);
```
This function is called for each swap of obstacles performed. The parameter $x$ represents that the obstacles at positions $x$ and $x + 1$ are being swapped.

```cpp
long long query(int x, int y);
```

This function is called multiple times, once for each query from Team Lacheta. Given the parameters $x$ and $y$, you need to return the sum $E[x] + E[x+1] + ... + E[y]$ for the current arrangement of obstacles.

Besides the functions you need to implement, you can declare local or global variables and implement other helper functions. It is recommended that global variables and functions be declared with the `static` modifier.

# Testing
To test your solutions locally, we provide the `main.cpp` program and the `vaporeon.h` header. The `main.cpp` program reads from the `vaporeon.in` input file, calls the `initialize`, `exchange`, and `query` functions of the contestant, and displays the result returned by each call to the query function.

The input file `vaporeon.in` contains on the first line the natural numbers $N$ and $K$. The second line contains $N$ natural numbers, representing the elements of the array $R$. The following lines describe the operations:
- `1 x`, if there is a call to `exchange(x)`
- `2 x y`, if there is a call to `query(x, y)`

Each line of the `vaporeon.out` file contains, in order, the answers returned by the `query` function.

# Constraints and clarifications
* $1 \leq N \leq 100 \ 000$
* $1 \leq K \leq 1 \ 000 \ 000$
* $1 \leq R[i] \leq 1 \ 000 \ 000 \ 000$
* The total number of calls to the `exchange` and `query` functions does not exceed $200 \ 000$.
* For `20%` of the tests, $N \leq 1 \ 000$ and the total number of calls to the `exchange` and `query` functions does not exceed $2 \ 000$.

# Example
`vaporeon.in`
```
5 3 
2 3 1 4 1
2 2 2
2 1 5
1 2
2 2 2
2 1 5
```
`vaporeon.out`
```
7
38
13
41
```
Explanation
---

The performed calls are:
`initialize(5, 3, {2,3,1,4,1})`
`query(2, 2)` - returns $7$
`query(1, 5)` - returns $38$
`exchange(2)`
`query(2, 2)` - returns $13$
`query(1, 5)` - returns $41$

For the first query, Vaporeon starts from the obstacle at position $2$ with a power of $3$. He performs:
Hydro Pump $1$
Hydro Pump $3$
Work Up (gains power $4$)
Hydro Pump $4$
Hydro Pump $5$

After the `exchange` operation, the obstacles are arranged as $\{2, 1, 3, 4, 1\}$.

For the third query, Vaporeon starts from the obstacle at position $2$ with a power of $1$. He performs:
Work Up (gains power $2$).
Hydro Pump $1$
Work Up (gains power $3$)
Hydro Pump $3$
Work Up (gains power $4$)
Hydro Pump $4$
Hydro Pump $5$