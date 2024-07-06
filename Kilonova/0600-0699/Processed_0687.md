```markdown
A sequence of $N$ coins numbered from $0$ to $N - 1$ is considered. On a toss, the coin $i$ has a probability $p[i]$ of landing heads, and $1 - p[i]$ of landing tails.

# Task
For $Q$ intervals $[a, b]$, you are required to find the probability that, if the coins $a, a + 1, \dots, b$ are tossed, an odd number of them will land heads.

# Interaction
The contestant will include the file `monede.h` by using the preprocessor directive `#include "monede.h"`. In this header file, a data structure `Raport` is implemented. It can be used as follows:
```cpp
Raport r;                                // r is initialized with value 0 / 1 = 0
Raport p(1, 2);                          // p represents the ratio 1 / 2
Raport q = Raport(2, 3);                 // q represents the ratio 2 / 3
bool b = (p == q);                       // b is false, because 1 / 2 != 2 / 3
Raport r = p + q;                        // r represents 1 / 2 + 2 / 3 = 7 / 6.
Raport r = p - q;                        // r represents 1 / 2 - 2 / 3 = - 1 / 6.
Raport r = p * q;                        // r represents 1 / 2 * 2 / 3 = 1 / 3.
Raport r = p / q;                        // r represents 1 / 2 : 2 / 3 = 3 / 4.
                                         // You can also calculate p * q, p / q, p - q
r -= p;                                  // r becomes 7 / 6 – 1 / 2 = 2 / 3.
                                         // You can also perform r += p, r *= p, r /= p.
```
The contestant will implement two functions. The first one is the `init` function, having the signature:
```cpp
void init(int N, const Raport p[]);
````
The commission will call this function exactly once, at the beginning of the program's execution. The function will receive through parameter $N$ (natural number) the number of coins and through the parameter $p$ the array of probabilities, indexed from $0$.

The second function is `solve`, with the signature:
```cpp
Raport solve(int a, int b);
```
The commission will call this function $Q$ times. The function receives through the parameters $a$ and $b$ ($0 \leq a \leq b < N$) two positions. The function will have to return the answer for the interval $[a, b]$.

The contestant does not implement the `main` function, only the functions indicated in the statement, and any auxiliary functions that are needed!

# Constraints and clarifications
* $1 \leq N \leq 1 \ 000 \ 000$
* $1 \leq Q \leq 1 \ 000 \ 000$
* The values $a$ and $b$ sent through the `solve` function parameters must satisfy the condition $0 \leq a \leq b < N$.
* For $23$ points, $N \leq 15, Q \leq 100$.
* For another $10$ points, $N \leq 1 \ 000, Q \leq 1\ 000$.
* For another $37$ points, $N, Q \leq 200 \ 000$.
* For another $15$ points, $p[i] \neq \frac{1}{2}$.

# Example
`Input`
```py
N = 3
p = [1/4, 1/3, 1/2]
```
`Output`
```cpp
Solve(0, 0) = 1 / 4;
Solve(1, 1) = 1 / 3;
Solve(0, 1) = 5 / 12
Solve(0, 2) = Solve(1, 2) = Solve(2, 2) = 1 / 2
```
```